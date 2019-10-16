#!/usr/bin/python
#-*-conding:utf8-*-
a=0
for i in range(1,5):
    b=1
    for j in range(1,i+1):
        b=b*j
    a=a+b
print(a)