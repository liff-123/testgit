#!/usr/bin/python
#-*-conding:utf8-*-
while True:
    print('-'*10,'start','-'*10)
    a=int(input('>>>'))
    if 100>=a>=90:
        print('优秀')
    elif 90>a>80:
        print('良好')
    elif 80>a>60:
        print('及格')
    elif 60>a>0:
        print('不及格')
    else:
        print('太差了')
    print('-' * 10, 'end', '-' * 10)