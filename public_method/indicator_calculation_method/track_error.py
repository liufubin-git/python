# -*- coding: utf-8 -*-
""" 
@Time    : 2020/11/11 16:37
@Author  : liufubin
@FileName: track_error.py
@description: 跟踪误差计算
"""
from public_method.indicator_calculation_method.standard_deviation import StandardDeviation
import math


class TrackError(object):
    @staticmethod
    def track_error(monthly_fund_field, benchmark_monthly, isannual=False):
        """计算跟踪误差，需要基金月度收益率，基准月度收益，是否年化"""
        excess_earnning_list = []   # 基金月度收益率与基准月度收益率差值列表
        for i in range(len(monthly_fund_field)):
            excess_earnning_monthly = monthly_fund_field[i] - benchmark_monthly[i]
            excess_earnning_list.append(excess_earnning_monthly)
        track_error = StandardDeviation.standard_deviation(excess_earnning_list)  # 调用计算标准差方法
        if isannual:  # 年度化
            track_error *= math.sqrt(12)
        return track_error


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
    track_error_result = TrackError.track_error(monthly_fund_field=monthly_fund,
                                                benchmark_monthly=benchmark_monthlys, isannual=True)
    print('跟踪误差计算结果：', track_error_result)
