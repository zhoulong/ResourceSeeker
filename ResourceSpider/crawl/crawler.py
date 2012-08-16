#coding:utf8
'''
Created on 2012-8-10

@author: zhoulong0116
'''
from model import record
from libs import net
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
        self.execute = True
        
    def run(self):
        while self.execute:
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
                content = None
                try:
                    response = net.get(record_obj.record_url)
                    content = response.read()
                    response.close()
                except Exception:
                    continue
                current_time = '%s' % time.time()
                folder_path = '%s/%s/' % (current_time[0 : 6], current_time[6 : 9])
                if not os.path.exists(define.HTML_PATH + folder_path):
                    os.makedirs(define.HTML_PATH + folder_path)
                file_path = folder_path + randomstr.random_str(32)
                while os.path.exists(define.HTML_PATH + file_path):
                    file_path = folder_path + randomstr.random_str(32)
                file_obj = open(define.HTML_PATH + file_path, 'w')
                file_obj.write(content)
                file_obj.close()
                record_obj.store_path = file_path
                record_obj.status = record.STATUS_REQUEST
                _logic.update_record(self.table, record_obj)
                self.url_dict[url] = time.time()
            
    def stop_task(self):
        self.execute = False
