#!/usr/bin/python
# -*- coding:UTF-8 -*-
import urllib
import urllib2
import  httplib
request = urllib2.Request("http://www.baidu.com", data="baidu")
request.get_method = lambda: 'PUT' # or 'DELETE'
response = urllib2.urlopen(request)