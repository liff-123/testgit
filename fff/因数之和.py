#!/usr/bin/python
#-*-conding:utf8-*-

#因数之和
a=0
for i in range(1,10):
    for j in range(1,i+1):
        if i%j==0:
            a=a+j
print(a)


#用函数
# def hanshu(x):
#     a=0
#     for i in range(x+1):
#         for j in range(1,i+1):
#             if i%j==0:
#                 a=a+j
#     return a
# print(hanshu(9))




