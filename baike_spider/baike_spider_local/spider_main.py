#coding=utf-8
''' 
Created on 2017.7.31
@summary: 
@author: Mir-Z
'''
from baike_spider import url_manager, html_outpurter, html_downloader,\
    html_parser
import logging
logging.basicConfig(level = logging.DEBUG,
                    format = '%(asctime)s: %(filename)s[line:%(lineno)d] %(levelname)s      %(message)s')

class SpiderMain(object):
    def __init__(self):
        #初始化
        self.urls = url_manager.UrlManager()#url_manager是一个module，UrlManager是一个类。词句实例化一个类UrlManager并赋值给 urls
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outpurter.HtmlOutputer()
    
    
    def craw(self, root_url):
        #爬取页面的函数
        count =1
        self.urls.add_new_url(root_url) 
        logging.debug(self.urls)
        while self.urls.has_new_url():
            try:        #有些页面的url访问有问题或者不存在，所以加try
                new_url = self.urls.get_new_url()
            except:
                print ('1 failed')
#            try:
#                html_cont = self.downloader.dowload(new_url)#html_cont，html内容
#            except:
#                print ('2 failed')
            try:
                new_urls,new_data = self.parser.parser(new_url)
            except:
                print ('3 failed')    
            try:
                self.urls.add_new_urls(new_urls)
            except:
                print ('4 failed')
            try:
                self.outputer.collect_data(new_data)
                
                if count ==50:
                    print('count = 50')
                    break
                count = count + 1
                logging.debug(count)
            except:
                print ('craw failed')
            self.outputer.outputer_html()
        logging.info(count)
        
    
    


if __name__=="__main__":
    root_url = "https://baike.baidu.com/item/Python"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)