# -*- coding: utf-8 -*-
""" 
@Time    : 2020/11/14 16:09
@Author  : liufubin
@FileName: success_rate.py
@description: 胜率计算
"""


class SuccessRate(object):
    @staticmethod
    def success_rate(monthly_fund_field: list, benchmark_monthly: list):
        """计算胜率，需要月度收益和基准收益列表"""
        success_count = 0  # 跑赢基准收益计数
        for i in range(len(monthly_fund_field)):
            if monthly_fund_field[i] > benchmark_monthly[i]:
                success_count += 1
        success_rate = success_count/len(monthly_fund_field)
        return success_rate


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
    success_result = SuccessRate.success_rate(monthly_fund_field=monthly_fund, benchmark_monthly=benchmark_monthlys)
    print(success_result)
