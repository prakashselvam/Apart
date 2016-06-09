'''
Created on 09-Jun-2016

@author: prakash.selvam
'''
import hashlib

from Maintenance.models import ApartmentAccount
from Maintenance import log_rotator

class ApartmentAccountClass(object):
    '''
    '''
    def __init__(self):
        '''
        '''
        self.UtilLogger = log_rotator.baseutil_logger()
        pass
    def createAccount(self,AppartmentName,AppartmentEmail,AppartmentAddress,NoOfBlocks,
                      NumberOfFlats,EmailAddress,MobileNumber,LandLine,Password):
        try:
            hash_object = hashlib.sha1(Password)
            PasswordHash = hash_object.hexdigest()
            resultSet = ApartmentAccount.objects.filter(AppartmentEmail = AppartmentEmail)
            if (resultSet.count()<=0):
                ApartmentAccount.objects.create(AppartmentName = AppartmentName,AppartmentEmail = AppartmentEmail,AppartmentAddress = AppartmentAddress,
                                            NoOfBlocks = NoOfBlocks,NumberOfFlats = NumberOfFlats,EmailAddress = EmailAddress,
                                            MobileNumber = MobileNumber,LandLine = LandLine,PasswordHash=PasswordHash)
                result = {'status': 'success', 'msg':'Account successfully ceated'}
            else:
                result = {'status': 'duplicate', 'msg':'Apartment email already exists try forgot password'}
        except:
            raise
        return result