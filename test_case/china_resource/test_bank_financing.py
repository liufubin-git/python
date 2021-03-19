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
        计算银行理财赎回的份额对应的成本，传入参数见下面方法注释
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

    @staticmethod
    def test_redemption_amount(redemption, purchase, net_redemption):
        """
        redemption传入的赎回信息，信息格式为:
        redemption_ = {           # 传入的赎回信息，包含赎回的方式，赎回的份额
                'specified': {       # 指定赎回，key为specified， value为dict并且key为赎回对应的时间，value为份数
                    '2020-08-30': 100,
                    '2020-07-22': 50,
                },
                'first_in_first_out': 200   # 先进先出赎回，key为first_in_first_out， value为赎回的份数
            }
        purchase为传入的申购信息，信息格式为：
        purchase_ = {             # 传入所有的申购信息，包含申购时间，申购对应的金额，申购对应的单位净值
        '2020-06-10': [300, 1.025],
        '2020-07-22': [200, 1.036],
        '2020-08-30': [400, 1.040]
        }
        net_redemption为传入的赎回日期和净值，格式为：
        net_redemption_ = ['2020-09-30', 1.050]  # 赎回的日期和对应的净值
        计算对应当日赎回的收益和收益率，赎回当日总的赎回份额 * 赎回当日的净值
        需要传入赎回信息和赎回日的净值, 传入申购信息用以计算陈本
        """
        redeem_shares = 0   # 赎回份额
        if 'specified' in redemption.keys():
            for key1, value1 in redemption['specified']:
                redeem_shares += value1
        if 'first_in_first_out' in redemption.keys():
            redeem_shares += redemption['first_in_first_out']
        redemption_amount = redeem_shares * net_redemption    # 赎回的收益
        redemption_costs = TestBankFinancing.test_redemption_costs(purchase, redemption)   # 赎回的份额对应的成本
        redemption_amount_ratio = (redemption_amount-redemption_costs)/redemption_costs  # 计算的收益率
        return redemption_amount, redemption_amount_ratio

    @staticmethod
    def test_net_fee_before_copies(thousands_of_income, revious_net_value, dates):
        """
        计算费前净值,基于万份收益的方法,需要传入对应的万份收益和上一个单位净值,初始净值到现在的天数
        thousands_of_income为万份收益，revious_net_value为上一个单位净值， dates为始净值到现在的天数（t日）
        """
        daily_rate = (thousands_of_income/10000)/revious_net_value  # 每日收益率
        net_fee_before = 1
        for i in range(dates):
            net_fee_before *= (1+daily_rate)
        return net_fee_before


if __name__ == '__main__':
    purchase_ = {             # 传入所有的申购信息，包含申购时间，申购对应的金额，申购对应的单位净值
        '2020-06-10': [300, 1.025],
        '2020-07-22': [200, 1.036],
        '2020-08-30': [400, 1.040]
    }
    redemption_ = {           # 传入的赎回信息，包含赎回的方式，赎回的份额
        'specified': {       # 指定赎回，key为specified， value为dict并且key为赎回对应的时间，value为份数
            '2020-08-30': 100,
            '2020-07-22': 50,
        },
        'first_in_first_out': 200   # 先进先出赎回，key为first_in_first_out， value为赎回的份数
    }
    net_redemption_ = ['2020-09-30', 1.050]  # 赎回的日期和对应的净值
