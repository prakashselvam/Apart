# -*- coding: utf-8 -*-
"""
Created on Jan 19, 2015

@author: elavarasan.m

Log rotator for Mobile App.
"""

import os
import logging
import datetime
import config

#Remember - When ever u create a logger object, default should be [None].
_errorLogger = [None]
_viewsLogger = [None]
_baseutilLogger = [None]

PATH_LOGS = os.path.dirname(os.path.abspath(__file__))+'/../../logs/'


def getLogger(logger_name,fName,levelname,disable_formatting=False):
    """
       Method to generate log file with today's date in file name.
    """
    logger = logging.getLogger(logger_name)
    curr_date = datetime.datetime.now()
    date_now = "%02d%02d%d" %(curr_date.day, curr_date.month, curr_date.year)
    handle = logging.FileHandler(fName+"_"+date_now+".log")
    if not disable_formatting:
        formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
        handle.setFormatter(formatter)
    logger.addHandler(handle)
    logger.setLevel(levelname)
    return logger

def gen_logger(logger_name, fName, logger_obj, disable_formatting=False):
    """
    Method to create log file with today's date in file name.
    """
    if not isinstance(logger_obj, list):
        logger_obj = [logger_obj]
    if logger_obj[0]:
        handlers = logger_obj[0].handlers
        if handlers and isinstance(handlers, (list, tuple)):
            handler = handlers[-1]
        else:
            handler = handlers
        if datetime.datetime.today().strftime("%d%m%Y") in handler.baseFilename:
            return logger_obj[0]
        else:
            #Remove the handlers from  logger object.
            logger_obj[0].handlers  = []

    logger_obj[0] = getLogger(logger_name, fName, logging.DEBUG, disable_formatting)
    #Log the current datetime in the created log file. This always logs at the starting of the log file.
    #logger_obj[0].info("Logger rotating time: %s, FileName: %s"%(datetime.datetime.now(), fName))
    return logger_obj[0]

def error_logger():
    global _errorLogger
    fPath = os.path.join(PATH_LOGS, config.ERROR_LOGGER)
    return gen_logger("ErrorLogger", fPath, _errorLogger)

def views_logger():
    global _viewsLogger
    fPath = os.path.join(PATH_LOGS, config.VIEW_LOGGER)
    return gen_logger("ViewsLogger", fPath, _viewsLogger)

def baseutil_logger():
    global _baseutilLogger
    fPath = os.path.join(PATH_LOGS, config.Baseutil_Logger)
    return gen_logger("BaseutilLogger", fPath, _baseutilLogger)