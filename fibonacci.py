#!/usr/bin/python3
# -*- coding:utf-8 -*-


# Fibonacci series:斐波那契数列
# 两个元素的总和确定了下一个数

a, b = 0, 1
while b < 10:
    print(b, end=' ')
    a, b = b, a + b
