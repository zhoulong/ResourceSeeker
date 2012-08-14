#coding:utf8
'''
Created on 2012-8-10

@author: zhoulong0116
'''
from common import define

from BeautifulSoup import BeautifulSoup

def analyse_url(html):
    soup = BeautifulSoup(html)
    #_analyse_js(soup)
    return _analyse_hyperlink(soup)
    
def _analyse_js(soup):
    return None

def _analyse_hyperlink(soup):
    url_list = []
    link_list = soup.findAll('a')
    for link in link_list:
        if link.has_key('href'):
            url_list.append(link['href'])
    return url_list

def analyse_text(html):
    key_list = []
    for key_word in define.KEY_WORDS:
        if html.find(key_word):
            key_list.append(key_word)
    return key_list
    


