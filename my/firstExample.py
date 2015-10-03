#coding:utf-8
import urllib2
import urllib
import re
gjc=urllib.quote("电影")
url_object=open('url.txt')
try:
	url_text=url_object.read();
finally:
	url_object.close()

url=url_text+gjc
headers={
	"GET":url,
	"Host":"www.haosou.com",
	"Referer":"http://www.haosou.com/",
	"User-Agent":"Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
}
req=urllib2.Request(url)
for key in headers:
	req.add_header(key,headers[key])

html=urllib2.urlopen(req).read()
ss=re.findall("\"(.*?)\"",html)
for items in ss:
	print items