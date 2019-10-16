#!/usr/bin/python
#-*-conding:utf8-*-

#不用int将字符串变成整数
a='1345'
a=a[::-1]
print(a)      #5431
b=0
for i in range(len(a)):      #i=0        i=1       i=2         i=3
    for j in range(10):      #j=5       j=4        j=3         j=1
        if str(j)==a[i]:     #5x10**0   4x10**1     3x10**2    1x10**3
            b+=j*10**i       #5         40+5        300+45     1000+345
print(b)     #str  因为a是字符串所以j要用字符串来比