#!/usr/bin/python
#-*-conding:utf8-*-

#十进制转十六进制
a = [str(i) for i in range(10)]+[chr(i) for i in range(97,103)]
b = int(input('>>>'))
f = []
while True:
    c = b%16
    b = b//16
    f.append(a[c])
    if b == 0:
        break
f.reverse()
s = ''.join(f)
print(s)
