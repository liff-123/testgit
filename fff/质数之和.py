#!/usr/bin/python
#-*-conding:utf8-*-aa
a=0
for i in range(2,10):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        a=a+i
print(a)


