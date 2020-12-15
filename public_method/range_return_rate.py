# -*- coding: utf-8 -*-
""" 
@Time    : 2020/11/2 11:00
@Author  : liufubin
@FileName: range_return_rate.py
@description: 区间收益率计算
"""


class RangeReturnRate(object):
    @staticmethod
    def annual_earnning(startvalue, endvalue, isannual=False, years=1):
        """计算区间收益率，需要传传入区间初和末期的净值，年化收益率，把当前区间收益换算成年度的收益，非实际收益"""
        range_rate = (endvalue - startvalue)/startvalue  # 计算的区间收益
        if isannual:
            range_rate = pow(1+range_rate, 1/years)-1      # range_rate为区间收益，可用上面的函数返回，years为对应的年化收益的年数
        return range_rate


if __name__ == '__main__':
    result = RangeReturnRate.annual_earnning(0.681135, 1.229152)
    print(result)
