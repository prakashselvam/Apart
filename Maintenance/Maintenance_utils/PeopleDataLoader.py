'''
Created on 07-Jun-2016

@author: prakash.selvam
'''
from XLSReader import xlsreader
from Maintenance.models import PreRegistrations

class PeopleDataLoader(object):
    '''
    '''
    def __init__(self):
        '''
        '''
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
            PreRegistrations.objects.create(
                    first_name = row['Firstname'],
                    last_name = row['Lastnme'],
                    block_name = row['Block'],
                    flat_number = row['FlatNumber'],
                    mobile_number = row['MobileNumber'], 
                    email_id = row['EmailID'],
                    type_occupancy = row['TypeofOccupancy'],
                    apartment_id = apartmentid)
                                