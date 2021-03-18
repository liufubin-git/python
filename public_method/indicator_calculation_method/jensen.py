# -*- coding: utf-8 -*-
""" 
@Time    : 2020/11/14 15:49
@Author  : liufubin
@FileName: jensen.py
@description: 詹森指数计算
"""
import numpy
from public_method.indicator_calculation_method.beta import Beta


class Jensen(object):
    @staticmethod
    def jensern(monthly_fund_field: list, benchmark_monthly: list, risk_free: float, isannual=False):
        """计算詹森指数，需要基金月度收益和基准月度收益列表，无风险收益率"""
        average_fund = numpy.average(monthly_fund_field)   # 基金月度收益平均值
        average_benchmark = numpy.average(benchmark_monthly)  # 基准月度收益平均值
        beta = Beta.beta(monthly_fund_field, benchmark_monthly)  # 贝塔
        jensen = average_fund - risk_free/12 - beta * (average_benchmark - risk_free/12)
        if isannual:
            jensen *= 12
        return jensen


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
    benchmark_monthlys = [  # 基准月度收益率列表
        0.053941974,
        0.002554274,
        -0.009327054,
        0.003932507,
        0.018933849,
        -0.014943403,
        0.069975072,
        -0.022623933,
        -0.015947571,
        -0.064439227,
        0.061425006,
        -0.011642965
    ]
    risk_frees = 0.015
    jensen_result = Jensen.jensern(monthly_fund_field=monthly_fund, benchmark_monthly=benchmark_monthlys,
                                   risk_free=risk_frees, isannual=True)
    print('詹森指数计算结果：', jensen_result)
