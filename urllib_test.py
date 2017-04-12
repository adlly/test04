#!/usr/bin/python
# -*- coding:UTF-8 -*-

import re

# pattern = re.compile(r'\d+')
# print re.split(pattern,'one1two2three3four4')

# pattern = re.compile(r'\d+')
# print re.findall(pattern,'one1two2three3four4')

# pattern = re.compile(r'\d+')
# for m in re.finditer(pattern,'one1two2three3four4'):
#     print m.group()

# pattern = re.compile(r'(\w+) (\w+)')
# s = 'i say, hello world!'
# print re.sub(pattern,r'\2 \1',s)
#
# def func(m):
#     return m.group(1).title() + ' ' + m.group(2).title()
#
# print re.sub(pattern,func,s)


pattern = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'

print re.subn(pattern, r'\2 \1', s)

def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()

print re.subn(pattern,func,s)