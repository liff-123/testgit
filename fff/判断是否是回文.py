#!/usr/bin/python
#-*-conding:utf8-*-
#判断是否是回文   12321是回文或者123321  123412不是
while True:
     a = input('>>>')
     b = list(a)
     c = list(reversed(b))
     if b==c:
         print('回文')
     else:
        print('不是回文')







