#!/usr/bin/python
#-*-conding:utf8-*-
with open('enen.txt',mode='r',encoding='utf-8') as f:
    a=f.readlines().count('\n')
    print(a)