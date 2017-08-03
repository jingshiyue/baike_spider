#coding=utf-8
'''
Created on 2017��7��31��

@author: Mir-Z
'''
from bs4 import BeautifulSoup
import re
from urllib.parse import  urljoin
import logging
from urllib.request import urlopen
logging.basicConfig(level = logging.DEBUG,
                    format = '%(asctime)s: %(filename)s[line:%(lineno)d] %(levelname)s      %(message)s')

class HtmlParser(object):


    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a',href=re.compile(r"/item/"))#/https://baike.baidu.com/item/GPL/2357903
#        logging.info(links)
        for link in links:
            new_url = link['href']
            new_full_url = urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls
    
    def _get_new_data(self, page_url, soup):
        res_data = {}  #定义字典来存储数据
        res_data['url'] = page_url
        #<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        title_node = soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find('h1')
        #<div class="para" label-module="para">Python<sup>[1]</sup><a name="ref_[1]_21087" class="sup-anchor">&nbsp;</a>
        summary_node = soup.find('div',class_="para")
        res_data['title'] = title_node.get_text()
        res_data['summary'] = summary_node.get_text()
        return res_data
    
    def parser(self,page_url):
        if page_url is None :
            return
        html = urlopen(page_url)
        soup = BeautifulSoup(html,'html.parser',from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
#        logging.info(new_urls)
#        logging.info(new_data)
        return new_urls,new_data
