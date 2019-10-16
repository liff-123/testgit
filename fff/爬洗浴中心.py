#!/usr/bin/python
#-*-conding:utf8-*-
#loads：反序列化（就是将ison格式转换为python的字典格式）
import requests
import json
# a=json.loads('{"result":{"data":12}')     #将字符串转化为字典格式
# print(type(a))
url='https://map.baidu.com/?qt=subwayscity&t=1569032020609'
html=requests.get(url)
geshi=html.text   #改接收的方式
result=json.loads(geshi)#转格式
i=0
while True:
    try:
        city=result['subways_city']['cities'][i]['cn_name']
        print(city)
        i+=1
    except:
        break