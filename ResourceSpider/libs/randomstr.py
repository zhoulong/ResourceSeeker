#coding:utf8

from random import Random

def random_str(length):
    randomStr = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    charsLength = len(chars) - 1
    random = Random()
    for i in range(length):
        randomStr += chars[random.randint(0, charsLength)]
    return randomStr
