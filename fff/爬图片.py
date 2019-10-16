#!/usr/bin/python
#-*-conding:utf8-*-
import requests
a='http://img3.duitang.com/uploads/item/201504/02/20150402H2753_JuTG3.thumb.700_0.jpeg'
b=requests.get(a)
c=b.content
print(c)
with open('图片下载.jpeg','wb') as f:
    f.write(c)