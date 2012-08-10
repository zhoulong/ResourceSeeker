#coding:utf8
'''
Created on 2012-8-10

@author: zhoulong0116
'''
from model import record
from logic import data_logic as _logic
from common import define


import os
import threading
import time

class Analyzer(threading.Thread):
    
    def __init__(self, index):
        threading.Thread.__init__(self)
        self.index = index
        self.table = '%s_%s' % (record.DB_TABLE, index)
        
    def run(self):
        while True:
            record_obj = _logic.get_record_with_status(self.table, record.STATUS_REQUEST)
            if record_obj == None:
                time.sleep(60)
                continue
            if os.path.exists(define.HTML_PATH + record_obj.store_path):
                file_obj = open(define.HTML_PATH + record_obj.store_path, 'r')
                html = file_obj.read()
                self.analyse(html)
                file_obj.close()
                
    def analyse(self, html):
        pass
    
    
    
