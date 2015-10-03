#coding:utf-8
import urllib
import urllib2
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')
def get_json(url):
	req=urllib2.Request(url)
	req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36')
	html = urllib2.urlopen(url)
	get_json = json.load(html)
	return get_json
def get_url_title(get_json):
	html=get_json
	share_url=[]
	title=[]
	for i in range(len(html['data'])):
		share_url.append(html['data'][i]['share_url'])
		title.append(html['data'][i]['title'])
	return (share_url,title)
url="http://toutiao.com/api/article/recent/?source=2&count=20&category=news_tech"
json=get_json(url)
(share_url,title)=get_url_title(json)
print share_url
print title