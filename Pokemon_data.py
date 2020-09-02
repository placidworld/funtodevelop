# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 10:49:49 2020

@author: heart
"""

import pandas as pd

df = pd.read_csv('pokemon_data.csv')

print(df.head(3))



#!/usr/bin/python3

import sys
import pandas
import numpy
import os
import re

#current_mon = "202004"
#previous_mon = "202003"

#current_mon = "2004"
#previous_mon = "2003"

# Define file path 
path = 'C:\\Work\\Iddoc\\IDDOC_EXCEL_COMPARISON\\pythonExcelComparision\\NGACOExcelFilesCmp\\'

# https://realpython.com/python-lambda/#first-example
pandas.set_option('display.float_format', lambda x: '%.3f' % x)

def compare_excel(infile1, infile2, outfile, sheet=None):
    
    print("Comparing whole file ...")
    
    excel1 = pandas.read_excel(infile1, sheet_name=sheet, convert_float = False, header=None, index_col=None, dtype="object")
    excel2 = pandas.read_excel(infile2, sheet_name=sheet, convert_float = False, header=None, index_col=None, dtype="object")
    
# Class for writing DataFrame objects into excel sheets.
# Default is to use xlwt for xls, openpyxl for xlsx. See DataFrame.to_excel for typical usage.
    with pandas.ExcelWriter(outfile) as writer:
        for name1, sheet1 in excel1.items():
            if (name1 not in excel2):
                continue

            print("Comparing sheet: {}".format(name1))
            
            sheet2 = excel2[name1]

            compare_result = sheet1.isin(sheet2).values
            rows,cols=numpy.where(compare_result==False)

            for row,col in zip(rows, cols):
                if (row >= sheet1.index.size or row >= sheet2.index.size):
                    continue
                if (col >= sheet1.columns.size or col >= sheet2.columns.size):
                    continue

                a = sheet1.at[row, col]
                b = sheet2.at[row, col]

                if (a is numpy.nan and b is numpy.nan):
                    continue
                elif (a is numpy.nan):
                    sheet1.at[row, col] = "None => {}".format(b)
                    continue
                elif (b is numpy.nan):
                    sheet1.at[row, col] = "{} => None".format(a)
                    continue

                try:
                    str1 = str(a).replace(",", "").replace("$", "")
                    str2 = str(b).replace(",", "").replace("$", "")
                    if (str1 == "nan" or str2 == "nan"):
                        continue
                    val1 = float(str1)
                    val2 = float(str2)
                    if (val1 == 0):
                        sheet1.at[row, col] = "{} => {}".format(a, b)
                    else:
                        sheet1.at[row, col] = "({:.2%})".format((val2 - val1) / val1)
                except ValueError as e:
                    sheet1.at[row, col] = "{} => {}".format(a, b)

# Using index = False to avoid creating an index in a saved file
            sheet1.to_excel(writer, sheet_name = name1, header=None, index = False)

def compare_phi(infile1, infile2, summary_file, diff_file, sheet, header):
    
    print("Calculating phi ...")
    
    excel1 = pandas.read_excel(infile1, sheet_name=sheet, convert_float = False, header=header, index_col=None)
    excel2 = pandas.read_excel(infile2, sheet_name=sheet, convert_float = False, header=header, index_col=None)
    
    #excel1.sort_values("MBI", inplace=True, )
    #excel2.sort_values("MBI", inplace=True)
    
    # Return the number of elements in the underlying data.
    rows1 = excel1.index.size
    rows2 = excel2.index.size
    
    both_df = pandas.merge(excel1, excel2, on="MBI", how="inner")
    both_rows = both_df.index.size
    
    first_name_change = 0
    last_name_change = 0
    addr_change = 0
    gender_change = 0
    date_change = 0
    reason_change = 0
    
    for row in range(0, both_rows):
        if (both_df.at[row, "First Name_x"] != both_df.at[row, "First Name_y"]):
            first_name_change += 1
            
        if (both_df.at[row, "Last Name_x"] != both_df.at[row, "Last Name_y"]):
            last_name_change += 1
            
        if (both_df.at[row, "Address_x"] != both_df.at[row, "Address_y"] or
            both_df.at[row, "State_x"] != both_df.at[row, "State_y"] or
            both_df.at[row, "Zip Code_x"] != both_df.at[row, "Zip Code_y"]):
            addr_change += 1
            
        if (both_df.at[row, "Gender_x"] != both_df.at[row, "Gender_y"]):
            gender_change += 1
            
        if (both_df.at[row, "Date of Exclusion_x"] != both_df.at[row, "Date of Exclusion_y"]):
            date_change += 1

        if (both_df.at[row, "Reason for Exclusion_x"] != both_df.at[row, "Reason for Exclusion_y"]):
            reason_change += 1
        
    summary = pandas.DataFrame({
            "Type": ["Excluded Beneficiaries in Previous Quarter",
                     "Excluded Beneficiaries in Current Quarter",
                     "Excluded Beneficiaries in Both Quarter",
                     "Excluded Beneficiaries in Previous Quarter only",
                     "Excluded Beneficiaries in Current Quarter only",
                     "In Both Files: First Name Changed",
                     "In Both Files: Last Name Changed",
                     "In Both Files: Address Changed",
                     "In Both Files: Gender Changed",
                     "In Both Files: Date of Exclusion Changed",
                     "In Both Files: Reason for Exclusion Changed"],
            "Count": [rows1, rows2, both_rows, rows1 - both_rows, rows2 - both_rows,
                      first_name_change, last_name_change, addr_change, gender_change, date_change, reason_change]
            })
    
    keys = both_df["MBI"]
    only1 = excel1[~excel1["MBI"].isin(keys)]
    only2 = excel2[~excel2["MBI"].isin(keys)]
    
    with pandas.ExcelWriter(summary_file) as writer:
    
        # summary sheet
        summary.to_excel(writer, sheet_name = "Summary", index=False)
    
        workbook = writer.book
        count_format = workbook.add_format({"num_format": "#,##0"})
    
        worksheet = writer.sheets["Summary"]
        worksheet.set_column("A:A", 60)
        worksheet.set_column("B:B", 18, count_format)
        
    with pandas.ExcelWriter(diff_file) as writer:
        only1.to_excel(writer, sheet_name = "Only in previous", index=False)
        only2.to_excel(writer, sheet_name = "Only in current", index=False)


def compare_phi_6_3(infile1, infile2, summary_file, diff_file, header, index_col):
    
    excel1 = pandas.read_excel(infile1, sheet_name=None, header=header, index_col=None)
    excel2 = pandas.read_excel(infile2, sheet_name=None, header=header, index_col=None)
  
    diff_writer = pandas.ExcelWriter(diff_file)
    summary_writer = pandas.ExcelWriter(summary_file)
    summary_book = summary_writer.book
    count_format = summary_book.add_format({"num_format": "#,##0"})
    
    sheet_list_1 = list(excel1)
    sheet_list_2 = list(excel2)
    
    for i in range(0, len(sheet_list_1)):
        
        name1 = sheet_list_1[i]
        name2 = sheet_list_2[i]
        
        sheet1 = excel1[name1]
        sheet2 = excel2[name2]

# With loc and iloc you can do practically any data selection operation on DataFrames you can think of. 
# loc is label-based, which means that you have to specify rows and columns based on their row and column labels. 
# iloc is integer index based, so you have to specify rows and columns by their integer index like you did in the previous exercise.      
        
        if sheet1.iloc[0, 0] == "PREF":
            provider_type = "PREF"
        else:
            provider_type = "PART"
            
        sheet1 = sheet1.loc[lambda df: df['Provider Type'] == provider_type, :]
        sheet2 = sheet2.loc[lambda df: df['Provider Type'] == provider_type, :]
        
        if "Physician" in name1:
            index_name = "Individual NPI"
        else:
            index_name = "Organization NPI"
        
        # remove duplicate records in previous month
        previous_records = len(sheet1.index)
        sheet1.drop_duplicates(index_name, inplace=True)
        sheet1.set_index(index_name, inplace=True)
        previous_duplicate_records = previous_records - len(sheet1.index)
        
        # remove duplicate records in current month
        current_records = len(sheet2.index)
        sheet2.drop_duplicates(index_name, inplace=True)
        sheet2.set_index(index_name, inplace=True)
        current_duplicate_records = current_records - len(sheet2.index)
        
        # remove Unnamed columns
        columns = list(sheet1.columns)
        for c in sheet1.columns:
            if isinstance(c, str) and "Unnamed" in c:
                columns.remove(c)
                
        sheet1 = sheet1.loc[:, columns]
        sheet2 = sheet2.loc[:, columns]
        
        print("Comparing sheet: " + str(name1) + ", index: " + str(index_name))
                
        merged = pandas.merge(sheet1, sheet2, left_index=True, right_index=True, how="outer")
        
        # remove dupliate keys
        rows = list(dict.fromkeys(merged.index))
        
        result_sheet = pandas.DataFrame(index = rows, columns = columns, dtype = 'object')
        result_sheet.index.name = index_name
        
        both_records = 0
        changed_records = 0
        
        for row in rows:
            if merged.loc[row, 'Provider Type_x'] == provider_type and merged.loc[row, 'Provider Type_y'] == provider_type:
                both_records += 1
                
            changed = 0
            for col in columns:
                cell1 = merged.loc[row, col + "_x"]
                cell2 = merged.loc[row, col + "_y"]
                
                str1 = str(cell1)
                str2 = str(cell2)
                
                if "incurred" in col or "amount" in col:
                    f1 = "${:,.2f}"
                    f2 = "${:,.2f}"
                    if isinstance(cell1, str):
                        cell1 = cell1.replace("$", "").replace(",", "")
                        if "(" in cell1:
                            # negative value
                            cell1 = cell1.replace("(", "").replace(")", "")
                            cell1 = - float(cell1)
                        else:
                            cell1 = float(cell1)
                    if isinstance(cell2, str):
                        cell2 = cell2.replace("$", "").replace(",", "")
                        if "(" in cell2:
                            # negative value
                            cell2 = cell2.replace("(", "").replace(")", "")
                            cell2 = - float(cell2)
                        else:
                            cell2 = float(cell2)
                else:
                    if isinstance(cell1, float):
                        f1 = "{:,.0f}"
                    else:
                        f1 = "{}"
                        
                    if isinstance(cell2, float):
                        f2 = "{:,.0f}"
                    else:
                        f2 = "{}"
                                    
                try:
                    if str1 == 'nan' and str2 == 'nan':
                        result_sheet.loc[row, col] = ""
                    
                    elif str1 == 'nan':
                        result_sheet.loc[row, col] = ("None => " + f2).format(cell2)
                        changed = 1
                    
                    elif str2 == 'nan':
                        result_sheet.loc[row, col] = (f1 + " => None").format(cell1)
                        changed = 1
                    
                    elif cell1 != cell2:
                        changed = 1
                        if isinstance(cell1, str) or isinstance(cell2, str) or cell1 == 0:
                            result_sheet.loc[row, col] = (f1 + " => " + f2).format(cell1, cell2)
                        else:
                            f = f1 + " => " + f2 + " ({:.1%})"
                            result_sheet.loc[row, col] = f.format(cell1, cell2, (cell2-cell1)/cell1)
                    else:
                        result_sheet.loc[row, col] = f1.format(cell1)
                except ValueError as e:
                    print("error: " + str(e))
                    print("sheet: " + name1 + ", NPI: " + str(row) + ", column: " + str(col) + ", cell1: " + str1 + ", cell2: " + str2)
                    #result_sheet.loc[row, col] = f1.format(cell1)
                    break
                
            if changed == 1:
                changed_records += 1
        
        result_sheet.to_excel(diff_writer, sheet_name = name1, index = True)
        s = diff_writer.sheets[name1]
        s.set_column(0, 1, 20)
        s.set_column(2, 2, 10)
        s.set_column(3, 3, 50)
        s.set_column(4, 13, 40)
        
        summary = pandas.DataFrame({
                'Type': ['Records in Previous Month',
                         'Records in Current Month',
                         'Records in Both Months',
                         'Records in Previous Month Only',
                         'Records in Current Month Only',
                         'Duplicate Records in Previous Month',
                         'Duplicate Records in Current Month',
                         'Records Changed'],
                'Count': [previous_records,
                          current_records,
                          both_records,
                          previous_records - both_records,
                          current_records - both_records,
                          previous_duplicate_records,
                          current_duplicate_records,
                          changed_records]
                })
    
        summary.to_excel(summary_writer, sheet_name = name1, index=False)
        summary_sheet = summary_writer.sheets[name1]
        summary_sheet.set_column("A:A", 60)
        summary_sheet.set_column("B:B", 18, count_format)
        
    diff_writer.save()
    summary_writer.save()
       
        
        
def compare_phi_6_4(infile1, infile2, outfile, sheet, header):
    
    excel1 = pandas.read_excel(infile1, sheet_name=sheet, convert_float = False, header=header, index_col=None)
    excel2 = pandas.read_excel(infile2, sheet_name=sheet, convert_float = False, header=header, index_col=None)

    #excel1.sort_values("MBI", inplace=True, )
    #excel2.sort_values("MBI", inplace=True)
    
    rows1 = excel1.index.size
    rows2 = excel2.index.size
    
    both_df = pandas.merge(excel1, excel2, on="Current MBI", how="inner")
    both_rows = both_df.index.size
    
    first_name_change = 0
    last_name_change = 0
    gender_change = 0
    
    for row in range(0, both_rows):
        if (both_df.at[row, "First Name_x"] != both_df.at[row, "First Name_y"]):
            first_name_change += 1
            
        if (both_df.at[row, "Last Name_x"] != both_df.at[row, "Last Name_y"]):
            last_name_change += 1
            
        if (both_df.at[row, "Gender_x"] != both_df.at[row, "Gender_y"]):
            gender_change += 1
            
    
    summary = pandas.DataFrame({
            "Type": ["Entitled Beneficiaries in Previous Month",
                     "Entitled Beneficiaries in Current Month",
                     "Entitled Beneficiaries in Both Months",
                     "Entitled Beneficiaries in Previous Month only",
                     "Entitled Beneficiaries in Current Month only",
                     "In Both Files: First Name Changed",
                     "In Both Files: Last Name Changed",
                     "In Both Files: Gender Changed"],
            "Count": [rows1, rows2, both_rows, rows1 - both_rows, rows2 - both_rows,
                      first_name_change, last_name_change, gender_change]
            })
    

    with pandas.ExcelWriter(outfile) as writer:
        # summary sheet
        summary.to_excel(writer, sheet_name = "Summary", index=False)


def do_process(infile1, infile2, report_num):
    # generate output file name
    fname = infile2.split(".")
    fname[0] += "_Validation"
    outfile = ".".join(fname)
    
    fname = infile2.split(".")
    fname[0] += "_Summary"
    outfile2 = ".".join(fname)
    
    fname = infile2.split(".")
    fname[0] += "_Differences"
    outfile3 = ".".join(fname)

    path1 = path + infile1
    path2 = path + infile2
    outfile = path + outfile
    outfile2 = path + outfile2
    outfile3 = path + outfile3
    
    print("Input file 1: " + path1)
    print("Input file 2: " + path2)
            
    if report_num == "6_3":
        print("Output file: " + outfile)
        compare_phi_6_3(path1, path2, outfile2, outfile3, header=5, index_col=2)
        
    elif report_num == "6_4":
        print("Output file: " + outfile)
        compare_phi_6_4(path1, path2, outfile, sheet=0, header=5)
        
    elif report_num == '1-2' or report_num == '1_2':
        print("Output file: " + outfile)
        print("Output file: " + outfile3)
        compare_phi(path1, path2, outfile, outfile3, sheet=0, header=3)
        
    else:
        print("Output file: " + outfile)
        compare_excel(path1, path2, outfile)
        
if __name__ == '__main__':

    #if (len(sys.argv) != 4):
    #    print("Usage: " + sys.argv[0] + " <infile1> <infile2> <outfile>")
    #    sys.exit(1)

    #infile1 = sys.argv[1]
    #infile2 = sys.argv[2]
    #outfile = sys.argv[3]
    #infile1 = "C:\\Work\\Iddoc\\IDDOC_EXCEL_COMPARISON\\pythonExcelComparision\\NGACOExcelFilesCmp\\VTAPM_6_2_F101_Runout_20200317.xlsx"
    #infile2 = "C:\\Work\\Iddoc\\IDDOC_EXCEL_COMPARISON\\pythonExcelComparision\\NGACOExcelFilesCmp\\VTAPM_6_2_F101_Runout_20200421.xlsx"
    #outfile = "C:\\Work\\Iddoc\\IDDOC_EXCEL_COMPARISON\\pythonExcelComparision\\NGACOExcelFilesCmp\\VTAPM_6_2_F101_Runout_Validation_20200422.xlsx"

 #   infile1 = "C:\\Work\\Iddoc\\IDDOC_EXCEL_COMPARISON\\pythonExcelComparision\\NGACOExcelFilesCmp\\V119 5-1 (Monthly) - March 2020.xlsx"
 #   infile2 = "C:\\Work\\Iddoc\\IDDOC_EXCEL_COMPARISON\\pythonExcelComparision\\NGACOExcelFilesCmp\\5-1 V119 (Monthly) - April 2020.xlsx"
 #   outfile = "C:\\Work\\Iddoc\\IDDOC_EXCEL_COMPARISON\\pythonExcelComparision\\NGACOExcelFilesCmp\\NGACO_5_1_V119_Validation_20200415.xlsx"
 
    model = input("Enter Program/Model, NGACO/VTAPM/SSP:  ")
    report_num = input("Enter report number:  ")
    current_mon = input("Enter report month current (YYYYMM): ")
    previous_mon = input("Enter report month previous (YYYYMM): ")    
    infile1 = None
    infile2 = None
    tag = None
    tag1 = None
    
    pattern = re.compile("^" + model + "_" + report_num + "_([A-Za-z0-9]+)_")
    
    files = os.listdir(path)
    files.sort()

    for fname in files:
        
        if "Validation" in fname:
            continue
       
        if "Summary" in fname:
            continue

        if "Differences" in fname:
            continue
        
        m = pattern.match(fname)
        if not m:
            continue
        
        tag = m.group(1)
                
        if previous_mon in fname:
            infile1 = fname
            tag1 = tag
            
        elif current_mon in fname:
            infile2 = fname
            if tag1 is not None and tag == tag1:
                do_process(infile1, infile2, report_num)

