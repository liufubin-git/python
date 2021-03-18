# -*- coding: utf-8 -*-
""" 
@Time    : 2020/11/11 13:56
@Author  : liufubin
@FileName: downside_risk.py
@description: 下行风险计算
"""
import math


class DownsideRisk(object):
    @staticmethod
    def downside_risk(monthly_fund_field: list, risk_free: float, isannual=False):
        """计算下行风险，需要基金月度收益列表，无风险利率(取一年期定期存款利率/12)"""
        monthly_difference_sum = 0    # 收益减去无风险之后小于0的值平方累加
        for value in monthly_fund_field:
            if (value - risk_free/12) < 0:
                monthly_difference_sum += pow((value - risk_free/12), 2)
        downside_risk = math.sqrt(monthly_difference_sum/(len(monthly_fund_field) - 1))
        if isannual:
            downside_risk *= math.sqrt(12)  # 计算年化值
        return downside_risk


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
    downside_risk_result = DownsideRisk.downside_risk(monthly_fund_field=monthly_fund,
                                                      risk_free=risk_frees, isannual=True)
    print('下行风险计算结果：', downside_risk_result)
