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

s3_client = boto3.client("s3")
s3_resource = boto3.resource('s3')

def generateSchema(cols):
    """generates schema for spark dataframe creation"""
    schema = StructType([StructField(col,StringType()) for col in cols])
    return schema

def copyParquetToOutbound(output, target, prefix):

    resp = s3_client.list_objects_v2(Bucket=output, Prefix = prefix)
    
    for obj in resp['Contents']:
        key = obj["Key"]
        copy_source = {
            'Bucket': output,
            'Key': key
        }
        s3_resource.meta.client.copy(copy_source, target, key)
        
def moveRawZipFileToT1(file, src, dest, prefix):
    
    #Copy the original file into T1 and delete the file from source 
    copy_source = {
            "Bucket": src,
            "Key": file
            }
    s3_resource.meta.client.copy(copy_source, dest, f"{prefix}/{file}")
    s3_client.delete_object(Bucket=src, Key=file)

#
# main
#
    
#parameters to be given while running this job manually --programName, --programFiletype, --filename
args = getResolvedOptions(sys.argv,
                          ['inputBucketName',
                           'outputBucketName',
                           'configBucketName',
                           'targetOutboundBucket',
                           'filename',
                           'interface',
                           'debug_level'])

today = datetime.today()
year = today.year
month = today.month
day = today.day
date = f"{year}-{month}-{day}"


inputBucketName = args['inputBucketName']
outputBucketName = args['outputBucketName']
configBucketName = args['configBucketName']
targetOutboundBucket = args['targetOutboundBucket']
filename = args['filename']
interface = args['interface']
debug = int(args['debug_level'])

print(f"inputBucketName={inputBucketName}, " +
      f"outputBucketName={outputBucketName}, " +
      f"configBucketName={configBucketName}, " +
      f"targetOutboundBucket={targetOutboundBucket}, " +
      f"filename={filename}, " +
      f"interface={interface}. ")


#
# loads column names and their lengths from config
#
obj = s3_client.get_object(Bucket=f"{configBucketName}", Key='config/fixed_file_config.json')
data = obj.get('Body').read()
config = json.loads(data)[interface]

sc = SparkContext()
sc.setLogLevel('ERROR')
spark = SparkSession.builder \
        .appName("parquet conversion").master("local[*]")\
        .config("spark.sql.shuffle.partitions","3")\
        .config("spark.sql.parquet.compression.codec", "uncompressed")\
        .getOrCreate()

#
# list for all input files starting as SUCCESS.T#EFT.UN.ACOT.NGD{interface}.
#

#if filename == "ALL":
#    resp = s3_client.list_objects_v2(Bucket=inputBucketName, Prefix=f"SUCCESS.T#EFT.UN.ACOT.NGD{interface}.")
#    files = []
#    for obj in resp['Contents']:
#        files.append(obj["Key"])
#else:
#    files = [filename]
    
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
    if program is None:
        raise NameError(f"File {filename} is not a {interface} file. ")
    
    print(f"Processing {program} program file {filename} ... ")
    
    # read data from the file
    table_array = []
    obj = s3_client.get_object(Bucket=inputBucketName, Key=filename)
    data = obj.get("Body").read()
    error = 0
    trailer_code_length = cfg["trailer_fields"]["code"]
    line_num = 0
    
    for line in data.splitlines():
        line_num += 1
        if line_num == 1:
            # read and verify header code
            header_code_length = cfg["header_fields"]["code"]
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
    outputPath = f"s3://{outputBucketName}/{interface}/{program}/parquet/{date}/"

    df.write.option("maxRecordsPerFile", 100) \
        .option("compression","uncompressed") \
        .mode("overwrite") \
        .format("parquet").save(outputPath)

    del df

    # Copy parquet to outbound folder
    prefix =f"{interface}/{program}/parquet/{date}/"
    copyParquetToOutbound(outputBucketName, targetOutboundBucket, prefix)

    # Copy the original file into T1 and delete the file from source 
    #prefix = f"{interface}/{program}/original/{date}"
    #moveRawZipFileToT1(filename, inputBucketName, outputBucketName, prefix)

    print(f"Done processing program {program} file {filename}. ")
    
print("Job finished! ")


