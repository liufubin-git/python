# -*- coding: utf-8 -*-
""" 
@Time    : 2020/11/10 18:22
@Author  : liufubin
@FileName: standard_deviation.py
@description: 标准差计算公式
"""
import math
from public_method.connect_mysql import ConnectMysql
import numpy


class StandardDeviation(object):
    """
    标准差计算公式，先计算月平均收益，然后每月与月平均相减再开平方之后用作分母，最后除以月份减一再开根号
    传参没有固定具体的时间，想要计算多久的，需要把这个时间段的月度收益放到list中，再请求函数
    """
    @staticmethod
    def standard_deviation(month_earning_list: list, is_annual=False):
        sum_pow = 0               # 计算公式中的根号里面的分母，累加
        if month_earning_list is None:
            return None
        avg_month_earnning = numpy.average(month_earning_list)  # 月平均收益
        for values in month_earning_list:
            sum_pow += pow((values - avg_month_earnning), 2)  # 结果为公式的分母
        standard_deviation = math.sqrt(sum_pow/(len(month_earning_list) - 1))  # 最后返回标准差
        if is_annual:
            standard_deviation *= math.sqrt(12)
        return standard_deviation

    # @staticmethod
    # def standard_deviation_std(month_earning_list: list, is_annual=False):
    #     """使用numpy中的std函数计算标准差"""
    #     month_earning_list = numpy.array(month_earning_list)
    #     standard_deviation = numpy.std(month_earning_list)
    #     if is_annual:
    #         return standard_deviation * math.sqrt(12)
    #     else:
    #         return standard_deviation

    @staticmethod
    def get_month_earnning(starttime, endtime):
        """根据开始和结束时间，从数据库中获取月度收益的list"""
        sql = ""
        sql_result = ConnectMysql().fetchall(sql=sql)
        print(sql_result)
        return sql_result


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
    stock_applies = [
        0.7229,
        0.2415,
        -0.241,
        1.9656,
        -1.6908,
        -0.9569,
        0.2398,
        0.4819,
        0.7177,
        0,
        0,
        1.4563,
        0,
        -0.9615,
        0,
        0.241,
        -0.4796,
        0,
        0.7246,
        0,
        0.2421,
        1.2255,
        0.2445,
        1.4888,
        -0.4938,
        -2.1739,
        1.7199,
        -0.245,
        -1.4493,
        0.2421
    ]
    print(len(stock_applies))
    print(stock_applies)
    stock_applies_100 = []
    for i in stock_applies:
        stock_applies_100.append(i/100)
    # standard_result = StandardDeviation.standard_deviation(month_earning_list=monthly_fund, is_annual=False)
    # print(standard_result)
    standard_result = StandardDeviation.standard_deviation(month_earning_list=stock_applies, is_annual=False)
    standard_result_100 = StandardDeviation.standard_deviation(month_earning_list=stock_applies_100, is_annual=False)
    print(math.sqrt(numpy.var(stock_applies_100)))
    print(stock_applies_100)
    print(standard_result)
    print(standard_result_100)
