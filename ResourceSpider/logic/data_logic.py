#coding:utf8
'''
Created on 2012-8-10

@author: zhoulong0116
'''

from model import record
from libs.sqlpool import pool as _pool

def create_record_table(table):
    create_sql = '''CREATE TABLE IF NOT EXISTS `%s` (
                      `%s` int(11) NOT NULL AUTO_INCREMENT,
                      `%s` varchar(255) NOT NULL,
                      `%s` int(11) NOT NULL,
                      `%s` varchar(255) NOT NULL,
                      `%s` varchar(255) NOT NULL,
                      PRIMARY KEY (`%s`)
                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;''' % \
                    (table, record.KEY_RECORD_ID, record.KEY_RECORD_URL,
                     record.KEY_STATUS, record.KEY_STORE_PATH, record.KEY_EXTRA, 
                     record.KEY_RECORD_ID)
    _pool.execute(create_sql)
    
def insert_record(table, obj):
    return record.insert(table, obj) == 1

def delete_record(table, obj):
    where_clause = '''WHERE %s=%s''' % (record.KEY_RECORD_ID, obj.record_id)
    return record.delete(table, where_clause) == 1

def update_record(table, obj):
    return record.update(table, obj) == 1

def get_record_with_id(table, record_id):
    where_clause = '''WHERE %s=%s''' % (record.KEY_RECORD_ID, record_id)
    limit_clause = '''LIMIT 1'''
    data = record.query(table, where_clause, limit_clause = limit_clause)
    if data == None or len(data) == 0:
        return None
    return record.generate(data)

def get_record_with_status(table, status):
    where_clause = '''WHERE %s=%s''' % (record.KEY_STATUS, status)
    order_clause = '''ORDER BY RAND()'''
    limit_clause = '''LIMIT 1'''
    data = record.query(table, where_clause, order_clause, limit_clause)
    if data == None or len(data) == 0:
        return None
    return record.generate(data)
    
