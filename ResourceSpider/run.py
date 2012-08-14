#coding:utf8
'''
Created on 2012-8-14

@author: zhoulong0116
'''
from analyse import analyzer
from crawl import crawler
from logic import data_logic as _logic
from model import record

import os
import sys


THREAD_COUNT = 5

def initialize():
    for i in range(0, 5):
        _logic.create_record_table('%s_%s' % (record.DB_TABLE, i))

def run_crawler():
    for i in range(0, 5):
        thread = crawler.Crawler(i)
        thread.start()

def run_analyzer():
    for i in range(0, 5):
        thread = analyzer.Analyzer(i)
        thread.start()

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
    else:
        print '参数错误'
