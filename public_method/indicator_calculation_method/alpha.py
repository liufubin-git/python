# -*- coding: utf-8 -*-
""" 
@Time    : 2020/11/11 10:33
@Author  : liufubin
@FileName: alpha.py
@description: 阿尔法的计算
"""
from public_method.indicator_calculation_method.beta import Beta
import numpy


class Alpha(object):
    @staticmethod
    def alpha(monthly_fund_field: list, benchmark_monthly: list, isannual=False):
        """计算贝塔，需要传入基金月度收益率列表和基准月度收益率列表, 需要贝塔的值"""
        beta = Beta.beta(monthly_fund_field, benchmark_monthly)   # 计算的beta值
        average_fund = numpy.average(monthly_fund_field)          # 基金月度收益平均值
        average_benchmark = numpy.average(benchmark_monthly)      # 基准月度收益平均值
        alpha = average_fund - beta * average_benchmark
        if isannual:
            alpha *= 12
        return alpha


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
    alpha_result = Alpha.alpha(monthly_fund_field=monthly_fund, benchmark_monthly=benchmark_monthlys, isannual=True)
    print('阿尔法计算结果：', alpha_result)
