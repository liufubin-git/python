# -*- coding: utf-8 -*-
""" 
@Time    : 2021/3/24 15:13
@Author  : liufubin
@FileName: test_rolling_difference_value.py
@description: 国君证券计算轧差市值测试用例
"""
from public_method.connect_mysql import ConnectMysql


class TestRollingDifferenceValue(object):
    def test_bull_market_value(self):
        """计算多头市值"""
        bull_market = 0
        open_time = '20200513'   # 持仓日期
        fund_id = 'CF0000003J'   # 产品id，用来查找对应的账户
        productname = '中证500'    # 品种名称，用来查找品种id
        connet_mysql = ConnectMysql(host='202.104.102.166', user='ppw_gtjaqh_user',
                                    password='IJU^T!yv0vbWwJXh', port=3306)
        bull_market_sql = "SELECT holdvol,stlprc FROM ppw_gtjaqh.`cm_gj_future_trade_hold` WHERE " \
                          "tradingday = '{}' AND assetacc = (SELECT assetacc FROM " \
                          "ppw_gtjaqh.`cm_fund_future_account_map` WHERE fund_id = '{}') " \
                          "AND productcode = (SELECT productcode FROM ppw_gtjaqh.`cm_gj_future_product` " \
                          "WHERE productname = '{}')   AND tradedir = 'B'".format(open_time, fund_id, productname)
        print(bull_market_sql)
        bull_market_result = connet_mysql.fetchall(bull_market_sql)   # 返回持仓表的对应的持仓量和结算价
        connet_mysql = ConnectMysql(host='202.104.102.166', user='ppw_gtjaqh_user',
                                    password='IJU^T!yv0vbWwJXh', port=3306)
        multiplier_sql = "SELECT multiplier FROM ppw_gtjaqh.`cm_gj_future_product` WHERE productname = '中证500'"
        multiplier_result = connet_mysql.fetchall(multiplier_sql)   # 返回对应的品种的标的乘数
        print(bull_market_result)
        for i in bull_market_result:
            bull_market += float(i[0])*float(i[1])*multiplier_result
        return bull_market

    def test_bear_market_value(self):
        """计算空头市值"""
        bear_market = 0
        open_time = '20200513'   # 持仓日期
        fund_id = 'CF0000003J'   # 产品id，用来查找对应的账户
        productname = '中证500'    # 品种名称，用来查找品种id
        connet_mysql = ConnectMysql(host='202.104.102.166', user='ppw_gtjaqh_user',
                                    password='IJU^T!yv0vbWwJXh', port=3306)
        bull_market_sql = "SELECT holdvol,stlprc FROM ppw_gtjaqh.`cm_gj_future_trade_hold` WHERE " \
                          "tradingday = '{}' AND assetacc = (SELECT assetacc FROM " \
                          "ppw_gtjaqh.`cm_fund_future_account_map` WHERE fund_id = '{}') " \
                          "AND productcode = (SELECT productcode FROM ppw_gtjaqh.`cm_gj_future_product` " \
                          "WHERE productname = '{}')   AND tradedir = 'S'".format(open_time, fund_id, productname)
        print(bull_market_sql)
        bull_market_result = connet_mysql.fetchall(bull_market_sql)   # 返回持仓表的对应的持仓量和结算价
        print(bull_market_result)
        connet_mysql = ConnectMysql(host='202.104.102.166', user='ppw_gtjaqh_user',
                                    password='IJU^T!yv0vbWwJXh', port=3306)
        multiplier_sql = "SELECT multiplier FROM ppw_gtjaqh.`cm_gj_future_product` WHERE productname = '中证500'"
        multiplier_result = connet_mysql.fetchall(multiplier_sql)  # 返回对应的品种的标的乘数
        for i in bull_market_result:
            bear_market += float(i[0])*float(i[1])*multiplier_result
        return bear_market


if __name__ == '__main__':
    bull_market_ = TestRollingDifferenceValue().test_bull_market_value()
    print('多头市值：', bull_market_)
    bear_market_ = TestRollingDifferenceValue().test_bear_market_value()
    print('空头市值：', bear_market_)
    print('轧差市值：', bull_market_-bear_market_)
