#!/usr/bin/python
#-*-conding:utf8-*-
a=[24,25,35,0]
for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)