#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 13:33:18 2020

@author: AWSCLOUD\l6oi
"""

import sys
from pyspark.sql import SparkSession
#from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
#from awsglue.context import GlueContext
#from awsglue.job import Job
#from awsglue.dynamicframe import DynamicFrame
#from pyspark.sql.functions import *
from pyspark.sql.types import StructType, StructField, StringType
from datetime import datetime
import boto3
#from pyspark.sql.window import Window
import json
import re

# schema to host the table column names - and set up them as string
def generateSchema(cols):
    """generates schema for spark dataframe creation"""
    schema = StructType([StructField(col,StringType()) for col in cols])
    return schema

#
# main
#
    
#parameters to be given while running this job manually --programName, --programFiletype, --filename
""" The AWS Glue getResolvedOptions(args, options) utility function gives you access to the arguments
    that are passed to your script when you run a job. To use this function, start by importing it 
    from the AWS Glue utils module, along with the sys module: """
args = getResolvedOptions(sys.argv,
                          ['inputBucketName',
                           'outputBucketName',
                           'configBucketName',
                           'targetOutboundBucket',
                           'filename',
                           'debug_level'])

today = datetime.today()
year = today.year
month = today.month
day = today.day
# This one is used for the T1 and outbound 
date = f"{year}-{month}-{day}"


inputBucketName = args['inputBucketName']
outputBucketName = args['outputBucketName']
configBucketName = args['configBucketName']
targetOutboundBucket = args['targetOutboundBucket']
filename = args['filename']
debug = int(args['debug_level'])

print(f"inputBucketName={inputBucketName}, " +
      f"outputBucketName={outputBucketName}, " +
      f"configBucketName={configBucketName}, " +
      f"targetOutboundBucket={targetOutboundBucket}, " +
      f"filename={filename}. ")

# S3.Client - A low-level client representing Amazon Simple Storage Service (S3)
# use this to retrieve the files 
s3_client = boto3.client("s3")

# this will be used later for copy/delete
s3_resource = boto3.resource('s3')

#
# loads column names and their lengths from config
#
obj = s3_client.get_object(Bucket=f"{configBucketName}", Key='config/1800_fixed.json')

# whole file Body is read as string
data = obj.get('Body').read()

# Python dictionary
config = json.loads(data)

# set up log level
sc = SparkContext()
sc.setLogLevel('ERROR')

# create Spark Session to create DataFrame
spark = SparkSession.builder \
        .appName("parquet conversion").master("local[*]")\
        .config("spark.sql.shuffle.partitions","3")\
        .config("spark.sql.parquet.compression.codec", "uncompressed")\
        .getOrCreate()

#
# list for all input files starting as SUCCESS.T#EFT.UN.ACOT.NGD1800.
#

# if filename == "ALL", files with prefix will be checked or listed
# if filename != "ALL", each individual files will be listed
if filename == "ALL":
    resp = s3_client.list_objects_v2(Bucket=inputBucketName, Prefix="SUCCESS.T#EFT.UN.ACOT.NGD1800.")
    files = []
    for obj in resp['Contents']:
        files.append(obj["Key"])
else:
    files = [filename]
    
# process all the files in a loop
for filename in files:
    program = None
    cfg = None
    for key in config.keys():
        pat = config[key]["filename_pat"]
        if re.match(pat, filename):
            program = key
            cfg = config[key]
            break

# If filename does not match any of the pattern, then it will go to next file
    if program is None:
        print(f"File {filename} is not 1800 file. ")
        continue
    
    print(f"Processing {program} program file {filename} ... ")
    
    # read data from the file
    table_array = []
    obj = s3_client.get_object(Bucket=inputBucketName, Key=filename)
    
    # byte array
    data = obj.get("Body").read()
    error = 0
    trailer_code_length = cfg["trailer_fields"]["code"]
    # used to check record counts
    line_num = 0
    
    for line in data.splitlines():
        line_num += 1
        if line_num == 1:
            # read and verify header code
            header_code_length = cfg["header_fields"]["code"]
            #check header if equal to header in Json
            header_code = line[0:header_code_length]
            header_code = header_code.decode("latin_1")
            if cfg["header_code"] != header_code:
                print(f"Invalid header code '{header_code}'. ")
                error = 1
                break
            continue
        
        # is it a trailer line?
        trailer_code = line[0:trailer_code_length]
        trailer_code = trailer_code.decode("latin_1")
        if cfg["trailer_code"] == trailer_code:
            # last line
            trailer_date_len = cfg["trailer_fields"]["date"]
            trailer_count_len = cfg["trailer_fields"]["count"]
            count_start = trailer_code_length + trailer_date_len
            count_end = trailer_code_length + trailer_date_len + trailer_count_len
            expected_count = int(line[count_start: count_end].decode("latin_1"))
            if expected_count != line_num - 2:
                print(f"File has {line_num - 2} data rows. Expect {expected_count} rows. ")
            break
        
        # read data row
        pos = 0
        fields = cfg["data_fields"]
        line_len = len(line)
        table_row = {}
        
        for col in fields.keys():
            field_len = fields[col]
            if pos + field_len > line_len:
                print(f"ERROR: line {line_num} is too short at {line_len} characters. Expect {pos + field_len}. ")
                value = ""
            else:
                value = line[pos: pos + field_len]
                value = value.decode("latin_1").strip()
            table_row[col] = value
            pos += field_len
            
        table_array.append(table_row)
        
        if debug == 1:
            print(f"Data row {line_num - 1}: ", table_row, ". ")
            
        # end of data line
        
    # end of reading from a file
    
    del data
    if error != 0:
        continue
    
    # create spark sql DataFrame
    cols = cfg["data_fields"].keys()
    schema = generateSchema(cols)
    df = spark.createDataFrame(table_array, schema)
    #df.show(1)
    
    # create parquet
    outputPath = f"s3://{outputBucketName}/1800/{program}/parquet/{date}/"

    df.write.option("maxRecordsPerFile", 100) \
        .option("compression","uncompressed") \
        .mode("overwrite") \
        .format("parquet").save(outputPath)

    del df

    #s3 copy to outbound folder
    prefix =f"1800/{program}/parquet/{date}/"
    resp = s3_client.list_objects_v2(Bucket=outputBucketName, Prefix = prefix)
    for obj in resp['Contents']:
        key = obj["Key"]
        copy_source = {
            'Bucket': outputBucketName,
            'Key': key
        }
        s3_resource.meta.client.copy(copy_source, targetOutboundBucket, key)
        
    
    # #Copy the original file into T1 and delete the file from source 
    # copy_source = {
    #         "Bucket": inputBucketName,
    #         "Key": filename
    #         }
    # s3_resource.meta.client.copy(copy_source, outputBucketName, f"1800/{program}/original/{date}/{filename}")
    # s3_client.delete_object(Bucket=inputBucketName, Key=filename)

    print(f"Done processing program {program} file {filename}. ")
    
    # end of processing file
    
print("Job finished! ")


