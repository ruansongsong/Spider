#coding:UTF-8
#coding:utf-8
import urllib
import urllib2
import re
import os
import sys
import jieba
reload(sys)
sys.setdefaultencoding('utf8')
'''
def get_url():
	object_url=open("C:/Users/ruans/Desktop/Sumer vacation/python/ip/title_url.txt","r")
	url_list=object_url.readline()
	object_url.close()
	return url_list
'''
def add_headers(url):
	headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36"
	}
	req=urllib2.Request(url)
	for keys in headers:
		req.add_header(keys,headers[keys])
	html=urllib2.urlopen(req)
	return html
def get_titlelist(html):
	reg=r'<a href="/p.*? title="(.*?)".*?>.*?</a>'
	title_re=re.compile(reg)
	title_list=re.findall(title_re,html)
	return title_list
def creat_file():
	#判断目录是否存在
	path="E:/ruansongsong/"
	isExists=os.path.exists(path)
	if not isExists:
	    os.mkdir(path)
	filename="jieba_title_list.txt"
	your_file=path+filename
	write_ip=file(your_file,"w+")
	return your_file

def write_jieba_list(jieba_list,file):
	write_jieba_list=open(file,'a')
	for i in range(len(jieba_list)):
		#a.append(href_list[i])
		write_jieba_list.writelines(jieba_list[i]+"\n")
		'''
	for j in title_list:
		write_all_list.writelines(j+"\n")
	'''
	write_jieba_list.close()
def get_urls():
	url=['http://tieba.baidu.com/f?kw=%E5%A4%9A%E7%9B%8A%E7%BD%91%E7%BB%9C&ie=utf-8&pn=0']
	i=0
	while(i<=150):
		url.append('http://tieba.baidu.com/f?kw=%%E5%%A4%%9A%%E7%%9B%%8A%%E7%%BD%%91%%E7%%BB%%9C&ie=utf-8&pn=%s'%i)
		i+=50
	return url
urls=get_urls()
get_file=creat_file()
jieba_list=[]
for index in range(len(urls)):
	html=add_headers(urls[index]).read()
	title_list=get_titlelist(html)
	for j in range(len(title_list)):	
		seg_list=list(jieba.cut(title_list[j],cut_all=False))
		a='jieba:'
		for i in seg_list:
			a+=(i.encode('utf-8')+"/")
		jieba_list.append(a)
write_jieba_list(jieba_list,get_file)
#print jieba_list[10]