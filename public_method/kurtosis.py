# -*- coding: utf-8 -*-
""" 
@Time    : 2020/11/14 16:59
@Author  : liufubin
@FileName: kurtosis.py
@description: 峰度计算
"""
import numpy
import pandas
from public_method.standard_deviation import StandardDeviation


class Kurtosis(object):
    @staticmethod
    def kurtosis(month_fund_yield):
        """计算峰度，需要对应的基金月度收益率和标准差"""
        average_fund = numpy.average(month_fund_yield)   # 基金月度收益平均值
        fund_difference_sum = 0   # 公式中月度收益与平均值差的四次方累加值
        for i in range(len(month_fund_yield)):
            fund_difference_sum += pow((month_fund_yield[i] - average_fund), 4)
        standard_deviation = StandardDeviation.standard_deviation(month_fund_yield)   # 标准差计算
        month_len = len(month_fund_yield)
        kurtosis = ((month_len * (month_len + 1) * (fund_difference_sum/pow(standard_deviation, 4))) /
                    ((month_len - 1) * (month_len - 2) * (month_len - 3))) - (3 * pow((month_len - 1), 2)) /\
                   ((month_len - 2) * (month_len - 3))
        return kurtosis

    @staticmethod
    def kurtosis_pandas(month_fund_yield):
        """使用pandas计算峰度，需要对应的基金月度收益率"""
        pandas_series = pandas.Series(month_fund_yield)
        kurtosis_pandas = pandas_series.kurt()
        return kurtosis_pandas


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
    kurtosis_result = Kurtosis.kurtosis(month_fund_yield=monthly_fund)
    kurtosis_pandas_result = Kurtosis.kurtosis_pandas(month_fund_yield=monthly_fund)
    print(kurtosis_result)
    print(kurtosis_pandas_result)
