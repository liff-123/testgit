#!/usr/bin/python
#-*-conding:utf8-*-
#判断三角形
a=int(input('一边：'))
b=int(input('二边：'))
c=int(input('三边：'))
n=[a,b,c]
n.sort()
if n[0]+n[1]>n[2]:
    if n[0]**2+n[1]**2==n[2]**2:
        print('直角三角形')     #a2+b2=c2
    elif n[0]**2+n[1]**2>n[2]**2:
        print('锐角三角形')     #a2+b2>c2
    elif n[0]**2+n[1]**2<n[2]**2:
        print('钝角三角形')      #a2+b2<c2
else:
    print('不是三角形')