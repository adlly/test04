#!/usr/bin/python
# -*- coding:UTF-8 -*-

import urllib
import urllib2

url = "http://www.qiushibaike.com/hot/page/1"
user_agent = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36"
headers = {'User-Agent': user_agent}
try :
    request = urllib2.Request(url, headers= headers)
    response =  urllib2.urlopen(request)
    print response.read()
except urllib2.URLError,e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"name"):
        print e.name

