# -*- coding: utf-8 -*-
""" 
@Time    : 2021/3/24 15:50
@Author  : liufubin
@FileName: test_variety_revenue_contribution.py
@description:品种收益贡献计算测试用例
"""
from public_method.connect_mysql import ConnectMysql


class TestVarietyRevenueContribution(object):
    def test_unwind_profit_and_loss(self):
        """平仓盈亏计算"""
        start_time = '20200801'
        end_time = '20200831'
        fund_id = 'CF0000003J'  # 产品id，用来查找对应的账户
        productname = '白银'  # 品种名称，用来查找品种id
        unwind_profit_and_loss = 0  # 平仓盈亏累加
        connet_mysql = ConnectMysql(host='202.104.102.166', user='ppw_gtjaqh_user',
                                    password='IJU^T!yv0vbWwJXh', port=3306)
        unwind_sql = "SELECT closeprlsm FROM ppw_gtjaqh.cm_gj_future_trade_data WHERE posiact IN ('C','T') AND " \
                     "assetacc = (SELECT assetacc FROM ppw_gtjaqh.`cm_fund_future_account_map` WHERE fund_id = " \
                     "'{}') AND productcode = (SELECT productcode FROM ppw_gtjaqh.`cm_gj_future_product` " \
                     "WHERE productname = '{}')AND tradingday BETWEEN {} AND  {} ".format(fund_id, productname,
                                                                                          start_time, end_time)
        print(unwind_sql)
        unwind_sql_result = connet_mysql.fetchall(unwind_sql)
        print(unwind_sql_result)
        for i in unwind_sql_result:
            unwind_profit_and_loss += float(i[0])
        return unwind_profit_and_loss

    def test_position_profit_and_loss(self):
        """持仓盈亏计算"""
        fund_id = 'CF0000003J'  # 产品id，用来查找对应的账户
        productname = '白银'  # 品种名称，用来查找品种id
        position_profit_and_loss = 0  # 平仓盈亏累加
        connet_mysql = ConnectMysql(host='202.104.102.166', user='ppw_gtjaqh_user',
                                    password='IJU^T!yv0vbWwJXh', port=3306)
        unwind_sql = "SELECT holdprlsm FROM ppw_gtjaqh.`cm_gj_future_trade_hold` WHERE assetacc = (SELECT assetacc " \
                     "FROM ppw_gtjaqh.`cm_fund_future_account_map` WHERE fund_id = '{}')   AND productcode = " \
                     "(SELECT productcode FROM ppw_gtjaqh.`cm_gj_future_product` WHERE productname = '{}') " \
            .format(fund_id, productname)
        print(unwind_sql)
        unwind_sql_result = connet_mysql.fetchall(unwind_sql)
        print(unwind_sql_result)
        for i in unwind_sql_result:
            position_profit_and_loss += float(i[0])
        return position_profit_and_loss

    def test_transaction_costs(self):
        """交易费用计算"""
        start_time = '20200801'
        end_time = '20200831'
        fund_id = 'CF0000003J'  # 产品id，用来查找对应的账户
        productname = '白银'  # 品种名称，用来查找品种id
        transaction_costs = 0  # 平仓盈亏累加
        connet_mysql = ConnectMysql(host='202.104.102.166', user='ppw_gtjaqh_user',
                                    password='IJU^T!yv0vbWwJXh', port=3306)
        transaction_costs_sql = "SELECT trdchrg FROM ppw_gtjaqh.cm_gj_future_trade_data  where " \
                                "assetacc = (SELECT assetacc FROM ppw_gtjaqh.`cm_fund_future_account_map` WHERE " \
                                "fund_id = '{}') AND productcode = (SELECT productcode FROM " \
                                "ppw_gtjaqh.`cm_gj_future_product` WHERE productname = '{}')AND tradingday BETWEEN {} " \
                                "AND  {} ".format(fund_id, productname, start_time, end_time)
        print(transaction_costs_sql)
        unwind_sql_result = connet_mysql.fetchall(transaction_costs_sql)
        print(unwind_sql_result)
        for i in unwind_sql_result:
            transaction_costs += float(i[0])
        return transaction_costs


if __name__ == '__main__':
    unwind_profit_and_loss_ = TestVarietyRevenueContribution().test_unwind_profit_and_loss()
    print('平仓盈亏计算结果：', unwind_profit_and_loss_)
    position_profit_and_loss_ = TestVarietyRevenueContribution().test_position_profit_and_loss()
    print('持仓盈亏计算结果：', position_profit_and_loss_)
    transaction_costs_ = TestVarietyRevenueContribution().test_transaction_costs()
    print('交易费用计算结果：', transaction_costs_)
    sum_profit = unwind_profit_and_loss_ + position_profit_and_loss_ - transaction_costs_
    print('品种实际收益：', sum_profit)
