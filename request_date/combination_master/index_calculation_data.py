# -*- coding: utf-8 -*-
""" 
@Time    : 2020/12/2 17:49
@Author  : liufubin
@FileName: index_calculation_data.py
@description: 指标计算参数
"""


class InvestmentCertificateBiomedical(object):
    """招商国证生物医药指数数据--时间为2019-06-01~2020-05-31"""
    start_fund = 0.681135  # 净值开始值
    end_fund = 1.229152    # 净值结束值
    date_start_fund = 0.680172  # 日净值开始值
    date_end_fund = 1.229152    # 日净值结束值
    years = 1
    risk_frees = 0.015   # 无风险收益率
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
