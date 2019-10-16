#!/usr/bin/python
#-*-conding:utf8-*-

#将列表中的元素向左挪一位
a=[1,78,56,29]
for i in range(len(a)-3):
    a.insert(len(a),a[0])
    a.remove(a[0])
    print(a)