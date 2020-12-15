# -*- coding: utf-8 -*-
""" 
@Time    : 2020/11/11 8:38
@Author  : liufubin
@FileName: filter_null_none.py
@description: 过滤列表中的None值与空值
"""


class FilteNone(object):
    """过滤列表中的空值与None值"""
    @staticmethod
    def filter_none(filter_list: list):
        filter_list = filter(None, filter_list)
        return list(filter_list)       # python3中，返回的是迭代器对象，需要转化成list类型返回


if __name__ == '__main__':
    filter_list1 = ['', None, '888', 4897, None, '']
    filter_result = FilteNone().filter_none(filter_list1)
    print(filter_result)
    print('555')
