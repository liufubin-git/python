# -*- coding: utf-8 -*-
""" 
@Time    : 2021/3/25 16:47
@Author  : liufubin
@FileName: test_position_cycle_earnings_contribution.py
@description: 持仓周期收益贡献对比
"""
from public_method.connect_mysql import ConnectMysql


class TestPositionCycleEarningContribution(object):
    def test_calculate_profit_and_loss(self):
        """计算持仓周期收益贡献中的盈亏"""
        fund_id = 'CF0000003J'  # 产品id，用来查找对应的账户
        productname = '螺纹'  # 品种名称，用来查找品种id
        unwind_data_sql = "SELECT posiact,tradedir,trdprc,trdvol,trdtms FROM ppw_gtjaqh.cm_gj_future_trade_data WHERE"\
                          " tradingday >= '20200801' AND tradingday <= '20200831'  AND posiact IN ('T'," \
                          "'C') AND productcode = (SELECT productcode FROM ppw_gtjaqh.`cm_gj_future_product` WHERE " \
                          "productname = '{}') AND assetacc = (SELECT assetacc FROM " \
                          "ppw_gtjaqh.`cm_fund_future_account_map` WHERE fund_id = '{}') ".format(productname, fund_id)
        connet_mysql = ConnectMysql(host='202.104.102.166', user='ppw_gtjaqh_user',
                                    password='IJU^T!yv0vbWwJXh', port=3306)
        unwind_data_result = connet_mysql.fetchall(unwind_data_sql)
        print(unwind_data_result)


if __name__ == '__main__':
    TestPositionCycleEarningContribution().test_calculate_profit_and_loss()