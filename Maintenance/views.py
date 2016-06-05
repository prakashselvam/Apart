from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.generic import View

import json
import urllib2

import config
import utils
import log_rotator
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
            result = {'status':'success'}
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