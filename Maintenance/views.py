from django.http import HttpResponse
from django.views.generic import View

import json
import urllib2

import config
import utils
import log_rotator
from Maintenance_utils.PeopleDataLoader import PeopleDataLoader
from Maintenance_utils.ApartmentAccountUtils import ApartmentAccountClass
from Maintenance_utils.ApartmentUserUtils import ApartUserUtil
# Create your views here.


def test(request):
    """
    @summary: View method to check the server status.
    @param request: HttpRequest.
    @rtype: HttpResponse
    @return: HttpResponse containing server status.
    """
    result = {'status': 'It works'}
    return HttpResponse(json.dumps(result, default=utils.json_default), content_type="application/json")
                
class LoadPeopleFile(View):
    def get(self,request,url):
        result = config.INVALID_REQUEST_METHOD_RESPONSE
        return HttpResponse(json.dumps(result, default=utils.json_default), content_type="application/json")
    def post(self,request,url):
        """
        @summary: View method to handle file load requests.
        @param request: file path
        @rtype: HttpResponse
        @return: HttpResponse containing load file status.
        """
        viewslogger = log_rotator.views_logger()
        result = {}
        try:
            apartmentid = request.POST.get('apartmentid')
            file_name = request.POST.get('file_name')
            SheetNo = request.POST.get('SheetNo')
            peopleDataLoader = PeopleDataLoader()
            result = peopleDataLoader.read_people_data(apartmentid, file_name, SheetNo)
        except urllib2.HTTPError, err:
            error_logger = log_rotator.error_logger()
            error_logger.debug("Exception::", exc_info=True)
            if err.code == 401:
                result = config.INVALID_CREDENTIALS_RESPONSE
            else:
                result = config.UNKNOWN_ERROR_RESPONSE
        except KeyError:
            error_logger = log_rotator.error_logger()
            error_logger.debug("Exception::", exc_info=True)
            result = config.MANDATORY_DATA_MISSING_RESPONSE
        except:
            error_logger = log_rotator.error_logger()
            error_logger.debug("Exception::", exc_info=True)
            result = config.UNKNOWN_ERROR_RESPONSE
        viewslogger.debug("Response : %s" % result)
        return HttpResponse(json.dumps(result, default=utils.json_default), content_type="application/json")
    
class CreateApartmentAccount(View):
    def get(self,request,url):
        result = config.INVALID_REQUEST_METHOD_RESPONSE
        return HttpResponse(json.dumps(result, default=utils.json_default), content_type="application/json")
    def post(self,request,url):
        """
        @summary: View method to handle file load requests.
        @param request: file path
        @rtype: HttpResponse
        @return: HttpResponse containing load file status.
        """
        viewslogger = log_rotator.views_logger()
        result = {}
        try:
            AppartmentName = request.POST.get('AppartmentName')
            AppartmentEmail = request.POST.get('AppartmentEmail')
            AppartmentAddress = request.POST.get('AppartmentAddress')
            NoOfBlocks = request.POST.get('NoOfBlocks')
            NumberOfFlats = request.POST.get('NumberOfFlats')
            EmailAddress = request.POST.get('EmailAddress')
            MobileNumber = request.POST.get('MobileNumber')
            LandLine = request.POST.get('LandLine')
            Password = request.POST.get('Password')
            apartmentUserObj = ApartUserUtil()
            result = apartmentUserObj.createAccount(AppartmentName,AppartmentEmail,AppartmentAddress,NoOfBlocks,
                                                       NumberOfFlats,EmailAddress,MobileNumber,LandLine,Password)
        except urllib2.HTTPError, err:
            error_logger = log_rotator.error_logger()
            error_logger.debug("Exception::", exc_info=True)
            if err.code == 401:
                result = config.INVALID_CREDENTIALS_RESPONSE
            else:
                result = config.UNKNOWN_ERROR_RESPONSE
        except KeyError:
            error_logger = log_rotator.error_logger()
            error_logger.debug("Exception::", exc_info=True)
            result = config.MANDATORY_DATA_MISSING_RESPONSE
        except:
            error_logger = log_rotator.error_logger()
            error_logger.debug("Exception::", exc_info=True)
            result = config.UNKNOWN_ERROR_RESPONSE
        viewslogger.debug("Response : %s" % result)
        return HttpResponse(json.dumps(result, default=utils.json_default), content_type="application/json")

