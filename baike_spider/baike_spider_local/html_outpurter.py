#coding=utf-8
'''
Created on 2017��7��31��

@author: Mir-Z
'''
import logging
logging.basicConfig(level = logging.INFO,
                    format = '%(asctime)s: %(filename)s[line:%(lineno)d] %(levelname)s      %(message)s')

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
    
    
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)
    
    def outputer_html(self):
        logging.info('outputer_html')
        fout = open('output.html','w',encoding='utf-8')
        fout.write('<html>')
        fout.write("<head><meta charset=\"utf-8\"></head>")
        fout.write('<body>')
        fout.write('<table>')
        
        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s<td>' % data['url'])
            fout.write('<td>%s<td>' % data['title'])
            logging.info(data['title'])
            fout.write('<td>%s<td>' % data['summary'].encode('utf-8').decode('utf-8'))
            fout.write('</tr>')
        
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
    
    
    



