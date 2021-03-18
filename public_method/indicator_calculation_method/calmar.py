# -*- coding: utf-8 -*-
""" 
@Time    : 2020/11/14 15:38
@Author  : liufubin
@FileName: calmar.py
@description: 卡玛比率计算
"""
from public_method.indicator_calculation_method.range_return_rate import RangeReturnRate
from public_method.indicator_calculation_method.maximum_retracement import MaximumRetracement


class Calmar(object):
    @staticmethod
    def calmar(startvalue, endvalue, fund_net_value, valuedates, max_fund=1, min_fund=1):
        """
        计算卡玛比率，需要基金年化收益，最大回撤，需要传入计算年化收益和最大回撤的参数
        组合大师计算回撤的净值是日净值，所以区间大的话，净值数据会很多
        """
        # annual_earnning = RangeReturnRate.annual_earnning_dates(startvalue=startvalue, endvalue=endvalue,
        #                                                         valuedates=valuedates, isannual=True)  # 计算基金年化收益
        annual_earnning = RangeReturnRate.annual_earnning_month(startvalue=startvalue, endvalue=endvalue,
                                                                month=valuedates, isannual=True)  # 计算基金年化收益
        maximum_retracement, retracement_list = MaximumRetracement.maxiunm_retracement(fund_net_value)  # 计算最大回撤
        # maximum_retracement = MaximumRetracement.maxiunm_retracement_(max_fund=max_fund,
        #                                                               min_fund=min_fund)  # 计算最大回撤

        calmar = annual_earnning/maximum_retracement
        return calmar


if __name__ == '__main__':
    start_fund = 0.681135
    end_fund = 1.229152
    years = 1

