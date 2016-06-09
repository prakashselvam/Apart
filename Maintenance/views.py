from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.generic import View

import json
import urllib2

import config
import utils
import log_rotator
from Maintenance_utils.PeopleDataLoader import PeopleDataLoader
from Maintenance_utils.ApartmentAccountUtils import ApartmentAccountClass
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
            
            apartmentAccountObj = ApartmentAccountClass()
            result = apartmentAccountObj.createAccount(AppartmentName,AppartmentEmail,AppartmentAddress,NoOfBlocks,
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