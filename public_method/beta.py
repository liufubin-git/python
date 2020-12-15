# -*- coding: utf-8 -*-
""" 
@Time    : 2020/11/11 10:02
@Author  : liufubin
@FileName: beta.py
@description: 计算贝塔
"""


class Beta(object):
    @staticmethod
    def beta(monthly_fund_field: list, benchmark_monthly: list):
        """计算贝塔，需要传入基金月度收益率列表和基准月度收益率列表"""
        product_cumulative = 0     # 基金月度收益与基准乘积累加
        fund_cumulative = 0        # 基金累加
        benchmark_cumulative = 0   # 基准累加
        benchmark_square_cumulative = 0     # 基准平方累加
        for i in range(len(benchmark_monthly)):    # 直接取的基准的列表个数做循环次数，所以要保持两个列表数量一致且时间对上。
            product_cumulative += monthly_fund_field[i] * benchmark_monthly[i]
            fund_cumulative += monthly_fund_field[i]
            benchmark_cumulative += benchmark_monthly[i]
            benchmark_square_cumulative += pow(benchmark_monthly[i], 2)
        beta = (product_cumulative - fund_cumulative * benchmark_cumulative/len(benchmark_monthly)) / \
               (benchmark_square_cumulative - pow(benchmark_cumulative, 2)/len(benchmark_monthly))
        return beta


if __name__ == '__main__':
    monthly_fund = [                # 基金月度收益率列表
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
    benchmark_monthlys = [         # 基准月度收益率列表
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
    beta_result = Beta.beta(monthly_fund_field=monthly_fund, benchmark_monthly=benchmark_monthlys)
    print('贝塔计算结果：', beta_result)
