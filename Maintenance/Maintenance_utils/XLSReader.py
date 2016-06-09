'''
Created on 07-Jun-2016

@author: prakash.selvam
'''
import xlrd

class xlsreader(object):
    def __init__(self):
        '''
        '''
        pass
    def readTestCase(self,file_name,SheetNo):
        #file_name = "testdata.xls"
        #reading a table with header and converting it to a list of Dictionary
        try:
            xlfile = xlrd.open_workbook(file_name)
        except IOError:
            raise
        sheet = xlfile.sheet_by_index(int(SheetNo))
        keys = [sheet.cell(0, col_index).value for col_index in xrange(sheet.ncols)]
        dict_list = []
        for row_index in xrange(1, sheet.nrows):
            d = {}
            for col_index in xrange(sheet.ncols):
                if type(sheet.cell(row_index, col_index).value) is float:
                    d[keys[col_index]] = str(sheet.cell(row_index, col_index).value).split('.')[0]
                else:
                    d[keys[col_index]] = str(sheet.cell(row_index, col_index).value)
            dict_list.append(d)
        return dict_list