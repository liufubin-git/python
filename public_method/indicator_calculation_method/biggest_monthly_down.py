# -*- coding: utf-8 -*-
""" 
@Time    : 2020/11/14 17:25
@Author  : liufubin
@FileName: biggest_monthly_down.py
@description: 下跌相关指标
"""


class BiggesrMonthlyDown(object):
    @staticmethod
    def biggest_monthly_down(month_fund_yield: list):
        """计算当月最大下跌,需要传入基金月度收益"""
        down_min = min(month_fund_yield)               # 当月最大下跌
        return down_min

    @staticmethod
    def down_month_ratio(month_fund_yield: list):
        """计算下跌月份比，需要传入基金月度收益"""
        count_down = 0  # 下跌月份计数
        for i in range(len(month_fund_yield)):
            if month_fund_yield[i] < 0:
                count_down += 1
        down_rate = count_down / len(month_fund_yield)  # 下跌月份比
        return down_rate

    @staticmethod
    def batting_average(monthly_fund_field: list, benchmark_monthly: list):
        """跑赢指数月份比计算，需要传入基金月度收益率列表和基准月度收益率列表"""
        count_win = 0    # 跑赢指数月份计数
        for i in range(len(monthly_fund_field)):
            if monthly_fund_field[i] >= benchmark_monthly[i]:
                count_win += 1
        batting_average = count_win/len(monthly_fund_field)
        return batting_average

    @staticmethod
    def profit_loss_ratio(monthly_fund_field: list):
        """计算盈利亏损比，需要传入基金月度收益列表"""
        profit_sum = 0
        loss_sum = 0
        for i in range(len(monthly_fund_field)):
            if monthly_fund_field[i] > 0:
                profit_sum += 1
            else:
                loss_sum += 1
        if loss_sum == 0:
            return profit_sum
        else:
            return -profit_sum/loss_sum


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
    down_min_result = BiggesrMonthlyDown.biggest_monthly_down(month_fund_yield=monthly_fund)
    down_rate_result = BiggesrMonthlyDown.down_month_ratio(month_fund_yield=monthly_fund)
    batting_average_result = BiggesrMonthlyDown.batting_average(monthly_fund_field=monthly_fund,
                                                                benchmark_monthly=benchmark_monthlys)
    prolit_loss_result = BiggesrMonthlyDown.profit_loss_ratio(monthly_fund_field=monthly_fund)
    print('当月最大下跌', down_min_result)
    print('下跌月份比', down_rate_result)
    print('跑赢指数月份比', batting_average_result)
    print('盈利亏损比：', prolit_loss_result)
