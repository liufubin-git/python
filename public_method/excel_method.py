# -*- coding: utf-8 -*-
""" 
@Time    : 2020/11/12 18:13
@Author  : liufubin
@FileName: excel_method.py
@description: python操作excel公共方法
"""
import xlrd


class Excel(object):
        @staticmethod
        def get_excel(path, excel_name):
            # 打开excel文件，创建一个workbook对象,book对象也就是fruits.xlsx文件,表含有sheet名
            rbook = xlrd.open_workbook(path, excel_name)
            # sheets方法返回对象列表,[<xlrd.sheet.Sheet object at 0x103f147f0>]
            rbook.sheets()
            # xls默认有3个工作簿,Sheet1,Sheet2,Sheet3
            rsheet = rbook.sheet_by_index(0)  # 取第一个工作簿
            for row in rsheet.get_rows():
                product_column = row[1]
                product_column = product_column[1:]
            print(product_column)


if __name__ == '__main__':
    Excel().get_excel('E:\工作\金融知识', '基金指标计算.xlsx')
