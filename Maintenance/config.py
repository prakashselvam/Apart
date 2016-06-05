'''
Created on 05-Jun-2016

@author: prakash.selvam
'''
INVALID_REQUEST_RESPONSE = {'status': 'error', 'msg': 'invalid Request object'}
UNKNOWN_ERROR_RESPONSE = {'status': 'error', 'msg': 'Something went wrong try again later'}
INVALID_CREDENTIALS_RESPONSE = {'status': 'error', 'msg': 'That email ID and password combination did not work. Double check your email and password.'}
INVALID_REQUEST_METHOD_RESPONSE = {'status': 'error', 'msg': 'Invalid Request method'}
MANDATORY_DATA_MISSING_RESPONSE = {'status': 'error', 'msg': 'Mandatory post data missing'}



ERROR_LOGGER = "Error"
VIEW_LOGGER = "Views"
Baseutil_Logger = "BaseUtil"