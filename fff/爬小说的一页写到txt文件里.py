#!/usr/bin/python
#-*-conding:utf8-*-

#爬小说的一页
# import re
# import requests
# a='http://www.quanshuwang.com/book/9/9055/9674264.html'
# b=requests.get(a)
# e=b.content.decode('gbk')
# # print(e)
# guolv=re.compile('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)&nbsp;&nbsp;&nbsp;&nbsp;',re.S)
# answer=guolv.findall(e)
# for i in answer:
#     i=i.strip('<br />\r\n<br />\r\n')+'\n'
#     h=open('aa.txt','a',encoding='UTF-8')
#     h.write(i)



#用函数爬10页小说
import re
import requests
class Xiao_shuo(object):
    def Qing_qiu(self,j):
        a='http://www.quanshuwang.com/book/9/9055/{}.html'.format(j)
        b=requests.get(a)
        e=b.content.decode('gbk')
        return e
    def Guo_lv(self,r):
        guolv=re.compile('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)&nbsp;&nbsp;&nbsp;&nbsp;',re.S)
        answer=guolv.findall(r)
        for i in answer:
            i=i.strip('<br />\r\n<br />\r\n')+'\n'
            h=open('aa.txt','a',encoding='UTF-8')
            h.write(i)
aa=Xiao_shuo()
for j in range(9674264,9674275):
    bb=aa.Qing_qiu(j)
    aa.Guo_lv(bb)


