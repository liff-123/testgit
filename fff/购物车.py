#!/usr/bin/python
#-*-conding:utf8-*-
# 要求用户输入总资产，例如：2000                                           #购物车
# 显示商品列表，让用户根据序号选择商品，加入购物车
# 购买，如果商品总额大于总资产，提示账户余额不足，否则，购买成功
# 附加：可充值，某商品移除购物
a=int(input('>>>'))
b=2000
c=[]
d={'name':'电脑','price':1999},{'name':'鼠标','price':10},{'name':'游艇','price':20},{'name':'美女','price':998}
for i,j in enumerate(d):
    print(enumerate(d))
    for u in range(1,4):
        if i==0:
            print('你已添加电脑')
            break
        elif i==1:
            print('你已添加鼠标')
            break
        elif i==2:
            print('你已添加游艇')
            break
        elif i==3:
            print('你已添加美女')
            break