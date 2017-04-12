#!/usr/bin/python
#-*- coding:UTF-8 -*-

import urllib2
req = urllib2.Request('http://xx.com')

try :
    resp = urllib2.urlopen(req)
    resp = urllib2.urlopen(req)
except urllib2.URLError as e:
  if hasattr(e, 'reason'):
    print(e.reason)
    print e
  else:
    print('error')