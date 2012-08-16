#coding:utf8
'''
Created on 2012-8-14

@author: zhoulong0116
'''
from common import define

from bitarray import bitarray
import hashlib
import pickle
import os

bitarr = None
FILE_PATH = define.CACHE_PATH + 'bloom_array.cache'

def _hash_func(url):
    m = hashlib.md5()
    m.update(url)
    md5_str = m.hexdigest()
    index_array = []
    index_array.append(int(md5_str[0 : 8], 16))
    index_array.append(int(md5_str[8 : 15], 16))
    index_array.append(int(md5_str[15 : 21], 16))
    index_array.append(int(md5_str[21 : 26], 16))
    index_array.append(int(md5_str[26 : 30], 16))
    index_array.append(int(md5_str[30:] + md5_str[0], 16))
    index_array.append(int(md5_str[1 : 3], 16))
    index_array.append(int(md5_str[3], 16))
    if index_array[0] > 2 ** 31:
        index_array[0] = int(md5_str[0 : 7], 16)
    return index_array

def init_bitarray():
    global bitarr
    if bitarr == None:
        if os.path.exists(FILE_PATH):
            bit_file = open(FILE_PATH, 'rb')
            bitarr = pickle.load(bit_file)
            bit_file.close()
        else:
            bitarr = bitarray(2 ** 31)
        print len(bitarr)

def save_bitarray():
    global bitarr
    if bitarr != None:
        bit_file = open(FILE_PATH, 'wb')
        pickle.dump(bitarr, bit_file, pickle.HIGHEST_PROTOCOL)
        bit_file.close()
        
def _switchon_bitarray(index_array):
    global bitarr
    if bitarr == None:
        return
    for index in index_array:
        bitarr[index] = True
        
def url_exist(url):
    global bitarr
    index_array = _hash_func(url)
    print index_array
    if bitarr != None:
        for index in index_array:
            if bitarr[index] == False:
                _switchon_bitarray(index_array)
                return False
        return True
    else:
        return False