class UpdateApartmentAccount(View):
    def get(self,request,url):
        result = config.INVALID_REQUEST_METHOD_RESPONSE
        return HttpResponse(json.dumps(result, default=utils.json_default), content_type="application/json")
    def post(self,request,url):
        """
        @summary: View method to handle file load requests.
        @param request: file path
        @rtype: HttpResponse
        @return: HttpResponse containing load file status.
        """
        viewslogger = log_rotator.views_logger()
        result = {}
        try:
            AppartmentEmail = request.POST.get('AppartmentEmail')
            AccountHolderName = request.POST.get('AccountHolderName')
            AccountNumber = request.POST.get('AccountNumber')
            IFSCCode = request.POST.get('IFSCCode')
            apartmentAccountObj = ApartmentAccountClass()
            result = apartmentAccountObj.UpdateBankDetails(AppartmentEmail,AccountHolderName, AccountNumber, IFSCCode)
        except urllib2.HTTPError, err:
            error_logger = log_rotator.error_logger()
            error_logger.debug("Exception::", exc_info=True)
            if err.code == 401:
                result = config.INVALID_CREDENTIALS_RESPONSE
            else:
                result = config.UNKNOWN_ERROR_RESPONSE
        except KeyError:
            error_logger = log_rotator.error_logger()
            error_logger.debug("Exception::", exc_info=True)
            result = config.MANDATORY_DATA_MISSING_RESPONSE
        except:
            error_logger = log_rotator.error_logger()
            error_logger.debug("Exception::", exc_info=True)
            result = config.UNKNOWN_ERROR_RESPONSE
        viewslogger.debug("Response : %s" % result)
        return HttpResponse(json.dumps(result, default=utils.json_default), content_type="application/json")
    
class RegisterUserAccount(View):
    def get(self,request,url):
        result = config.INVALID_REQUEST_METHOD_RESPONSE
        return HttpResponse(json.dumps(result, default=utils.json_default), content_type="application/json")
    def post(self,request,url):
        """
        @summary: View method to handle file load requests.
        @param request: file path
        @rtype: HttpResponse
        @return: HttpResponse containing load file status.
        """
        viewslogger = log_rotator.views_logger()
        result = {}
        try:
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            block_name = request.POST.get('block_name')
            flat_number = request.POST.get('flat_number')
            mobile_number = request.POST.get('mobile_number')
            email_id = request.POST.get('email_id')
            type_occupancy = request.POST.get('type_occupancy')
            have_car = request.POST.get('have_car')
            apartment_id = request.POST.get('apartment_id')
            password = request.POST.get('password')
            apartmentUserObj = ApartUserUtil()
            result = apartmentUserObj.registerUserAccount(first_name, last_name, block_name, flat_number, 
                                                          mobile_number, email_id, type_occupancy, have_car, 
                                                          apartment_id, password)
        except urllib2.HTTPError, err:
            error_logger = log_rotator.error_logger()
            error_logger.debug("Exception::", exc_info=True)
            if err.code == 401:
                result = config.INVALID_CREDENTIALS_RESPONSE
            else:
                result = config.UNKNOWN_ERROR_RESPONSE
        except KeyError:
            error_logger = log_rotator.error_logger()
            error_logger.debug("Exception::", exc_info=True)
            result = config.MANDATORY_DATA_MISSING_RESPONSE
        except:
            error_logger = log_rotator.error_logger()
            error_logger.debug("Exception::", exc_info=True)
            result = config.UNKNOWN_ERROR_RESPONSE
        viewslogger.debug("Response : %s" % result)
        return HttpResponse(json.dumps(result, default=utils.json_default), content_type="application/json")
    
