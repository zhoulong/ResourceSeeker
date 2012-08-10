#coding:utf8
'''
Created on 2012-8-10

@author: zhoulong0116
'''
from model import record
from libs import net
from libs.sqlpool import pool as _pool
from libs import randomstr
from logic import data_logic as _logic
from common import define

import os
import threading
import time
from urlparse import urlparse

class Crawler(threading.Thread):
    
    def __init__(self, index):
        threading.Thread.__init__(self)
        self.index = index
        self.table = '%s_%s' % (record.DB_TABLE, index)
        self.url_dict = {} #已请求过的url
        
    def run(self):
        while True:
            record_obj = _logic.get_record_with_status(self.table, record.STATUS_NOTYET)
            if record_obj == None:
                time.sleep(60)
                continue
            parse_result = urlparse(record_obj.record_url)
            if parse_result.netloc == '':
                sub_end = parse_result.path.find('/')
                if sub_end == -1:
                    url = parse_result.path
                else:
                    url = parse_result.path[0 : sub_end]
            else:
                url = parse_result.netloc
            if not self.url_dict.has_key(url) or time.time() - self.url_dict[url] > 5:
                response = net.get(record_obj.record_url)
                file_path = randomstr.random_str(32)
                while os.path.exists(define.HTML_PATH + file_path):
                    file_path = randomstr.random_str(32)
                file_obj = open(define.HTML_PATH + file_path, 'w')
                file_obj.write(response.read())
                response.close()
                file_obj.close()
                record_obj.store_path = file_path
                record_obj.status = record.STATUS_REQUEST
                _logic.update_record(self.table, record_obj)
                self.url_dict[url] = time.time()
            
