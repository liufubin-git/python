# -*- coding: utf-8 -*-
""" 
@Time    : 2020/11/11 14:45
@Author  : liufubin
@FileName: treynor.py
@description: 特雷诺比率
"""
from public_method.indicator_calculation_method.range_return_rate import RangeReturnRate
from public_method.indicator_calculation_method.beta import Beta


class Treynor(object):
    @staticmethod
    def treynor(risk_free_year: float, monthly_fund_field: list, benchmark_monthly: list, startvalue, endvalue):
        """计算特雷诺比率，需要基金年化收益率，无风险收益率（取一年期定期存款利率）"""
        range_rate = RangeReturnRate.annual_earnning_dates(startvalue, endvalue)  # 计算区间收益，需要对应的区间始末净值
        beta = Beta.beta(monthly_fund_field, benchmark_monthly)                 # 计算贝塔，需要基金月度收益率，基准月度收益率
        treynor = (range_rate-risk_free_year)/beta
        return treynor


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
    treynor_result = Treynor.treynor(risk_free_year=risk_frees, monthly_fund_field=month_fund,
                                     benchmark_monthly=benchmark_monthlys, startvalue=start_fund,
                                     endvalue=end_fund)
    print(treynor_result)
