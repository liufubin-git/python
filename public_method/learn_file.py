# -*- coding: utf-8 -*-
""" 
@Time    : 2020/10/14 9:13
@Author  : liufubin
@FileName: learn_file.py
@description:
"""
a = 'ed'
c = a
b = 'ed'
print(c == b)  # 主要看value是否一致，值一致就返回true
print(a is b)  # 主要是看地址是否一致，id不一致返回false
print(id(b))
print(id(c))
