# -*- coding: utf-8 -*-
""" 
@Time    : 2021/2/7 11:42
@Author  : liufubin
@FileName: amihud.py
@description: 计算非流动性指标amihud
"""
import math


class Amihud(object):
    @staticmethod
    def amihud(daily_earnings, daily_turnover):
        """daily_earnings为日收益率，daily_turnover为日交易额"""
        amihud = -math.log(abs(daily_earnings)/abs(daily_turnover))
        return amihud


if __name__ == '__main__':
    daily_earnings_hushen = 0.0071558680556667136  # 2021年1月20号沪深300日收益率
    daily_turnover_shenshi = 518389.49  # 2021年1月20号深市日成交额
    daily_turnover_hushi = 396564.10  # 2021年1月20号沪市日成交额
    amihud_result = Amihud()
    print(amihud_result.amihud(daily_earnings_hushen, daily_turnover_shenshi))
    print(amihud_result.amihud(daily_earnings_hushen, daily_turnover_hushi))
    print(amihud_result.amihud(daily_earnings_hushen, daily_turnover_shenshi+daily_turnover_hushi))


