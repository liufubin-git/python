# -*- coding: utf-8 -*-
""" 
@Time    : 2020/11/11 19:49
@Author  : liufubin
@FileName: maximum_retracement.py
@description: 最大回撤计算
"""
import random


class MaximumRetracement(object):
    @staticmethod
    def maxiunm_retracement(fund_net_value: list):
        """计算最大回撤，需要传入对应的净值--fund_net_value对应日频的净值"""
        retracement_list = []   # 回撤列表
        """以下是计算第二个数的回撤值    """
        retracement_list.append((fund_net_value[1] - fund_net_value[0])/fund_net_value[0])
        for i in range(1, (len(fund_net_value) - 1)):
            """从第三个数开始计算最大回撤"""
            retracement = fund_net_value[i+1] - max(fund_net_value[0:i])
            if retracement < 0:
                retracement_list.append(retracement/max(fund_net_value[0:i]))
        maxiunm_retracement = min(retracement_list)     # 回撤为负，所以直接取最小值即为最大回撤
        return -maxiunm_retracement, retracement_list

    @staticmethod
    def maxiunm_retracement_(min_fund, max_fund):
        return -(min_fund - max_fund)/max_fund


if __name__ == '__main__':
    num_list = []
    for i in range(100):
        num_list.append(random.randint(1, 100))
    print(num_list)
    maxiunm, list1 = MaximumRetracement.maxiunm_retracement(num_list)
    print(maxiunm)
    print(list1)
