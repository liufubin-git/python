# -*- coding: utf-8 -*-
""" 
@Time    : 2020/11/2 11:00
@Author  : liufubin
@FileName: range_return_rate.py
@description: 区间收益率计算
"""


class RangeReturnRate(object):
    @staticmethod
    def annual_earnning_dates(startvalue, endvalue, isannual=False, valuedates=365):
        """计算区间收益率，需要传传入区间初和末期的净值，valuedates为净值区间的天数"""
        range_rate = (endvalue - startvalue)/startvalue  # 计算的区间收益
        if isannual:
            range_rate = pow(1+range_rate, 365.25/valuedates)-1      # 日频的年化收益计算方法
        return range_rate

    @staticmethod
    def annual_earnning_month(startvalue, endvalue, isannual=False, month=12):
        """计算区间收益率，需要传传入区间初和末期的净值，valuedates为净值区间的天数"""
        range_rate = (endvalue - startvalue) / startvalue  # 计算的区间收益
        if isannual:
            range_rate = pow(1 + range_rate, 12 / month) - 1  # 日频的年化收益计算方法
        return range_rate

    @staticmethod
    def annual_earnning_yesrs(startvalue, endvalue, isannual=False, yesrs=1):
        """计算区间收益率，需要传传入区间初和末期的净值，valuedates为净值区间的天数"""
        range_rate = (endvalue - startvalue)/startvalue  # 计算的区间收益
        if isannual:
            range_rate = pow(1+range_rate, 1/yesrs)-1      # 年频率的年化收益计算方法
        return range_rate


if __name__ == '__main__':
    result = RangeReturnRate.annual_earnning_dates(startvalue=0.680172, endvalue=1.229152, valuedates=362, isannual=True)
    print(result)
