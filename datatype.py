#!/usr/bin/evn python3
# _*- coding: utf-8 -*-

"""
Python数据类型
"""

# 整型变量
counter = 100
# 浮点型变量
miles = 1000.0
# 字符串
name = "runoob"

# 多个变量赋值
a = b = c = 1

a, b, c = 1, 2, "runoob"

# 标准数据类型
"""
Python中有六个标准数据类型
Number(数字)
String(字符串)
List(列表)
Tuple(元组)
Sets(集合)
Dictionary(字典)
"""

list = ['abcd', 789, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']

# 输出完整列表
print(list)
# 输出列表第一个元素
print(list[0])
# 从第二个开始输出到第三个元素
print(list[1:3])
# 输出从第三个元素开始的所有元素
print(list[2:])
# 输出两次列表
print(tinylist * 2)
# 连接列表
print(list + tinylist)

# Tuple(元组)
"""
元组(tuple)与列表类似,不同之处在于元组的元素不能修改。元组写在小括号(())里,元素之间用逗号隔开。
元组中的元素类型也可以不相同
"""
tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')

# 输出完整元组
print(tuple)
# 输出元组的第一个元素
print(tuple[0])
# 输出从第二个元素开始到第三个元素
print(tuple[1:3])
# 输出从第三个元素开始的所有元素
print(tuple[2:])
# 输出两次元组
print(tinytuple * 2)
# 连接元组
print(tuple + tinytuple)

tup = (1, 2, 3, 4, 5, 6)
print(tup[0])

print(tup[1:5])

for i in tup:
    print(i, end=',')

# 空元组
tup1 = ()
# 一个元素,需要在元素后添加逗号
tup2 = (20,)

print(type(tup2))

# 集合(Set)是一个无序不重复元素的序列

student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
# 输出集合,重复的元素会自动被去掉
print(student)

# 成员测试
if 'Rose' in student:
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)

# a和b的差集
print(a - b)

# a和b的并集
print(a | b)

# a和b的交集
print(a & b)

# a和b中同时存在的元素
print(a ^ b)

# 字典(Dictionary)
"""
字典是Python中另外一个非常有用的内置数据类型。
列表是有序的对象集合，字典是无序的对象集合。两者之间的区别是：字典中的元素是通过键存取的，而不是通过偏移存取。
字典是一种映射类型，字典用"{}"标识，它是一个无序的键(key):值(value)对集合。
键(key)必须使用不可变类型。
在同一个字典中，键(key)必须是唯一的。
"""

dict2 = {}
dict2['one'] = "1 - 菜鸟工具"
dict2[2] = "2 - 菜鸟教程"

tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

# 输出键为'one'的值
print(dict2['one'])
# 输出键为 2 的值
print(dict2[2])
# 输出完整的字典
print(tinydict)
# 输出所有键
print(tinydict.keys())
# 输出所有值
print(tinydict.values())

# 构造函数dict()可以直接从键值对序列中构建字典如下：
dict1 = ([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
print(dict1)

dict3 = dict(Runoob=1, Goole=2, Taobao=3)
print(dict3)

print("我叫%s今年%d岁!" % ('小明', 10))
