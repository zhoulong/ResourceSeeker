#coding:utf8
'''
Created on 2012-8-10

@author: zhoulong0116
'''
from model import record
from logic import data_logic as _logic
from common import define
from analyse import html_analyse

import os
import threading
import time
import re

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
                self.analyse(os.path.dirname(record_obj.record_url), html)
                record_obj.status = record.STATUS_ANALYSE
                _logic.update_record(self.table, record_obj)
                file_obj.close()
                
    def analyse(self, base_url, html):
        url_list = html_analyse.analyse_url(html)
        for url in url_list:
            record_url = None
            if re.search('^https?://[0-9a-zA-Z\\.&%/]+$', url) != None:
                record_url = url
            elif re.search('^/[0-9a-zA-Z\\.&%/]+$', url) != None:
                record_url = base_url + url
            elif re.search('^(\\./)*[0-9a-zA-Z\\.&%/]+$', url) != None:
                count = len(re.findall('(\\./)', url))
                parent_url = base_url
                for i in range(0, count):
                    parent_url = os.path.dirname(parent_url)
                record_url = parent_url + url[count * 2 :]
            if record_url != None:
                record_obj = record.Record(define.UNDEFINE, record_url, record.STATUS_NOTYET, '', '')
                _logic.insert_record(self.table, record_obj)
        
    
    
    
