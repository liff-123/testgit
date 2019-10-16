#!/usr/bin/python
#-*-conding:utf8-*-
#存放家具
#定义一个家的类
class Home:
    def __init__(self,newarea):
        self.area=newarea
        self.containsItems=[]
    def __str__(self):
        msg='家当前可用面积为:'+str(self.area)+'平方米'
        msg+='\n家里目前的家具有:'
        if len(self.containsItems)>0:
            for i in self.containsItems:
                msg+='席梦思，席梦思2'+','
            msg=msg.strip(',')
        else:
            msg+='当前还没有家具'
        return  msg
    def additems(self,item):
        if self.area>item.area:
            self.containsItems.append(item)
            self.area=item.area
class Bed:
    def __init__(self,newname,newarea):
        self.name=newname
        self.area=newarea
    def __str__(self):
        msg='床的面积为:'+str(self.area)+'平方米'
        msg+='\n床的样式为:'+self.name
        return  msg
home=Home(110)
print(home)
bed=Bed('席梦思',4)
print(bed)
home.additems(bed)
print(home)