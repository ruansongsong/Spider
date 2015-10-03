#coding:utf-8
import urllib2
import urllib
import re
from random import choice
class SetHP(object):
	# variable：
	# self.iplist=[]
	# self.url=url
	# self.r = ''
	# header form:
	# 	"GET":url,
	# 	"Host":"sug.so.360.cn",
	# 	"Referer":"http://www.haosou.com/",
	# 	"User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/530.4368.102 Safari/537.36"
	# }
	def __init__(self, url, header=None):
		self.iplist=[]
		self.url=url
		self.res = ''

		req = urllib2.Request(url)
		if header is not None:
			for key in header:
				req.add_header(key,header[key])

		#添加代理
		# try:
		# 	for line in open(r'getip.ip','r'):
		# 		self.iplist += [line.strip()]
		# except IOError:
		# 	pass
		# if len(self.iplist):
		# 	ip=choice(self.iplist)
		# 	proxy_handler = urllib2.ProxyHandler({'http': 'http://'+ip})
		# 	opener = urllib2.build_opener(proxy_handler)
		# 	urllib2.install_opener(opener)
		# else:
		# 	print "iplist is None"
		
		self.res = urllib2.urlopen(req).read()

	url="http://www.baidu.com"
	response=SetHP(url)
	print(response.url, response.iplist,response.res)