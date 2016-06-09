'''
Created on 07-Jun-2016

@author: prakash.selvam
'''
from XLSReader import xlsreader
from Maintenance.models import PreRegistrations
from Maintenance import log_rotator

class PeopleDataLoader(object):
    '''
    '''
    def __init__(self):
        '''
        '''
        self.UtilLogger = log_rotator.baseutil_logger()
        pass
    def read_people_data(self,apartmentid,file_name,SheetNo):
        try:
            xlsreaderObj = xlsreader()
            people_dict_list = xlsreaderObj.readTestCase(file_name, SheetNo)
            self.write_people_data_to_db(people_dict_list,apartmentid)
            return {'status': 'success', 'msg':'successfully entered'}
        except:
            raise
        
    def write_people_data_to_db(self,people_dict_list,apartmentid):
        for row in people_dict_list:
            resultSet = PreRegistrations.objects.filter(block_name = row['Block'], flat_number = row['FlatNumber'], apartment_id = apartmentid)
            self.UtilLogger.debug("Result set:%s: %s",resultSet,str(row))
            if (resultSet.count()>0):
                resultSet.update(
                    first_name = row['Firstname'],
                    last_name = row['Lastnme'],
                    mobile_number = row['MobileNumber'], 
                    email_id = row['EmailID'],
                    type_occupancy = row['TypeofOccupancy'])
            else:
                PreRegistrations.objects.create(
                        first_name = row['Firstname'],
                        last_name = row['Lastnme'],
                        block_name = row['Block'],
                        flat_number = row['FlatNumber'],
                        mobile_number = row['MobileNumber'], 
                        email_id = row['EmailID'],
                        type_occupancy = row['TypeofOccupancy'],
                        apartment_id = apartmentid)
                                