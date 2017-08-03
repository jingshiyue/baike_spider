'''
#coding=utf-8
Created on 2017��7��31��

@author: Mir-Z
'''
import logging
logging.basicConfig(level = logging.DEBUG,
                    format = '%(asctime)s: %(filename)s[line:%(lineno)d] %(levelname)s      %(message)s')

class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
        
    
    def add_new_url(self,url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
            
    def add_new_urls(self,urls):
        #批量添加url
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)
        
    def has_new_url(self):
        # 返回布尔值
        return len(self.new_urls) != 0
    
    def get_new_url(self):
        # 从新url列表中移除一个到旧的url列表
        new_url = self.new_urls.pop() #pop方法，从列表中移除一个
        self.old_urls.add(new_url)
#        logging.debug(new_url)
#        logging.debug(self.old_urls)
        return new_url
    

    
    
    
    
    
    
    



