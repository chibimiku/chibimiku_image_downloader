#!/usr/bin/python3

import time,os,sys

def log(my_text, log_level = 1, module_name = ''):
    try:
        content = str(my_text)
        log_level_dict = ["DEBUG", "INFO", "TRACE", "WARNING", "ERROR", "CRITICAL"]
        if(log_level > 5 or log_level < 0):
            log_level = 1
        currtime = time.strftime('%Y%m%d %H:%M:%S', time.localtime(time.time()))
        outstr = "[" + log_level_dict[log_level] + "]" + "[" + str(currtime) + "] " + content
        print (outstr)
        if(log_level == 5):
            print ("CRITICAL error occured. exit...")
            os._exit(1)
        return True
    except Exception as e:
        print ("Unexpected error.")
        print (e)