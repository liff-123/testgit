#!/usr/bin/python
#-*-conding:utf8-*-
for x in range(1, 5):
    for y in range(1, 5):
        for z in range(1, 5):
            if (x != y) and (x !=z ) and (y != z):
                print(x*100+y*10+z*1,end=' ')
    print('')