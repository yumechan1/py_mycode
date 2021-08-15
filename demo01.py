import random
# print(random.sample(range(10),10))
# print(random.sample(range(10),20))
#
# d = {
#     "name": "木瓜太香",
#     "age": "18"
# }
#
# a,b = d
# print(a,b)
# print(0j)
#
# i=0
# while i<10:
#     print(f"{i}小于10")
#     i+=1
# else:
#     print(f"循环结束，当前i为:{i}")
#
# print(f"最后打印一下i:{i}")
#
# def fn():
#     print(fn)
#
# fn.s = "木瓜太大"
# print(fn.s)

# class Animal(object):
#     def __init__(self,name):
#         self.name = name
#
#     def __call__(self,age):
#         print(f"我的名字叫做{self.name},今年{age}岁")
#
#
# a1 = Animal("木瓜")
#
# a1(18)

# s = "木瓜太香"
# print("%-08o" % 111)

# from string import Template
#
# t = Template("""
# 我是：${username}
# 今年：${age}岁
# """)
#
# print(t.substitute({"username": "木瓜太香", "age": 18}))
#

from random import choices,shuffle
# s = "苹果草莓香蕉榴莲"
# print(s.find("草莓1"))
# print(s.count("榴莲"))

# l1 = [1,2,3,4,5,6]
#
# l2 = choices(l1)
# print(l1)
# print(l2)

# l1 = [1,2,3,4,5]
# l2 = shuffle(l1)
#
# print(l1)
# print(l2)


# l1 = "西瓜1,甜瓜2,榴莲3,草莓4"
# print(l1.split(",",maxsplit=2))

# x = "你好 啊哈哈哈   1"
#
# print("".join(x.split()))

# s = "苹果西瓜苹果"
# print(s.replace("苹果","木瓜",1))

# table = str.maketrans({
#     "a": "1",
#     "b": "2"
# })
#
# s = "aabbcc"
# print(s.translate(table))
#
# s1 = "abcs"
#
# print(s1.islower())





