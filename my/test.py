#coding:utf-8
import urllib
import urllib2
#获取txt中的IP地址
def get_ip():
	object_ip=open("C:/Users/ruans/Desktop/Sumer vacation/python/ip/ip.txt","r")
	ip_list=object_ip.readlines()
	object_ip.close()
	return ip_list
#添加IP代理
def add_proxy(ip):
	ip_proxy=urllib2.ProxyHandler({'http':ip})
	opener=urllib2.build_opener(ip_proxy)
	urllib2.install_opener(opener)
#添加header
def add_headers(url):
	headers={
		#其他headers
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36"
	}
	req=urllib2.Request(url)
	for keys in headers:
		req.add_header(keys,headers[keys])
	html=urllib2.urlopen(req)
	return html
ip_list=get_ip()
url="http://www.baidu.com"
for index in range(len(ip_list)):
	add_proxy(ip_list[index])
	html=add_headers(url).readline()
	print html 
'''
proxy = '117.185.124.74:80'
proxy_support = urllib2.ProxyHandler({'http':proxy})
# opener = urllib2.build_opener(proxy_support,urllib2.HTTPHandler(debuglevel=1))
opener = urllib2.build_opener(proxy_support)
urllib2.install_opener(opener)
url = "http://www.baidu.com"
req=urllib2.Request(url)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36')
html=urllib2.urlopen(req).read()
print html
'''