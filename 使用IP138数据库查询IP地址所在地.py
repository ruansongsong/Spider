#-*- coding:utf-8 -*-
#www.ip138.com
import urllib.request
import re

# try:
while True:
    # ipaddr = raw_input("Enter IP Or Domain Name:")
    ipaddr="120.24.228.173"
    if ipaddr == "" or ipaddr == 'exit':
        break
    else:
        url = "http://www.ip138.com/ips138.asp?ip=%s&action=2" % ipaddr
        print(url)
        req = urllib.request.Request(url)
        header={
            "GET":url,
            "User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.4368.102 Safari/537.36"
        }
        for item in header:
            req.add_header(item,header[item])

        u = urllib.request.urlopen(req)
        s = u.read()
        print(s)

        #Get IP Address
        ip = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',s)
        print ("\n****** Below Result From IP138 Database *****")
        print ("IP Address:", ip[0])
        #Get IP Address Location
        result = re.findall(r'(<li>.*?</li>)',s)
        for i in result:
            print (i[4:-5])
        print ("*"*45)
        print ("\n")
# except:
#     print ("Not Data Find")