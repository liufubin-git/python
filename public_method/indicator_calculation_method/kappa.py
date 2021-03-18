# -*- coding: utf-8 -*-
""" 
@Time    : 2020/11/11 18:50
@Author  : liufubin
@FileName: kappa.py
@description: 卡帕比率计算
"""
from public_method.indicator_calculation_method.range_return_rate import RangeReturnRate


class Kappa(object):

    @staticmethod
    def lpm_3(monthly_fund_field: list, risk_free: float):
        """计算LMP3，需要传入基金月度收益率，无风险收益率（取一年期定期存款利率/12）"""
        monthly_difference_sum = 0  # 公式中累加的数
        for i in range(len(monthly_fund_field)):
            if (risk_free/12 - monthly_fund_field[i]) > 0:
                monthly_difference_sum += pow((risk_free/12 - monthly_fund_field[i]), 3)
        lpm3 = monthly_difference_sum/(len(monthly_fund_field) - 1)
        return lpm3

    @staticmethod
    def kappa(startvalue, endvalue, yesrs, monthly_fund_field, risk_free, isannual=True):
        """计算卡帕，需要年化收益率，需要传入始末净值和净值总天数，需要年化无风险收益率，lpm3"""
        annual_earnning = RangeReturnRate.annual_earnning_yesrs(startvalue=startvalue,  # 计算年化收益
                                                                endvalue=endvalue, isannual=isannual, yesrs=yesrs)
        lpm3 = Kappa.lpm_3(monthly_fund_field, risk_free)
        kappa = (annual_earnning - risk_free)/(pow((lpm3 * 12), 1/3))
        print(kappa)
        return kappa


if __name__ == '__main__':
    start_fund = 0.681135
    end_fund = 1.229152
    years = 1
    risk_frees = 0.015  # 无风险收益率1.5%
    month_fund = [  # 基金月度收益率列表
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
    kappa_result = Kappa.kappa(startvalue=start_fund, endvalue=end_fund, year=years,
                               monthly_fund_field=month_fund, risk_free=risk_frees, isannual=True)
    print('卡帕计算结果：', kappa_result)
