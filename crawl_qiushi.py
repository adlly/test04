#!/usr/bin/python
# -*- coding:UTF-8 -*-

import urllib
import urllib2
import re
import bs4

url = "http://www.qiushibaike.com/hot/page/1"
user_agent = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36"
headers = {'User-Agent': user_agent}
try :
    request = urllib2.Request(url, headers= headers)
    response =  urllib2.urlopen(request)
    content =  response.read()
    # print content
    # pattern = re.compile('<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?'+
    #                      'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
    html = bs4.BeautifulSoup(content, 'html5lib')
    items = html.findAll('div', attrs={'class':'content-text'})
    count = 0
    for i in items:
        count += 1
        print i
    print str(count)
    # for item in items:
    #
    #   print item[0],item[1],item[2],item[3],item[4]

except urllib2.URLError,e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"name"):
        print e.name

