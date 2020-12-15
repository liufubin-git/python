# -*- coding: utf-8 -*-
""" 
@Time    : 2020/11/11 15:42
@Author  : liufubin
@FileName: information_ratio.py
@description: 信息比率计算
"""
from public_method.track_error import TrackError
import math


class InformationRatio(object):
    @staticmethod
    def information_ratio(monthly_fund_field, benchmark_monthly, isannual=False):
        """计算信息比率，需要基金月度收益率，基准月度收益，超额收益标准差（跟踪误差）"""
        excess_earnning_sum = 0   # 超额收益累加
        for i in range(len(monthly_fund_field)):
            excess_earnning_sum += (monthly_fund_field[i] - benchmark_monthly[i])
        track_error = TrackError.track_error(monthly_fund_field, benchmark_monthly)  # 计算跟踪误差
        information_ratio = excess_earnning_sum/len(monthly_fund_field)/track_error
        if isannual:
            information_ratio *= math.sqrt(12)
        return information_ratio


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
    information_ratio_result = InformationRatio.information_ratio(monthly_fund_field=monthly_fund,
                                                                  benchmark_monthly=benchmark_monthlys, isannual=True)
    print('信息比率计算结果：', information_ratio_result)
