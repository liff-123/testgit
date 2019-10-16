#!/usr/bin/python
#-*-conding:utf8-*-

#显示所有第一大和第二大的数
b=[99,99,65,86,86,86,12]
b.sort()
c=[]
for i in b:
    if i not in c:
        c.append(i)
print(c)
c.reverse()
print(c)
for j in b :
    if j==c[1] or j==c[0]:   #取c表里第一个和第二个数据，如果b列表里有和第一个，第二个相同的数，就给他打印出来
        print(j,end=' ')