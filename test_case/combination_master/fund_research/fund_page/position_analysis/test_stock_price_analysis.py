# -*- coding: utf-8 -*-
""" 
@Time    : 2021/2/2 15:25
@Author  : liufubin
@FileName: test_stock_price_analysis.py
@description: 持仓分析股票价格分析测试用例
"""
from public_method.connect_mysql import ConnectMysql


class TestStockPriceAnnalysis(object):
    def test_check_price_threshold(self):
        """检查数据库高价低价股阈值数据准确性"""
        connect_mysql = ConnectMysql(host='202.104.102.166', user='rz_cm_master',
                                     password='TbLuENLK', port=3306, db='jydb')
        day = "'2021-01-11 00:00:00'"
        sql = "SELECT ClosePrice,InnerCode FROM QT_StockPerformance WHERE TradingDay = {}".format(day)
        sql_result = connect_mysql.fetchall(sql)  # 获取某一天的股票价格，表数据量很大，查询时间需要好几分钟
        price_list = []   # 价格列表
        innercode_sorted_list = []    # 股票id倒序列表
        innercode_dict = {}    # 价格与股票id相对应字典
        for i in sql_result:
            price = float(i[0])
            innercode = i[1]
            innercode_dict[price] = innercode
            price_list.append(float(i[0]))
        price_sorted_list = sorted(price_list, reverse=True)  # 价格倒序列表
        for i in price_sorted_list:
            for key, value in innercode_dict.items():
                if i == key:
                    innercode_sorted_list.append(value)
                    break
        print('股票价格原始数据：', sql_result)
        print('股票价格列表：', price_list)
        print('股票价格个数：', len(price_sorted_list))
        print('股票价格倒序列表：', price_sorted_list)
        print('股票价格三分之一处价格', price_sorted_list[int(len(price_sorted_list) * 1/3)])
        print('股票价格三分之二处价格', price_sorted_list[int(len(price_sorted_list) * 2/3)])
        print('股票价格三分之一股票数量值', len(price_sorted_list) * 1/3)
        print('股票价格三分之二股票数量值', len(price_sorted_list) * 2/3)
        print('股票价格三分之一股票数量值int型', int(len(price_sorted_list) * 1/3))
        print('股票价格三分之二股票数量值int型', int(len(price_sorted_list) * 2/3))
        print('股票id根据价格排序后的id排序', innercode_sorted_list)
        print('价格排序后三分之一处的股票id', innercode_sorted_list[int(len(price_sorted_list) * 1/3)])
        print('价格排序后三分之二处的股票id', innercode_sorted_list[int(len(price_sorted_list) * 2/3)])


if __name__ == '__main__':
    check_price = TestStockPriceAnnalysis()
    check_price.test_check_price_threshold()
