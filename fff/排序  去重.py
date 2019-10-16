#!/usr/bin/python
#-*-conding:utf8-*-
a=[3,6,10,12,56,89,67,3,12]
b=[]
for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)
for n in a:
    if n not in b:
        b.append(n)
print(b)