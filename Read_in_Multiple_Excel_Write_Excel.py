# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 22:44:22 2020

@author: heart
"""

import pandas

class DataInconsistency:
    def __init__(self):

        # initialize data dictionary
        self.di = {
                   'Org ID': [],
                   'Validation Type': [],
                   'Validation Error': []
                   }
        

        self.header = None

    def collect_stats(self, freq, org, k1):
        for row in freq.index:
            if freq.loc[row, 'Compared Results'] == 'Not Matched':
                self.di['Validation Type'].append('Summary of Missing Values')
                self.di['Validation Error'].append(freq.loc[row, 'Variables in File'])
                self.di['Org ID'].append(org)
                
    def set_header(self, header):
        if self.header is None:
            self.header = header
            
    def write(self, outfile):
        df = pandas.DataFrame(self.df)
        
        with pandas.ExcelWriter(outfile) as writer:
            
            df.to_excel(writer, sheet_name = 'Data Inconsistency Report', index = None, startrow = 1)
            
            work_book = writer.book
            left_align_format = work_book.add_format()
            left_align_format.set_align("left")
            count_format = work_book.add_format({"num_format": "#, ##0})
            wrap_format = work_book.add_format()
            wrap_format.set_text_wrap()
                                                     
            full_boarder = work_book.add_format(
                    {"boarder": 1,
                     "boarder_color": "#000000"}
                    )
            worksheet = writer.sheets['Data Inconsistency Report']
            worksheet.set_column(1, 0, 30)
            worksheet.set_column(2, 0, 30)
            worksheet.set_column(3, 0, 30)
            
            worksheet.merge_range("A1:D1", self.header, wrap_format)
            worksheet.set_row(0, 60)
            
            