#!/usr/bin/env python
#-*- encoding:utf-8 -*-
# 注1：请使用chrome浏览器，并在地址栏里输入chrome://flags/，然后查找QUIC，启用该协议，同时建议启用SPDY/4，能让访问更流畅。
# 注2：请使用https的方式访问，比如：https://www.google.com
# 注3：默认可能会跳转到www.google.com.hk，如果.hk访问困难，请使用：https://www.google.com/ncr 方式访问，禁止国别跳转。
import sys
import urllib,sys,platform
import urllib2

# reload(sys)
# sys.setdefaultencoding('utf-8')

#确定操作系统平台
if platform.uname()[0]=='Windows':
    file = r'c:\windows\system32\drivers\etc\hosts'
    # file = 'C:/Users/Administrator/Desktop/host.txt'
else:
    file=r'/etc/hosts'

url='http://www.360kb.com/kb/2_150.html'
data=urllib2.Request.urlopen(url).read().decode('utf-8')
# 加上decode('utf-8')后print(data)时出错
# UnicodeEncodeError: 'gbk' codec can't encode character '\xa9' in position 33806: illegal multibyte sequence

if data is not None:
    a=data.find('#google-hosts-2015')
#    b=data.find('#google-hosts-2015-end')
 
    b=data.find('<br /></div></div>')
    if a==-1 or b==-1:
        sys.exit(-1)
    data=data[a:b].split("\n")
    print(data)
    '''
    #lines 保存hosts文件中原有的信息
    fpr=open(file, 'r')
    lines=fpr.readlines()
    fpr.close()

    fpw=open(file, 'w')
    flag=0

    for line in lines:
        if "google-hosts" in line:
            for dt in data:
                fpw.write(dt+'\n')
            flag=1
        elif flag!=1:
            fpw.write(line)
        if "google hosts" in line:
        	flag=2

    #flag==0表示原hosts文件中没有添加过google-hosts
    if flag==0:
    	for dt in data:
            fpw.write('\n'+dt)

    fpw.close()
    print ('ok')
else:
    print ('url not found')

    '''
