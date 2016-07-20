'''
Created on 07-Jun-2016

@author: prakash.selvam
'''
from XLSReader import xlsreader
from Maintenance.models import MaintenanceDetails
from Maintenance import log_rotator
from StdSuites.Table_Suite import row

class DueDataLoader(object):
    '''
    '''
    def __init__(self):
        '''
        '''
        self.UtilLogger = log_rotator.baseutil_logger()
        pass
    def read_due_data(self,apartmentid,file_name,SheetNo):
        try:
            xlsreaderObj = xlsreader()
            due_dict_list = xlsreaderObj.readTestCase(file_name, SheetNo)
            month_year_due = xlsreaderObj.readMonthFromSheet(file_name, SheetNo)
            self.write_due_data_to_db(due_dict_list,apartmentid,month_year_due)
            return {'status': 'success', 'msg':'successfully entered'}
        except:
            raise
        
    def write_due_data_to_db(self,due_dict_list,apartmentid,month_year_due):
        for row in due_dict_list:
            resultSet = MaintenanceDetails.objects.filter(block_name = row['Block'], flat_number = row['Flat'], 
                                                        apartment_id = apartmentid, month_year = month_year_due)
            self.UtilLogger.debug("Result set:%s: %s",resultSet,str(row))
            if (resultSet.count()>0):
                resultSet.update(
                    maintenance_due = row["MaintenenceDue"],
                    maintenance_due_date = row["DueDate"])
            else:
                MaintenanceDetails.objects.create(
                        maintenance_due = row["MaintenenceDue"],
                        maintenance_due_date = row["DueDate"],
                        block_name = row['Block'],
                        flat_number = row['Flat'],
                        month_year = month_year_due,
                        apartment_id = apartmentid)
                                