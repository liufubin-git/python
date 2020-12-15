# -*- coding: utf-8 -*-
""" 
@Time    : 2020/11/11 8:58
@Author  : liufubin
@FileName: uplink_capture.py
@description: 上行捕获率计算
"""
from public_method.upward_capture import UpwardCapture


class UplinkCapture(object):
    @staticmethod
    def ucr_x(benchmark_monthly: list):
        """ucr_x计算，需要传基金月度收益率列表和基准月度收益率列表"""
        i = 0
        product_sum = 1  # 计算公式中的括号中的累乘
        add_sum = 0  # 计算公式中的指数累加值
        for eary_month_benchmark in benchmark_monthly:
            if eary_month_benchmark >= 0:
                product_sum = product_sum * (benchmark_monthly[i] + 1)
                add_sum += 1
            i += 1
        ucr_x = pow(product_sum, 1 / add_sum) - 1
        return ucr_x

    @staticmethod
    def uplink_capture(monthly_fund_field: list, benchmark_monthly: list):
        """上行捕获率计算，上行捕获收益率(ucr_y)除以ucrx,计算需要传入基金月度收益率列表和基准月度收益率列表"""
        ucr_y = UpwardCapture.upward_capture(monthly_fund_field=monthly_fund_field, benchmark_monthly=benchmark_monthly)
        ucr_x = UplinkCapture.ucr_x(benchmark_monthly=benchmark_monthly)
        uplink_capture = ucr_y/ucr_x
        return uplink_capture


if __name__ == '__main__':
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
    uplink_capture_result = UplinkCapture.uplink_capture(monthly_fund_field=month_fund, benchmark_monthly=benchmark_monthlys)
    print(uplink_capture_result)
