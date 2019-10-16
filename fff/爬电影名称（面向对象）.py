#!/usr/bin/python
#-*-conding:utf8-*-

#爬电影名称 （面向对象）
import requests
import re

class Douban(object):
    def qing_qiu(self, page):
        url = f'https://movie.douban.com/top250?start={page}&filter='      #以90为一页
        head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
        }
        # 发送请求，并将结果赋值给res
        res = requests.get(url=url, headers=head)
        # 读取结果
        h = res.content.decode('utf-8')
        return h

    def guo_lv(self, html):
        patt = re.compile(r'<span class="title">(.*?)</span>', re.S)
        items = patt.findall(html)

        for i in items:
            if '&nbsp' in i:
                items.remove(i)
        return items

    def save(self, shuju):
        with open('mm.txt', 'a', encoding='utf-8') as f:
            for i in shuju:
                f.write(i + '\n')


dd = Douban()
for i in range(0, 100, 25):
    hh = dd.qing_qiu(i)
    shuju = dd.guo_lv(hh)
    dd.save(shuju)
