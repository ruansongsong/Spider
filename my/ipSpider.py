#coding:utf-8
import urllib
import urllib2
import re
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
def get_url():
	object_url=open("C:/Users/ruans/Desktop/Sumer vacation/python/ip/getip.txt","r")
	url_list=object_url.readline()
	object_url.close()
	return url_list
def add_headers(url):
	headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36"
	}
	req=urllib2.Request(url)
	for keys in headers:
		req.add_header(keys,headers[keys])
	html=urllib2.urlopen(req)
	return html
def get_iplist(html):
	reg=r"(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d]):\d{1,5}"
	ip_re=re.compile(reg)
	ip_list=re.findall(ip_re,html)
	return ip_list
def creat_file():
	#判断目录是否存在
	path="E:/ruansongsong/"
	isExists=os.path.exists(path)
	if not isExists:
	    os.mkdir(path)
	filename="ip_list.txt"
	your_file=path+filename
	write_ip=file(your_file,"w+")
	return your_file
def write_iplist(ip_list,file):
	write_iplist=open(file,'a')
	for i in ip_list:
		write_iplist.writelines(i+"\n")
	write_iplist.close()
def get_urls():
	url=['http://www.youdaili.net/Daili/guonei/3450.html']
	for i in range(2,7):
		url.append('http://www.youdaili.net/Daili/guonei/3450_%s.html' % i)
	return url
urls=get_urls()
get_file=creat_file()
for index in range(len(urls)):
	html=add_headers(urls[index]).read()
	ip_list=get_iplist(html)
	write_iplist(ip_list,get_file)