#coding:utf8
'''
Created on 2012-8-10

@author: zhoulong0116
'''

from libs.sqlpool import pool as _pool

STATUS_INVALID, STATUS_NOTYET, STATUS_REQUEST, STATUS_ANALYSE = range(4)

class Record:
    
    def __init__(self, record_id, record_url, status, store_path, extra):
        self.record_id = record_id
        self.record_url = record_url
        self.status = status
        self.store_path = store_path
        self.extra = extra
        
DB_TABLE = 'record'
KEY_RECORD_ID = 'record_id'
KEY_RECORD_URL = 'record_url'
KEY_STATUS = 'status'
KEY_STORE_PATH = 'store_path'
KEY_EXTRA = 'extra_info'

def insert(table, record):
    sql = '''INSERT INTO %s(%s, %s, %s, %s) 
             VALUES('%s', %s, '%s', '%s');''' % (table, 
            KEY_RECORD_URL, KEY_STATUS, KEY_STORE_PATH, KEY_EXTRA,
            record.record_url, record.status, record.store_path, record.extra)
    return _pool.execute(sql)

def update(table, record):
    sql = '''UPDATE %s SET %s='%s', %s=%s, %s='%s', %s='%s' WHERE %s=%s;''' % (
            table, KEY_RECORD_URL, record.record_url, KEY_STATUS, record.status,
            KEY_STORE_PATH, record.store_path, KEY_EXTRA, record.extra, 
            KEY_RECORD_ID, record.record_id)
    return _pool.execute(sql)

def delete(table, where_clause = ''):
    sql = '''DELETE FROM %s %s;''' % (table, where_clause)
    return _pool.execute(sql)

def query(table, where_clause = '', order_clause = '', limit_clause = ''):
    sql = '''SELECT %s, %s, %s, %s, %s FROM %s %s %s %s;''' % (KEY_RECORD_ID,
            KEY_RECORD_URL, KEY_STATUS, KEY_STORE_PATH, KEY_EXTRA,
            table, where_clause, order_clause, limit_clause)
    return _pool.query(sql, 1)

def generate(data_dict):
    return Record(data_dict[KEY_RECORD_ID], data_dict[KEY_RECORD_URL],
                 data_dict[KEY_STATUS], data_dict[KEY_STORE_PATH], data_dict[KEY_EXTRA])
