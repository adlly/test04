#!/usr/bin/python
# -*- coding:UTF-8 -*-

import selenium.webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

chrome = selenium.webdriver.Chrome()

chrome.get('http://www.baidu.com')

chrome.find_element_by_id('kw').send_keys('aa')
chrome.find_element_by_id('su').send_keys(Keys.RETURN)

# 网页的shishiyuanma


# pattern = re.compile('<h3 class="t"><a.*?>(.*?)</a></h3>', re.S)
# match = re.findall(pattern=pattern, string=source)
# for i in match:
#     if i == None:
#         print('Not found')
#     else:
#         print(i)
chrome.refresh()
# time.sleep(1)
# source = chrome.find_element_by_xpath("//*").get_attribute("outerHTML")
source = chrome.page_source
open('source.html', 'w+').write(source.encode('utf-8'))
# print source
soup = BeautifulSoup(source,'lxml')
# head = soup.find_all("h3", class_='t')
# for i in head:
#     print(i.a.text)
#     print(i.a.attrs['href'])

main = soup.findAll('div', class_='result c-container ')

for i in main:
    print(i.a.text)
    child = i.find('div', class_='c-abstract')
    if child != None:
        print(i.span.text)
        print(i.text)
    else:
        print 'None'

chrome.close()
