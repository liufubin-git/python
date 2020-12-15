# -*- coding: utf-8 -*-
""" 
@Time    : 2020/11/11 11:32
@Author  : liufubin
@FileName: sharpe.py
@description: 夏普比例计算
"""
from public_method.standard_deviation import StandardDeviation
import math


class Sharepe(object):
    @staticmethod
    def sharpe(monthly_fund_field: list, risk_free: float, isannual=False):
        """计算夏普比例，需要基金月度收益列表，无风险利率(取一年期定期存款利率/12)，月度收益率标准差"""
        income_difference_sum = 0  # 月度收益和无风险收益差值的累加
        for value in monthly_fund_field:
            income_difference_sum += (value - risk_free/12)
        standard_deviation = StandardDeviation.standard_deviation(monthly_fund_field)  # 计算标准差
        sharpe = (income_difference_sum/len(monthly_fund_field))/standard_deviation
        if isannual:
            sharpe *= math.sqrt(12)     # 年化夏普比率
        return sharpe


if __name__ == '__main__':
    monthly_fund = [  # 基金月度收益率列表
        0.050473107,
        0.032867281,
        0.08931831,
        0.021267266,
        0.060634109,
        -0.039898534,
        0.049669143,
        0.081554021,
        0.052515903,
        -0.001117565,
        0.141202937,
        0.077852734,
    ]
    risk_frees = 0.015
    sharp_result = Sharepe.sharpe(monthly_fund_field=monthly_fund, risk_free=risk_frees, isannual=True)
    print(sharp_result)
