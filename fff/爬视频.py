#!/usr/bin/python
#-*-conding:utf8-*-
import requests
a='https://video.pearvideo.com/mp4/adshort/20190921/cont-1604840-14409612_adpkg-ad_hd.mp4'
b=requests.get(a)
c=b.content
print(c)
with open('视频下载.mp4','wb') as f:   #把c写进去
    f.write(c)