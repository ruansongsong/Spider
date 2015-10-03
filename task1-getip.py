#coding:utf-8
import sethp
import sys
import re
class GetIP(object):
	# the IP is gotten from "http://www.xici.net.co/nn/"
	# variable：
	# self.url="http://www.xici.net.co/"
	# self.iplist=[]
	def __init__(self):
		self.url="http://www.xici.net.co/"
		self.iplist=[]
		self.header={
			"GET":self.url,
			"Host":"www.xici.net.co",
			"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 UBrowser/5.2.2603.31 Safari/537.36"
			}
		response = sethp.SetHP(self.url, self.header).res
		ss=re.findall("<td>\d*\.\d*\.\d*\.\d*</td>\s{0,6}<td>\d*</td>",response)
		# print ss
		if len(ss) == 0:
			print "the ip crawled is none"
			sys.exit()
		output=open('getip.ip', 'w')
		for item in ss:
			# print (item.replace('<td>','').replace('</td>', '').replace('\n    ', ':'))
			ip=item.replace('<td>','').replace('</td>', '').replace('\n    ', ':')
			output.write(ip+'\n')
			self.iplist+=[ip]
		output.close()

if __name__ == '__main__':
	for ip in GetIP().iplist:
		print ip