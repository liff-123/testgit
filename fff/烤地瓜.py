#!/usr/bin/python
#-*-conding:utf8-*-
#烤地瓜
class Sweetpotato:
    #定义属性，一般用来完成一些初始化的工作
    def __init__(self):
        self.cookedLevel=0                                #0-3生的，3-5半生不熟，5-8已经考好了，>8烤成木炭了
        self.cookedString='生的'                         #生熟的程度
        self.condiments=[]                               #烤的时间
    def __str__(self):
        msg='地瓜的成熟程度:'+self.cookedString
        msg+='\n地瓜的等级为:'+str(self.cookedLevel)
        msg+='\n添加佐料为:'
        if len(self.condiments)>0:
             for i in self.condiments:
                msg+=i+','
             msg=msg.strip(',')
        else:
            msg+='当前没有佐料'
        return msg
    def cook(self,times):
        self.cookedLevel+=times
        if self.cookedLevel>8:
            self.cookedString='考成木炭了'
        elif self.cookedLevel>5:
            self.cookedString='已经烤好了'
        elif self.cookedLevel>3:
            self.cookedString='半生不熟'
        else:self.cookedString='生的'
    def addcondiments(self,temp):
        self.condiments.append(temp)
digua=Sweetpotato()
print(digua)
digua.cook(4)
print(digua)
digua.addcondiments('芥末')
digua.cook(2)
print(digua)
digua.addcondiments('番茄酱')
digua.cook(3)
print(digua)
