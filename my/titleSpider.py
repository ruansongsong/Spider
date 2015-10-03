#coding:utf-8
import urllib
import urllib2
import re
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
#获取txt中的url，返回URL列
'''
def get_url():
	object_url=open("C:/Users/ruans/Desktop/Sumer vacation/python/ip/url.txt","r")
	url_list=object_url.readline()
	object_url.close()
	return url_list
'''
#对url加报头，返回html
def get_html(url):
	req=urllib2.Request(url)
	req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36')
	html=urllib2.urlopen(req).read()
	return html
def get_hreflist(html):
	reg=r'(?<=<a href=\"/p)([^\"]+)'
	href_re=re.compile(reg)
	href_list=re.findall(href_re,html)
	return href_list
#匹配html中的href地址，返回href地址
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
	filename="title_list.txt"
	your_file=path+filename
	write_ip=file(your_file,"w+")
	return your_file
#写入到txt文件
def write_all_list(href_list,title_list,file):
	write_all_list=open(file,'a')
	for i in range(len(href_list)):
		#a.append(href_list[i])
		write_all_list.writelines("http://tieba.baidu.com/p"+href_list[i]+" 标题："+title_list[i]+"\n")
		'''
	for j in title_list:
		write_all_list.writelines(j+"\n")
	'''
	write_all_list.close()
url="http://tieba.baidu.com/f?kw=%E5%A4%9A%E7%9B%8A%E7%BD%91%E7%BB%9C"
html=get_html(url)
href_list=get_hreflist(html)
title_list=get_titlelist(html)
get_file=creat_file()
write_all_list(href_list,title_list,get_file)
#？？？
#上面这些代码可以正常运行，但是我print列表中的title_list[0] 会显示[Decode error - output not utf-8]
#
#encode('UTF-8') decode('UTF-8') 以及修改了个配置文件为	"encoding":"utf-8",	"encoding":"cp936",都不行
#???

a=title_list[0]
b=title_list[1]
print type(a)