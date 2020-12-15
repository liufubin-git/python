# -*- coding: utf-8 -*-
""" 
@Time    : 2020/11/11 14:20
@Author  : liufubin
@FileName: sotino_ratio.py
@description: 索提诺比率计算
"""
from public_method.downside_risk import DownsideRisk
import math


class SotinoRatio(object):
    @staticmethod
    def sotio_ratio(monthly_fund_field: list, risk_free: float, isannual=False):
        """计算索提诺比率，需要基金月度收益列表，无风险利率(取一年期定期存款利率/12)，月度收益率的下行风险"""
        monthly_difference_sum = 0    # 月度收益与无风险收益的差值累加
        for value in monthly_fund_field:
            monthly_difference_sum += (value - risk_free/12)
        downside_risk = DownsideRisk.downside_risk(monthly_fund_field, risk_free)  # 计算下行风险
        sotino_ratio = (monthly_difference_sum/len(monthly_fund_field))/downside_risk
        if isannual:
            sotino_ratio *= math.sqrt(12)  # 计算年化
        return sotino_ratio


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
    sotino_result = SotinoRatio.sotio_ratio(monthly_fund_field=monthly_fund, risk_free=risk_frees, isannual=True)
    print(sotino_result)