class UnmatchedRegistrations(View):
    def get(self,request,url):
        result = config.INVALID_REQUEST_METHOD_RESPONSE
        return HttpResponse(json.dumps(result, default=utils.json_default), content_type="application/json")
    def post(self,request,url):
        """
        @summary: View method to handle file load requests.
        @param request: file path
        @rtype: HttpResponse
        @return: HttpResponse containing load file status.
        """
        viewslogger = log_rotator.views_logger()
        result = {}
        try:
            block_name = request.POST.get('block_name')
            flat_number = request.POST.get('flat_number')
            apartment_id = request.POST.get('apartment_id')
            type_occupancy = request.POST.get('type_occupancy')
            apartmentUserObj = ApartUserUtil()
            result['unmatch'] = apartmentUserObj.getunmatchreg(block_name, flat_number, apartment_id,type_occupancy)
            result['prereg'] = apartmentUserObj.getpreregistrations(block_name, flat_number, apartment_id, type_occupancy)
        except urllib2.HTTPError, err:
            error_logger = log_rotator.error_logger()
            error_logger.debug("Exception::", exc_info=True)
            if err.code == 401:
                result = config.INVALID_CREDENTIALS_RESPONSE
            else:
                result = config.UNKNOWN_ERROR_RESPONSE
        except KeyError:
            error_logger = log_rotator.error_logger()
            error_logger.debug("Exception::", exc_info=True)
            result = config.MANDATORY_DATA_MISSING_RESPONSE
        except:
            error_logger = log_rotator.error_logger()
            error_logger.debug("Exception::", exc_info=True)
            result = config.UNKNOWN_ERROR_RESPONSE
        viewslogger.debug("Response : %s" % result)
        return HttpResponse(json.dumps(result, default=utils.json_default), content_type="application/json")
    
class UpdatePreRegUser(View):
    def get(self,request,url):
        result = config.INVALID_REQUEST_METHOD_RESPONSE
        return HttpResponse(json.dumps(result, default=utils.json_default), content_type="application/json")
    def post(self,request,url):
        """
        @summary: View method to handle file load requests.
        @param request: file path
        @rtype: HttpResponse
        @return: HttpResponse containing load file status.
        """
        viewslogger = log_rotator.views_logger()
        result = {}
        try:
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            block_name = request.POST.get('block_name')
            flat_number = request.POST.get('flat_number')
            mobile_number = request.POST.get('mobile_number')
            email_id = request.POST.get('email_id')
            type_occupancy = request.POST.get('type_occupancy')
            apartment_id = request.POST.get('apartment_id')
            apartmentUserObj = ApartUserUtil()
            result = apartmentUserObj.updatePreRegUser(first_name, last_name, block_name, flat_number, 
                                                       mobile_number, email_id, type_occupancy, apartment_id)
        except urllib2.HTTPError, err:
            error_logger = log_rotator.error_logger()
            error_logger.debug("Exception::", exc_info=True)
            if err.code == 401:
                result = config.INVALID_CREDENTIALS_RESPONSE
            else:
                result = config.UNKNOWN_ERROR_RESPONSE
        except KeyError:
            error_logger = log_rotator.error_logger()
            error_logger.debug("Exception::", exc_info=True)
            result = config.MANDATORY_DATA_MISSING_RESPONSE
        except:
            error_logger = log_rotator.error_logger()
            error_logger.debug("Exception::", exc_info=True)
            result = config.UNKNOWN_ERROR_RESPONSE
        viewslogger.debug("Response : %s" % result)
        return HttpResponse(json.dumps(result, default=utils.json_default), content_type="application/json")
    
class VerifyOTP(View):
    def get(self,request,url):
        result = config.INVALID_REQUEST_METHOD_RESPONSE
        return HttpResponse(json.dumps(result, default=utils.json_default), content_type="application/json")
    def post(self,request,url):
        """
        @summary: View method to handle file load requests.
        @param request: file path
        @rtype: HttpResponse
        @return: HttpResponse containing load file status.
        """
        viewslogger = log_rotator.views_logger()
        result = {}
        try:
            mobile_number = request.POST.get('mobile_number')
            apartment_id = request.POST.get('apartment_id')
            otp = request.POST.get('otp')
            apartmentUserObj = ApartUserUtil()
            result = apartmentUserObj.verifyOTP(apartment_id, mobile_number, otp)
        except urllib2.HTTPError, err:
            error_logger = log_rotator.error_logger()
            error_logger.debug("Exception::", exc_info=True)
            if err.code == 401:
                result = config.INVALID_CREDENTIALS_RESPONSE
            else:
                result = config.UNKNOWN_ERROR_RESPONSE
        except KeyError:
            error_logger = log_rotator.error_logger()
            error_logger.debug("Exception::", exc_info=True)
            result = config.MANDATORY_DATA_MISSING_RESPONSE
        except:
            error_logger = log_rotator.error_logger()
            error_logger.debug("Exception::", exc_info=True)
            result = config.UNKNOWN_ERROR_RESPONSE
        viewslogger.debug("Response : %s" % result)
        return HttpResponse(json.dumps(result, default=utils.json_default), content_type="application/json")