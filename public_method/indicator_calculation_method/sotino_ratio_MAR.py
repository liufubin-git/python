# -*- coding: utf-8 -*-
""" 
@Time    : 2020/11/11 17:38
@Author  : liufubin
@FileName: sotino_ratio_MAR.py
@description: 索提诺比率（MAR）
"""
from public_method.indicator_calculation_method.downside_risk import DownsideRisk
import math


class SotioRatioMar(object):
    @staticmethod
    def sotio_ratio_mar(monthly_fund_field: list, risk_free: float, isannual=False):
        """计算索提诺比率，需要基金月度收益列表，无风险利率(取一年期定期存款利率/12)，月度收益率的下行风险"""
        monthly_fund_min = min(monthly_fund_field)  # 最小月度收益率
        monthly_fund_sum = 0    # 月度收益与最小月度收益差值的累加
        for i in range(len(monthly_fund_field)):
            monthly_fund_sum += (monthly_fund_field[i] - monthly_fund_min)
        downside_risk = DownsideRisk.downside_risk(monthly_fund_field, risk_free)   # 月度收益率下行风险
        sotino_ratio_mar = monthly_fund_sum/(len(monthly_fund_field) * downside_risk)
        if isannual:
            sotino_ratio_mar *= math.sqrt(12)
        return sotino_ratio_mar


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
    sotio_result = SotioRatioMar.sotio_ratio_mar(monthly_fund_field=monthly_fund, risk_free=risk_frees,isannual=True)
    print(sotio_result)
