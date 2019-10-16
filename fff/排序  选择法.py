#!/usr/bin/python
#-*-conding:utf8-*-

#冒泡
# a = [3, 5, 2, 1, 8, 4]
# b = len(a)
# for x in range(b-1):
#    for y in range(x+1,b):
#       if a[x]>a[y]:
#          a[x],a[y]=a[y],a[x]
#          print(a)

#排序  选择法
a = [12, 56, 5, 89, 32]
for i in range(len(a)-1):
   for j in range(i + 1, len(a)):
      if a[i] > a[j]:
         a[i], a[j] = a[j], a[i]
   print(a)


#不简便的方式
# a = [12, 56, 5, 89, 32]
# for i in range(len(a)-1):
#    c = i
#    for j in range(i + 1, len(a)):
#       if a[j] < a[c]:
#          a[j], a[c] = a[c], a[j]
#    print(a)


# 用函数
# def selection_sort(arr):
#   for i in range(len(arr) - 1):
#       min_index = i
#       for j in range(i + 1, len(arr)):
#           if arr[j] < arr[min_index]:
#              min_index = j
#       arr[min_index], arr[i] = arr[i], arr[min_index]
#   return arr
# print(selection_sort([12,56,5,89]))