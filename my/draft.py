import urllib2
import urllib
import re
object=open("C:/Users/ruans/Desktop/Sumer vacation/python/ip/url.txt","r")
url_list=object.readlines()
object.close()
headers={
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36"
}
req=urllib2.Request(url_list)
for keys in headers:
	req.add_header(keys,headers[keys])
html=urllib2.urlopen(req).read()
reg =r"http:.+?\.jpg"
img_re=re.compile(reg)
img_list=re.findall(img_re,html)
x=0
for img_url in img_list:
	urllib.urlretrieve(img_url,'C:/Users/ruans/Desktop/Sumer vacation/python/tempFile/%s.jpg' % x)
	x+=1