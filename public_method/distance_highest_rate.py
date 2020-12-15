# -*- coding: utf-8 -*-
""" 
@Time    : 2020/11/14 17:13
@Author  : liufubin
@FileName: distance_highest_rate.py
@description: 距最高净值比
"""


class DistanceHighestRate(object):
    @staticmethod
    def distance_highest_rate(fund_daily_rate: list):
        """计算距最高净值比，需要传入日频率净值"""
        distance_highest_rate = (max(fund_daily_rate) - fund_daily_rate[(len(fund_daily_rate) - 1)]) / \
                                (fund_daily_rate[(len(fund_daily_rate) - 1)])
        return distance_highest_rate


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
    distance_highest_result = DistanceHighestRate.distance_highest_rate(fund_daily_rate=monthly_fund)
    print('据最高净值比', distance_highest_result)
