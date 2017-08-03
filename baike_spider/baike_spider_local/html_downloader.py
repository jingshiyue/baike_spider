#coding=utf-8
'''
Created on 2017��7��31��
@summary: 
@author: Mir-Z
'''
import urllib.request
import logging
logging.basicConfig(level = logging.DEBUG,
                    format = '%(asctime)s: %(filename)s[line:%(lineno)d] %(levelname)s      %(message)s')
class HtmlDownloader(object):

    
    def dowload(self,url):
        if url is None:
            return None
        
        response = urllib.request.urlopen(url)
        
        if response.getcode() != 200: #200表示成功应答
            return None
        
        return response.read()
    



