# -*- coding: utf-8 -*-
""" 
@Time    : 2021/3/18 10:35
@Author  : liufubin
@FileName: test_bank_financing.py
@description: 国君期货银行理财日收益计算测试用例
"""


class TestBankFinancing(object):
    @staticmethod
    def test_redemption_costs(purchase, redemption):
        """
        计算银行理财日收益需要先计算成本，考虑两种赎回方式：先进先出，指定赎回
        申购是对应的金额，赎回是份额，所以需要传入申购的时间和金额和对应的单位净值(数据格式为dict，key为时间，value为list，对应的金额和净值)
        需要传入对应的赎回方式，优先指定赎回，然后再先进先出。指定赎回需要传入赎回的时间和赎回的份数，先进先出要传入赎回的份数
        """
        cost_total = 0     # 成本总和
        # 计算指定赎回的成本
        if 'specified' in redemption.keys():
            for key1, value1 in redemption['specified'].items():
                # 首先把指定赎回的份数在赎回字典中移除
                purchase[key1][0] = ((purchase[key1][0] * purchase[key1][1]) - value1)/purchase[key1][1]
                # 计算指定赎回日期的成本
                cost_total += value1 * purchase[key1][1]
        # 计算先进先出的成本
        if 'first_in_first_out' in redemption.keys():
            for key2, value2 in purchase.items():
                # 循环判断是不是够扣，如果够扣，就计算指定赎回的成本
                if value2[0] >= redemption['first_in_first_out']:
                    cost_total += redemption['first_in_first_out'] * value2[1]
                    break
                # 如果不够扣，就先把这个日期的所以申购都算成本，再循环看下一个申购日期的成本进行累加
                else:
                    cost_total += value2[0] * value2[1]
                    redemption['first_in_first_out'] -= value2[0]  # 计算一次需要减去已经计算的那个份额
                    continue
        return cost_total


if __name__ == '__main__':
    purchase_ = {             # 传入所有的申购信息，包含申购时间，申购对应的金额，申购对应的单位净值
        '2020-06-10': [300, 1.025],
        '2020-07-22': [200, 1.036],
        '2020-08-30': [400, 1.040]
    }
    redemption_ = {           # 传入的赎回信息，包含赎回的方式，赎回的份数
        'specified': {       # 指定赎回，key为specified， value为dict并且key为赎回对应的时间，value为份数
            '2020-08-30': 100,
            '2020-07-22': 50,
        },
        'first_in_first_out': 200   # 先进先出赎回，key为first_in_first_out， value为赎回的份数
    }
    net_redemption = ['2020-09-30', 1.050]  # 赎回的日期和对应的净值
