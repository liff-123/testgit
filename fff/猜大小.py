#!/usr/bin/python
#-*-conding:utf8-*-
import random
a=random.randrange(10)
for i in range(3):
    b=int(input('>>>'))
    if a>b:
        print('你猜小了')
    elif a<b:
        print('你猜大了')
    elif a==b:
        print('你猜对了')
        break
else:
    print('结束了')
