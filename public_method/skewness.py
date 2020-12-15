# -*- coding: utf-8 -*-
""" 
@Time    : 2020/11/14 16:42
@Author  : liufubin
@FileName: skewness.py
@description: 偏度计算
"""
import numpy
import pandas
from public_method.standard_deviation import StandardDeviation


class Skewness(object):
    @staticmethod
    def skewness(month_fund_yield: list):
        """计算偏度，需要对应的基金月度收益率和标准差"""
        average_fund = numpy.average(month_fund_yield)   # 月度收益率平均值
        fund_difference_sum = 0   # 月度收益与平均值的差值的次方累加
        for i in range(len(month_fund_yield)):
            fund_difference_sum += pow((month_fund_yield[i] - average_fund), 3)
        standard_deviation = StandardDeviation.standard_deviation(month_earning_list=month_fund_yield)   # 计算的标准差
        skewness = (len(month_fund_yield)/((len(month_fund_yield) - 1) * (len(month_fund_yield) - 2))) *\
                   ((1/pow(standard_deviation, 3))*fund_difference_sum)
        return skewness

    @staticmethod
    def skewness_pandas(month_fund_yield: list):
        """使用pandas函数计算偏度，需要对应的基金月度收益率和标准差"""
        pandas_series = pandas.Series(month_fund_yield)
        skewness_pandas = pandas_series.skew()
        return skewness_pandas


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
    skewness_result = Skewness.skewness(month_fund_yield=monthly_fund)
    skewness_pandas_result = Skewness.skewness_pandas(month_fund_yield=monthly_fund)
    print(skewness_result)
    print(skewness_pandas_result)
