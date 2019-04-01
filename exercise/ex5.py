# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2019-03-30 15:34:38
# @Last Modified by:   Marte
# @Last Modified time: 2019-03-30 15:53:31
# list的学习 熟练各种函数
# cmp（list1，list2）比较两个函数 3.7 cmp失效了
list1, list2 = [123, 'xyz'], [456, 'abc']
print(len(list1))
list3 =[7,8,9]
print('list3 max num %d' % max(list3))
print('list3 min num %d' % min(list3))
list3.append(7)
print(list3)
print('list3 has 7 num is %d' % list3.count(7))
print('8 at list3 index id %d' % list3.index(8))
list3.insert(1,11)
print(list3)
print(list3.pop())
list3 =list3.reverse()
print(list3)

print("*"*15)

user =['liangdianshui','两点水','twowater']
print('\n1.产品名称')
print(user)
len(user)
print("\n2.一共有多少用户")
print(len(user))

