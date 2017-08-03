	 项目简介： 
	作用：爬取百度百科词条
	spider_main:程序入口
	工作原理：首先自己定义一个爬取的url作为爬取的起始url，
	然后parser解析该页面，把当前页面（百度百科）的url、title、summary存入收集到的字典中（data）。另外还要找出该页面所有需要的url存入new_urls列表中，到此，第一个页面（自定义的url）爬取成功。
	接下来进行第二个页面的爬取：从上一个页面中获取到的new_urls列表中pop中顶上一个url作为这一轮的url爬取页面。
	如此循环。每下一个的url都是从上一个页面中爬取到的new_urls列表中pop出的一个

	IDE：eclipse
	output.html：html文件存放爬取结果
	此例子中没有用到下载器 self.downloader = html_downloader.HtmlDownloader()，其功能被解析器代劳了
	变量的作用域与函数返回值的作用域 区别
	--------
	输出html文件：
	fout = open('output.html','w',encoding='utf-8') #必须有文件的编码声明
	fout.write("<head><meta charset=\"utf-8\"></head>") #必须要html页面的编码格式
	fout.write('<td>%s<td>' % data['title'])   #title 编码格式为utf-8
	fout.write('<td>%s<td>' % data['summary'].encode('utf-8').decode('utf-8')) #summary编码格式为utf-8

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
	----------------
	count = 1
	while True:
		if count == 5:
			break
		count = count + 1
		print count
		
	break 跳出终止while循环	
	输出结果： 1 2 3 4  
	-----------------
	定义:  工程->>包->>module->>类e->>方法、字段   module在python中就是一个文件，module名跟module中定义的类的名字不同，这跟JAVA有区别（java中类名跟文件名相同）
		def _get_new_urls(self, page_url, soup)  前面加1个短横向，标明该方法为私有。
		变量的作用域与函数返回值的作用域 区别
	def __init__(self):
			#初始化
			self.urls = url_manager.UrlManager()#url_manager是一个module，UrlManager是一个类。词句实例化一个类UrlManager并赋值给 urls
			self.downloader = html_downloader.HtmlDownloader()
			self.parser = html_parser.HtmlParser()
			self.outputer = html_outpurter.HtmlOutputer()
	-----------------
	不知道函数调度哪儿出问题了，给每条语句加个try，调试用

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

