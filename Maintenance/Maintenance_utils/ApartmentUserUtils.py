'''
Created on 11-Jun-2016

@author: prakash.selvam
'''
import hashlib
import random

from Maintenance.models import RegisteredApartUser, UnmatchedRegistrations, PreRegistrations

class ApartUserUtil(object):
    def registerUserAccount(self,first_name,last_name, block_name, flat_number,mobile_number,
                            email_id,type_occupancy, have_car, apartment_id, password):
        try:
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