# -*- coding: utf-8 -*-
""" 
@Time    : 2020/11/11 9:37
@Author  : liufubin
@FileName: downward_capture.py
@description: 下行捕获收益率计算
"""


class DownwardCapture(object):
    @staticmethod
    def downward_capture(monthly_fund_field: list, benchmark_monthly: list):
        """下行捕获收益率计算，需要传基金月度收益率列表和基准月度收益率列表"""
        i = 0
        product_sum = 1   # 计算公式中的括号中的累乘
        add_sum = 0       # 计算公式中的指数累加值
        for eary_month_benchmark in benchmark_monthly:
            if eary_month_benchmark < 0:    # 与上行捕获率相反，基准收益小于0才计算
                product_sum *= (monthly_fund_field[i] + 1)
                add_sum += 1
            i += 1
        dcr_y = pow(product_sum, 1/add_sum) - 1
        return dcr_y


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
    downward_capture = DownwardCapture.downward_capture(monthly_fund_field=monthly_fund,
                                                        benchmark_monthly=benchmark_monthlys)
    print('下行捕获收益率计算结果为：', downward_capture)
