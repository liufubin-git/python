# -*- coding: utf-8 -*-
""" 
@Time    : 2021/2/1 15:31
@Author  : liufubin
@FileName: test_market_stock_assets.py
@description: 持仓分析股票资产市值分析测试用例
"""
from public_method.connect_mysql import ConnectMysql
import pandas


class TestMarketStockAssets(object):
    def test_check_threshold_year(self):
        """检查数据库大盘股小盘股阈值年数据准确性"""
        connect_mysql = ConnectMysql(host='202.104.102.166', user='rz_cm_master', password='TbLuENLK', port=3306)
        sql = 'SELECT avg_totalmv,InnerCode FROM rz_combination_master.cm_jydb_stock_avg_market_year ' \
              'where trading_day = 2018'
        sql_result = connect_mysql.fetchall(sql)
        market_value_list = []  # 总市值列表
        innercode_list = []     # 股票id列表
        innercode_dict = {}     # 市值与股票id映射字典
        print(sql_result)
        for i in sql_result:
            market_value = float(i[0])
            innercode = i[1]
            innercode_dict[market_value] = innercode
            market_value_list.append(int(i[0]))
        print(market_value_list)
        market_value_sorted_list = sorted(market_value_list, reverse=True)
        print(len(market_value_sorted_list))
        print(market_value_sorted_list)
        list_sum = sum(market_value_sorted_list)  # 所有的总数
        i = 0
        print(list_sum)
        cumulative_sum = 0  # 累加的总数
        for m in market_value_sorted_list:
            cumulative_sum += m
            i += 1
            if cumulative_sum >= list_sum * 0.75 and ((cumulative_sum - m) < (list_sum * 0.75)):
                print(market_value_sorted_list[i-1])
                print(innercode_dict[market_value_sorted_list[i-1]])
            elif cumulative_sum >= list_sum * 0.9 and ((cumulative_sum - m) < (list_sum * 0.9)):
                print(market_value_sorted_list[i-1])
                print(innercode_dict[market_value_sorted_list[i-1]])
        # sql_list = []
        # print(list(sql_result))
        # print(pandas.DataFrame(sql_result).values)

    @staticmethod
    def test_chenk_value_weight():
        """
        检查持仓分析中的股票市值权重占大盘小盘股权重的准确性
        步骤：把这个基金的股票id找出来，然后通过这些股票id找出这些股票的这年的日均总股本市值，然后把循环这些查询出来的日均总股本市值和阈值做对比。
        """
        connect_mysql = ConnectMysql(host='202.104.102.166', user='rz_cm_master', password='TbLuENLK', port=3306)
        valuation_data = '2016-12-31'
        # stock_id_sql = "SELECT t.securities_code FROM rz_combination_master.cm_fund_position_detail t WHERE " \
        #                "t.fund_id = 'MF00003PWC' AND t.isvalid = 1 AND t.valuation_date = {} AND " \
        #                "t.userid = 864859 AND t.sec_type = 0 AND t.securities_code IS NOT NULL AND " \
        #                "t.sec_id IS NOT NULL".format(valuation_data)  # 查找基金下的某个估值日的股票id
        stock_id_sql = "SELECT t.securities_code FROM rz_hfdb_core.fund_position_detail t LEFT JOIN " \
                       "rz_hfdb_core.base_underlying_information tt ON t.sec_id = tt.sec_id AND " \
                       "tt.isvalid = 1 AND t.isvalid = 1 WHERE t.fund_id = 'MF00003PWC' AND t.isvalid = 1 " \
                       "AND t.valuation_date = '{}' AND t.sec_id IS NOT NULL AND t.market_value IS NOT NULL " \
                       "AND t.sec_type = 0".format(valuation_data)  # 查找基金下的某个估值日的股票id
        stock_sql_result = connect_mysql.fetchall(stock_id_sql)
        print(stock_sql_result)
        stock_id_list = []
        for i in stock_sql_result:
            stock_id_list.append(i[0])
        print(stock_id_list)
        print(len(stock_id_list))
        valuation_year = valuation_data.split('-')[0]  # 因为一年日均总股本市值的查找时间是为年
        stock_value_sql = "select sm.SecuCode,my.avg_totalmv from jydb.SecuMain sm left join " \
                          "rz_combination_master.cm_jydb_stock_avg_market_year my on my.InnerCode = sm.InnerCode " \
                          "and my.trading_day = '{}' and my.isvalid = 1 where sm.SecuCode in {} and " \
                          "sm.SecuCategory = 1".format(valuation_year, tuple(stock_id_list))  # 查询每个个股的一年日均总股本市值：
        connect_mysql = ConnectMysql(host='202.104.102.166', user='rz_cm_master', password='TbLuENLK', port=3306)
        stock_value_sql_result = connect_mysql.fetchall(stock_value_sql)
        print(stock_value_sql_result)
        stock_value_list = []    # 个股日均总市值列表
        large_cap_num = 0    # 大盘股数量
        mid_cap_num = 0      # 中盘股数量
        small_cap_num = 0    # 小盘股数量
        stock_num = 0        # 基金对应股票总数量
        for i in stock_value_sql_result:
            stock_num += 1
            if i[1] is None:
                small_cap_num += 1
                break
            else:
                stock_value_list.append(int(i[1]))
        print(stock_value_list)
        year_value_threshold_sql = "select cum_avg_totalmv_n1,cum_avg_totalmv_n2 from " \
                                   "rz_combination_master.cm_stock_market_performance_year " \
                                   "where trading_day = '{}' and isvalid = 1".format(valuation_year)  # 大小盘阈值
        connect_mysql = ConnectMysql(host='202.104.102.166', user='rz_cm_master', password='TbLuENLK', port=3306)
        year_value_threshold = connect_mysql.fetchall(year_value_threshold_sql)
        print(year_value_threshold)
        for i in stock_value_list:
            if i >= int(year_value_threshold[0][0]):
                large_cap_num += 1
            elif i < int(year_value_threshold[0][1]):
                small_cap_num += 1
            else:
                mid_cap_num += 1
        print(valuation_data + '大盘股权重：', large_cap_num/stock_num)
        print(valuation_data + '小盘股权重：', small_cap_num/stock_num)
        print(valuation_data + '中盘股权重：', mid_cap_num/stock_num)


if __name__ == '__main__':
    check_sql = TestMarketStockAssets()
    # check_sql.test_check_threshold_year()
    check_sql.test_chenk_value_weight()
