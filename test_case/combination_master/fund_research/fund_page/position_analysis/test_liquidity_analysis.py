# -*- coding: utf-8 -*-
""" 
@Time    : 2021/2/3 16:49
@Author  : liufubin
@FileName: test_liquidity_analysis.py
@description: 持仓分析资产流动性分析测试用例
"""
from public_method.connect_mysql import ConnectMysql


class TestLiquidityAnalysis(object):
    def test_check_liquidity_threshold(self):
        """检查数据库流动性阈值数据准确性"""
        connect_mysql = ConnectMysql(host='202.104.102.166', user='rz_cm_master',
                                     password='TbLuENLK', port=3306, db='jydb')
        valuation_day = "'2021-01-13'"   # 估值日期
        # valuation_day_split = valuation_day.split('-')
        # valuation_five_day = '{}-{}-{}'.format(valuation_day_split[0], valuation_day_split[1],
        #                                        (int(valuation_day_split[2])-4))
        valuation_five_day = "'2021-01-07'"  # 估值日前5日
        sql = "SELECT SUM(d.TurnoverValue) AS calnum, s.SecuCode AS calid FROM jydb.QT_DailyQuote d " \
              "INNER JOIN jydb.SecuMain s ON d.InnerCode = s.InnerCode INNER JOIN jydb.CT_SystemConst c " \
              "ON (s.ListedState = c.DM) WHERE s.SecuCategory = 1 AND s.SecuMarket IN (83, 90) AND " \
              "c.LB = 1176 AND c.DM IN (1) AND SUBSTR(d.TradingDay,1,10) >= {} AND " \
              "SUBSTR(d.TradingDay,1,10) <= {} GROUP BY s.SecuCode".format(valuation_five_day, valuation_day)
        sql_result = connect_mysql.fetchall(sql)   # 获取估值日近5日成交额
        # print(sql_result)
        turnover_list = []  # 成交额列表
        turnover_dict = {}  # 成交额与secucode映射表
        secucode_list = []  # secucode列表
        for i in sql_result:
            turnover = float(i[0])
            secucode = i[1]
            turnover_dict[turnover] = secucode
            turnover_list.append(float(i[0]))
        turnover_sorted_list = sorted(turnover_list, reverse=True)  # 成交额倒序排列
        print(turnover_sorted_list)
        print(turnover_sorted_list[int(len(turnover_sorted_list) * 1/5)])
        print(turnover_sorted_list[int(len(turnover_sorted_list) * 2/5)])
        print(turnover_sorted_list[int(len(turnover_sorted_list) * 3/5)])
        print(turnover_sorted_list[int(len(turnover_sorted_list) * 4/5)])
        print(turnover_dict[turnover_sorted_list[int(len(turnover_sorted_list) * 1/5)]])
        print(turnover_dict[turnover_sorted_list[int(len(turnover_sorted_list) * 2/5)]])
        print(turnover_dict[turnover_sorted_list[int(len(turnover_sorted_list) * 3/5)]])
        print(turnover_dict[turnover_sorted_list[int(len(turnover_sorted_list) * 4/5)]])


if __name__ == '__main__':
    check_liquidity_threshold = TestLiquidityAnalysis()
    check_liquidity_threshold.test_check_liquidity_threshold()
