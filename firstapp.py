# /usr/bin/python3
# -*- coding: utf-8 -*-


# Python关键字
import keyword

print(keyword.kwlist)

# Python注释

# 这是一个当行注释
print("Hello,Python!")  # 第二个注释

'''
第三个注释
第四个注释
'''

"""
第五个注释
第六个注释
"""

# 数字(Number)类型
"""
int(整数)
bool(布尔)
float(浮点数)
complex(复数)
"""

# 字符串(String)
"""
python中单引号和双引号使用完全相同
使用三引号('''和\"\"\")可以指定一个多行字符串
转义符'\'
反斜杠可以用来转义，使用r可以让反斜杠不发生转义。。 如 r"this is a line with \n" 则\n会显示，并不是换行。
按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。
字符串可以用 + 运算符连接在一起，用 * 运算符重复。
Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
Python中的字符串不能改变。
Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
字符串的截取的语法格式如下：变量[头下标:尾下标]
"""

word = '字符串'
sentence = "这是一个句子"
paragraph = """这是一个段落,
可以由多行组成"""

string = 'Runoob'

# 输出字符串
print(string)
# 输出第一个到倒数第二个的所有字符
print(string[0:-1])
# 输出字符串第一个字符
print(string[0])
# 输出从第三个开始的后所有字符
print(string[2:5])
# 输出从第三个开始的后所有字符
print(string[2:])
# 输出字符串两次
print(string * 2)
# 连接字符串
print(string + '你好')

# 空行
"""
函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。
类和函数入口之间也用一行空行分隔，以突出函数入口的开始。
空行与代码缩进不同，空行并不是Python语法的一部分。
书写时不插入空行，Python解释器运行也不会出错。但是空行的作用在
于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。
记住：空行也是程序代码的一部分。
"""

# 等待用户输入
# input("\n\n>>> 按下 ENTER 键后退出 <<<")

# Print输出
# print默认输出是换行的,如果要实现不换行是需要在变量尾部加上end=""

x = "a"
y = "b"
# 换行输出
print(x)
print(y)

print('-------------')
# 不换行输出
print(x, end=" ")
print(y, end="")
print()

# import与from...import
"""
在Python用import或者from...import来导入相应的模块。
将整个模块(somemodule)导入,格式为:import somemodule
将某个模块中导入某个函数,格式为:from somemodule import somefuction
将某个模块中导入多个函数,格式为:from somemodule import firstfunc,secondfunc
将某个模块中的全部函数导入,格式为:from somemodule import *
"""

import sys

print('======= Python import code ======')
print('命令行参数为:')
for i in sys.argv:
    print(i)
print('\n Python路径为', sys.path)
