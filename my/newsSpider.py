#coding:utf-8
import urllib
import urllib2
import json
import re
import os
import sys
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf8')
#返回json文件
def get_json(url):
	headers={
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36'
	}
	req=urllib2.Request(url)
	for keys in headers:
		req.add_header(keys,headers[keys])
	html = urllib2.urlopen(req)
	get_json = json.load(html)
	return get_json
#返回json文件中的URL和title
def get_url_title(get_json):
	html=get_json
	share_url=[]
	title=[]
	for i in range(len(html['data'])):
		share_url.append(html['data'][i]['share_url'])
		title.append(html['data'][i]['title'])
	return (share_url,title)
#创建文件夹
def creat_file(share_url,title):
	your_files=[]
	#根据url个数创建文件夹
	for i in range(len(share_url)):
		path='E:/ruansongsong/'+str(i)
		isExists=os.path.exists(path)
		if not isExists:
		    os.makedirs(path)		
		your_files.append(path)
	return your_files
#返回正文、img的src、图片个数
def get_content(share_url):
	headers={
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36'
	}
	get_content=[]
	img_numbers=[]
	get_imgs=[]
	for i in range(len(share_url)):
		req=urllib2.Request(share_url[i])
		for keys in headers:
			req.add_header(keys,headers[keys])
		html = urllib2.urlopen(req).read()
		print share_url[i]
		soup = BeautifulSoup(html)
		#根据不同的页面建立不同的提取规则
		if (bool(soup.find_all(attrs={'class': 'article-content'}))):
			get=soup.find_all(attrs={'class': 'article-content'})
		elif (bool(soup.find_all('article'))):
			get=soup.find_all('article')
		elif (bool(soup.find_all(attrs={'class':'rich_media_content'}))):
			get=soup.find_all(attrs={'class':'rich_media_content'})
		elif (bool(soup.find_all(attrs={'class':'content-main'}))):
			get=soup.find_all(attrs={'class':'content-main'})
		elif (bool(soup.find_all('div'))):
			get=soup.find_all('div')
		else:
			get='''<p>error</p>'''
		#得到所有段落
		paragraph=get[0].find_all('p')
		#得到所有img的链接
		paragraph1=get[0].find_all('img')
		get_img=[]
		print "获取到的图片个数"+str(len(paragraph1))
		img_numbers.append(len(paragraph1))
		for i in range(len(paragraph1)):
		  get_img.append(paragraph1[i].get('src'))
		content=[]
		for i in range(len(paragraph)):
			#获取段落文本
			temp=paragraph[i].get_text()
			content.append(temp)
		#将所有段落合并到一起
		a='\n'.join(content)
		get_content.append(a)
		#将每一个新闻中的图片的src合并在一个list
		get_imgs.extend(get_img)
	return (get_content,get_imgs,img_numbers)
#写入文件
def write_all_list(urls,titles,contents,imgs,numbers,get_file):
	x=0
	temp=0
	search = 'uploads/image/'
	for i in range(len(urls)):
		#写入url、标题、正文
		write_all_list=open(get_file[i]+"/"+"news.txt",'a')
		write_all_list.writelines("url："+urls[i]+"\n"+"title："+titles[i]+"\n"+"正文"+"\n"+contents[i]+"\n")
		write_all_list.close()
		#写入照片
		temp+=int(numbers[i])
		while(x<temp):
			temp_imgs_url=imgs[x]
			if (temp_imgs_url==None):
				x+=1
				continue
			if ((temp_imgs_url.find(search))>0):
				#好奇心日报正文中的图片链接要加上http://www.qdaily.com
				temp_imgs_url="http://www.qdaily.com"+temp_imgs_url
			print temp_imgs_url
			urllib.urlretrieve(temp_imgs_url,get_file[i]+"/"+str(x)+".jpg")
			x+=1
url="http://toutiao.com/api/article/recent/?source=2&count=20&category=news_tech&max_behot_time"
json=get_json(url)
(urls,titles)=get_url_title(json)
get_file=creat_file(urls,titles)
(contents,imgs,numbers)=get_content(urls)
#print len(get_content(share_url))
#print share_url
write_all_list(urls,titles,contents,imgs,numbers,get_file)
#print share_url
#print title