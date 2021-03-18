# -*- coding: utf-8 -*-
""" 
@Time    : 2020/11/11 19:12
@Author  : liufubin
@FileName: omega_ratio.py
@description: 欧米伽比率计算
"""
from public_method.indicator_calculation_method.range_return_rate import RangeReturnRate


class OmegaRtio(object):
    @staticmethod
    def lpm_1(monthly_fund_field: list, risk_free: float):
        """计算LMP1，需要传入基金月度收益率，无风险收益率（取一年期定期存款利率/12）"""
        monthly_difference_sum = 0  # 公式中累加的数
        for i in range(len(monthly_fund_field)):
            if (risk_free/12 - monthly_fund_field[i]) > 0:
                monthly_difference_sum += (risk_free/12 - monthly_fund_field[i])
        lpm1 = monthly_difference_sum / (len(monthly_fund_field) - 1)
        return lpm1

    @staticmethod
    def omega_ratio(startvalue, endvalue, valuedates, risk_free_year, monthly_fund_field):
        """计算欧米伽，需要年化收益率，需要传入始末净值和年数，需要年化无风险收益率，lpm3"""
        annual_earnning = RangeReturnRate.annual_earnning_dates(startvalue=startvalue,  # 计算的年化收益率
                                                          endvalue=endvalue, valuedates=valuedates)
        lpm1 = OmegaRtio.lpm_1(monthly_fund_field, risk_free_year)  # 计算lpm1
        omega_ratio = (annual_earnning - risk_free_year) / (lpm1 * 12) + 1
        return omega_ratio


if __name__ == '__main__':
    start_fund = 0.681135
    end_fund = 1.229152
    years = 1
    risk_frees = 0.015
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
    omega_result = OmegaRtio.omega_ratio(startvalue=start_fund, endvalue=end_fund,
                                         year=years, risk_free_year=risk_frees, monthly_fund_field=month_fund)
    print(omega_result)
