#coding:utf8
'''
Created on 2012-8-14

@author: zhoulong0116
'''
from analyse import analyzer
from crawl import crawler
from logic import data_logic as _logic
from model import record
from analyse import bloom_fliter
from common import urls
from common import define

import os
import sys
import socket 

THREAD_COUNT = 5
crawler_thread = []
analyzer_thread = []

def initialize():
    if not os.path.exists(define.STORAGE_PATH):
        os.mkdir(define.STORAGE_PATH)
    if not os.path.exists(define.HTML_PATH):
        os.mkdir(define.HTML_PATH)
    if not os.path.exists(define.CACHE_PATH):
        os.mkdir(define.CACHE_PATH)
    for i in range(0, 5):
        _logic.create_record_table('%s_%s' % (record.DB_TABLE, i))
    bloom_fliter.init_bitarray()
    index = 0
    for url in urls.init_url_list:
        if not bloom_fliter.url_exist(url):
            record_obj = record.Record(define.UNDEFINE, url, record.STATUS_NOTYET, '', '')
            table = '%s_%s' % (record.DB_TABLE, index % THREAD_COUNT)
            _logic.insert_record(table, record_obj)
        index = index + 1
    bloom_fliter.save_bitarray()

def run_crawler():
    global crawler_thread
    for i in range(0, 5):
        thread = crawler.Crawler(i)
        crawler_thread.append(thread)
        thread.start()

def run_analyzer():
    global analyzer_thread
    for i in range(0, 5):
        thread = analyzer.Analyzer(i)
        analyzer_thread.append(thread)
        thread.start()
        
def stop_crawler():
    global crawler_thread
    for thread in crawler_thread:
        thread.stop_task()

def stop_analyzer():
    global analyzer_thread
    for thread in analyzer_thread:
        thread.stop_task()
  
def run_listener():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    sock.bind(('localhost', 8002))  
    sock.listen(5)  
    while True:  
        connection, address = sock.accept()  
        try:  
            connection.settimeout(5)  
            buf = connection.recv(1024)  
            if buf == 'stop': 
                print '正在停止...'
                stop_crawler() 
                stop_analyzer()
                bloom_fliter.save_bitarray()
                print '已经成功保存数据'
                connection.close()
                break
        except socket.timeout:  
            print 'time out'  
        connection.close()

def client_send_msg(msg):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    sock.connect(('localhost', 8002))  
    sock.send(msg)  
    sock.close()  

if __name__ == '__main__':
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    argv = sys.argv
    if len(argv) <= 1:
        print '缺少启动参数，init 初始化, start 启动服务'
    elif argv[1] == 'init':
        print '正在初始化...'
        initialize()
        print '初始化完成'
    elif argv[1] == 'start':
        print '正在启动...'
        run_crawler()
        run_analyzer()
        run_listener()
    elif argv[1] == 'stop':
        client_send_msg('stop')
    else:
        print '参数错误'
    print '程序退出'
