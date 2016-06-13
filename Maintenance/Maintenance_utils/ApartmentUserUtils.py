'''
Created on 11-Jun-2016

@author: prakash.selvam
'''
import hashlib
import random

from Maintenance.models import RegisteredApartUser, UnmatchedRegistrations, PreRegistrations

class ApartUserUtil(object):
    
    def model_to_dict(self, instance, include=None, exclude=None):
        fields = instance._meta.concrete_fields
        if include is not None:
            return {f.attname: getattr(instance, f.attname) for f in fields if f.name in include.split(',')}
        if exclude is not None:
            return {f.attname: getattr(instance, f.attname) for f in fields if f.name not in exclude.split(',')}
        return {f.attname: getattr(instance, f.attname) for f in fields}
    
    def verifyOTP(self, apartment_id, mobile_number, otp):
        try:
            otp_hash_object = hashlib.sha1(otp)
            otp_hash = otp_hash_object.hexdigest()
            regResultSet = RegisteredApartUser.objects.filter(mobile_number = mobile_number, apartment_id = apartment_id,
                                                              otp_hash = otp_hash)
            if regResultSet.count()>0:
                regResultSet.update(verified_mobile = True,
                                    otp_hash = '')
                result = {'status': 'success', 'msg':'mobile number successfully verified'}
                return result
            else:
                result = {'status': 'failure', 'msg':'wrong otp'}
        except:
            raise
        return result
    def registerUserAccount(self,first_name,last_name, block_name, flat_number,mobile_number,
                            email_id,type_occupancy, have_car, apartment_id, password):
        try:
            type_occupancy = 1 if type_occupancy.lower() == 'owner' else 0
            password_hash_object = hashlib.sha1(password)
            passwordHash = password_hash_object.hexdigest()
            resultSet = PreRegistrations.objects.filter(block_name = block_name, flat_number = flat_number, 
                                                        mobile_number = mobile_number, apartment_id = apartment_id)
            regResultSet = RegisteredApartUser.objects.filter(block_name = block_name, flat_number = flat_number, 
                                                        mobile_number = mobile_number, apartment_id = apartment_id)
            if regResultSet.count()>0:
                result = {'status': 'failure', 'msg':'Account already registered try to login or reset password'}
                return result
            if (resultSet.count()>0):
                otp = str(random.randrange(1111, 9999))
                otp_hash_object = hashlib.sha1(otp)
                otp_hash = otp_hash_object.hexdigest()
                RegisteredApartUser.objects.create(first_name = first_name,
                                            last_name = last_name,
                                            block_name = block_name,
                                            flat_number = flat_number,
                                            mobile_number = mobile_number,
                                            email_id = email_id,
                                            type_occupancy = type_occupancy,
                                            have_car = have_car,
                                            apartment_id = apartment_id,
                                            passwordHash = passwordHash,
                                            otp_hash = otp_hash,
                                            verified_mobile = False)
                result = {'status': 'success', 'msg':'Account successfully ceated', 'otp': otp}
            else:
                unregResultset = UnmatchedRegistrations.objects.filter(mobile_number = mobile_number)
                if unregResultset.count()>0:
                    unregResultset.update(first_name = first_name,
                                            last_name = last_name,
                                            block_name = block_name,
                                            flat_number = flat_number,
                                            mobile_number = mobile_number,
                                            email_id = email_id,
                                            type_occupancy = type_occupancy,
                                            have_car = have_car,
                                            apartment_id = apartment_id,
                                            passwordHash = passwordHash)
                else:
                    UnmatchedRegistrations.objects.create(first_name = first_name,
                                            last_name = last_name,
                                            block_name = block_name,
                                            flat_number = flat_number,
                                            mobile_number = mobile_number,
                                            email_id = email_id,
                                            type_occupancy = type_occupancy,
                                            have_car = have_car,
                                            apartment_id = apartment_id,
                                            passwordHash = passwordHash)
                result = {'status': 'notmatched', 'msg':'mobile number not in database. Contact your apartment admin'}
        except:
            raise
        return result
    
    def getpreregistrations(self, block_name, flat_number, apartment_id, type_occupancy):
        try:
            type_occupancy = 1 if type_occupancy.lower() == 'owner' else 0
            unregResultset = PreRegistrations.objects.filter(block_name=block_name, flat_number=flat_number, apartment_id=apartment_id,type_occupancy=type_occupancy)
            if unregResultset.count()>0:
                result = self.model_to_dict(unregResultset[0],None,'passwordHash,have_car')
            else:
                result = {'status': 'notmatched', 'msg':'registration details not in database.'}
        except:
            raise
        return result
    
    def getunmatchreg(self, block_name, flat_number, apartment_id, type_occupancy):
        try:
            type_occupancy = 1 if type_occupancy.lower() == 'owner' else 0
            unregResultset = UnmatchedRegistrations.objects.filter(block_name=block_name, flat_number=flat_number, apartment_id=apartment_id,type_occupancy=type_occupancy)
            if unregResultset.count()>0:
                result = self.model_to_dict(unregResultset[0],None,'passwordHash,have_car')
            else:
                result = {'status': 'notmatched', 'msg':'registration details not in database.'}
        except:
            raise
        return result
    
    def updatePreRegUser(self,first_name,last_name, block_name, flat_number,mobile_number,
                            email_id,type_occupancy, apartment_id):
        try:
            type_occupancy = 1 if type_occupancy.lower() == 'owner' else 0
            resultSet = PreRegistrations.objects.filter(block_name = block_name, flat_number = flat_number, 
                                                        apartment_id = apartment_id, type_occupancy = type_occupancy)
            if (resultSet.count()>0):
                resultSet.update(
                    first_name = first_name,
                    last_name = last_name,
                    mobile_number = mobile_number, 
                    email_id = email_id)
                result = {'status': 'success', 'msg':'registration details updated. ask customer to try registering again'}
            else:
                result = {'status': 'notmatched', 'msg':'registration details not in database.'}
        except:
            raise
        return result