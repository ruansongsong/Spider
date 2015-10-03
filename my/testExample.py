#coding:utf-8
'''
urlopen返回对象提供方法：

-         read() , readline() ,readlines() , fileno() , close() ：这些方法的使用方式与文件对象完全一样

-         info()：返回一个httplib.HTTPMessage对象，表示远程服务器返回的头信息

-         getcode()：返回Http状态码。如果是http请求，200请求成功完成;404网址未找到

-         geturl()：返回请求的url
'''
#test1 redline()函数
'''
import urllib
html=urllib.urlopen('http://www.baidu.com')
firstLine=html.readline()
print firstLine
'''

#test2 read()函数
'''
import urllib
html=urllib.urlopen('http://www.ifeng.com')
allRead=html.read()
print allRead
'''
'''
测试百度，百度采取了防爬措施
'''
'''
import urllib
html=urllib.urlopen('http://www.baidu.com')
allRead=html.read()
print allRead
'''
'''
下面加header试试
'''
'''
import urllib
import urllib2
url="http://www.ifeng.com/"
headers={
	#仅仅要user-agent就行
	
	#"GET":url,
	#"Host":"www.baidu.com",
	#"Referer":"https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=rr&rsv_pq=dd63ffe00002ad51&rsv_t=62edx55xgu4j9miwY8rZS4Pes7dOF3YDrL8Ta12ZvuNTTE9%2F6Z1tKw05QpA&rsv_enter=1&rsv_sug3=3&rsv_sug1=2&oq=%E4%BA%BA%E4%BA%BA%E7%BD%91&rsv_sug2=0&inputT=1224&rsv_sug4=1904",
	#"Cookie":"PSTM=1438510017; BIDUPSID=FE36914512177E9E33559C2256AF0A43; BD_UPN=12314753; H_PS_645EC=d29671SPbH42caj6IYHa0B6wDS96QTpDMuH%2BNNLvsUxmEVCdYSjG%2FYByeW4; BAIDUID=3C88266F5ADAECACBAD687C1E64E6A47:FG=1; BDSVRTM=86; H_PS_PSSID=1423_12658_10812_14430_12868_14669_16521_16513_16664_16424_16514_15478_11666_13932",
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36"
}
req=urllib2.Request(url)
for keys in headers:
	req.add_header(keys,headers[keys])
html=urllib2.urlopen(req)
firstLine=html.readlines()
header=html.info()
get_code=html.getcode()
get_url=html.geturl()
print get_url
'''
#test3 urlretrieve()
'''
urlretrieve方法将url定位到的html文件下载到你本地的硬盘中。如果不指定filename，则会存为临时文件。

urlretrieve()返回一个二元组(filename,mine_hdrs)

'''
'''
import urllib
def Schedule(a,b,c):
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
    print '%.2f%%' % per
url="http://www.baidu.com"
file_path='C:/Users/ruans/Desktop/Sumer vacation/python/tempFile/test.html'
urllib.urlretrieve(url,file_path,Schedule)
'''
#test4 urllib.quote(url)和urllib.quote_plus(url) urllib.unquote(url)和urllib.unquote_plus(url)
#将url数据获取之后，并将其编码，从而适用与URL字符串中，使其能被打印和被web服务器接受。
'''
import urllib
url="http://www.baidu.com"
url_quote=urllib.quote(url)
unurl="https://www.baidu.com/s?wd=%E7%99%BE%E5%BA%A6%E5%92%8C%E8%B0%B7%E6%AD%8C%E5%93%AA%E4%B8%AA%E5%A5%BD&rsv_spt=1&issp=1&f=3&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=6&rsv_sug1=3&oq=%E7%99%BE%E5%BA%A6%E5%92%8C%E8%B0%B7%E6%AD%8C&rsv_pq=d0a72d62000082aa&rsv_t=ffe8srAMv5O%2FSW1GU8477t0uRSehxtGuVEyj8ttIQj2yifAQP3Wj%2BKr93sY63BLaB1Xq&rsv_sug2=0&rsp=1&inputT=9133&rsv_sug4=10954"
url_unquote=urllib.unquote(unurl)
print url_quote
print url_unquote
'''
#test6 urllib.urlencode()
'''
6.urllib.urlencode(query)
将URL中的键值对以连接符&划分
这里可以与urlopen结合以实现post方法和get方法：
'''
#GET方法
'''
>>> import urllib
>>> params=urllib.urlencode({'spam':1,'eggs':2,'bacon':0})
>>> params
'eggs=2&bacon=0&spam=1'
>>> f=urllib.urlopen("http://python.org/query?%s" % params)
>>> print f.read()
'''
#POST方法
'''
>>> import urllib
>>> parmas = urllib.urlencode({'spam':1,'eggs':2,'bacon':0})
>>> f=urllib.urlopen("http://python.org/query",parmas)
>>> f.read()
'''
'''
import urllib
list_a=urllib.urlencode(
	{
	'apple':1,
	'banana':2,
	'egg':3
	}
	)
print list_a
'''
#获取文本每一行
import urllib2
import urllib
import re
object=open("C:/Users/ruans/Desktop/Sumer vacation/python/ip/url.txt","r")
url_list=object.readlines()
object.close()
for index in range(len(url_list)):
	print url_list[index]
