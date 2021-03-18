# -*- coding: utf-8 -*-
""" 
@Time    : 2021/2/3 14:56
@Author  : liufubin
@FileName: test_asset_financial_analysis.py
@description: 持仓分析资产财务分析测试用例
"""

from public_method.connect_mysql import ConnectMysql


class TestAssetFinancialAnalysis(object):
    @staticmethod
    def test_check_roe_threshold_greater_zero():
        """检查数据库绩优股(roe大于0)阈值数据准确性"""
        connect_mysql = ConnectMysql(host='202.104.102.166', user='rz_cm_master',
                                     password='TbLuENLK', port=3306, db='jydb')
        day = "'2019-03-31'"
        sql = "SELECT m.roe,s.SecuCode FROM jydb.LC_MainIndexNew m INNER JOIN jydb.SecuMain s " \
              "ON (m.CompanyCode = s.CompanyCode) INNER JOIN jydb.CT_SystemConst c ON " \
              "(s.ListedState = c.DM) WHERE s.SecuCategory = 1 AND s.SecuMarket IN (83,90) AND c.LB = 1176 " \
              "AND c.DM IN (1) AND  SUBSTR(EndDate,1,10) = {} AND m.roe > 0".format(day)
        sql_result = connect_mysql.fetchall(sql)  # 获取某一天的所有A股ROE值
        roe_greater_zero = []    # 大于0的roe值的列表
        roe_secucode_dict = {}   # 大于0的roe与secucode映射表
        # secucode_list = []
        for i in sql_result:
            roe = float(i[0])
            secucode = i[1]
            roe_secucode_dict[roe] = secucode
            roe_greater_zero.append(float(i[0]))
        roe_greater_zero_sorted = sorted(roe_greater_zero)
        print(sql_result)
        print(roe_greater_zero)
        print(roe_greater_zero_sorted)
        if (len(roe_greater_zero_sorted)) % 2 == 0:
            list_len = int(len(roe_greater_zero_sorted) / 2)
            roe_median = (roe_greater_zero_sorted[list_len] + roe_greater_zero_sorted[list_len + 1]) / 2
            print(list_len)
            print(roe_median)
            print(roe_secucode_dict[roe_greater_zero_sorted[list_len]])
            print(roe_secucode_dict[roe_greater_zero_sorted[list_len + 1]])

        else:
            list_len = len(roe_greater_zero_sorted) / 2
            print(list_len)
            list_len = int(len(roe_greater_zero_sorted) / 2) + 1
            print(list_len)
            roe_median = roe_greater_zero_sorted[list_len]
            print(roe_median)
            print(roe_secucode_dict[roe_median])

    @staticmethod
    def test_check_roe_threshold_less_zero():
        """检查数据库绩优股(roe小于0)阈值数据准确性"""
        connect_mysql = ConnectMysql(host='202.104.102.166', user='rz_cm_master',
                                     password='TbLuENLK', port=3306, db='jydb')
        day = "'2019-03-31'"
        sql = "SELECT m.roe,s.SecuCode FROM jydb.LC_MainIndexNew m INNER JOIN jydb.SecuMain s " \
              "ON (m.CompanyCode = s.CompanyCode) INNER JOIN jydb.CT_SystemConst c ON " \
              "(s.ListedState = c.DM) WHERE s.SecuCategory = 1 AND s.SecuMarket IN (83,90) AND c.LB = 1176 " \
              "AND c.DM IN (1) AND  SUBSTR(EndDate,1,10) = {} AND m.roe < 0".format(day)
        sql_result = connect_mysql.fetchall(sql)  # 获取某一天的所有A股ROE值
        roe_greater_zero = []    # 大于0的roe值的列表
        roe_secucode_dict = {}   # 大于0的roe与secucode映射表
        # secucode_list = []
        for i in sql_result:
            roe = float(i[0])
            secucode = i[1]
            roe_secucode_dict[roe] = secucode
            roe_greater_zero.append(float(i[0]))
        roe_greater_zero_sorted = sorted(roe_greater_zero, reverse=True)
        print(sql_result)
        print(roe_greater_zero)
        print(roe_greater_zero_sorted)
        if (len(roe_greater_zero_sorted)) % 2 == 0:
            list_len = int(len(roe_greater_zero_sorted)/2)
            roe_median = (roe_greater_zero_sorted[list_len] + roe_greater_zero_sorted[list_len + 1])/2
            print(list_len)
            print(roe_median)
            print(roe_secucode_dict[roe_greater_zero_sorted[list_len]])
            print(roe_secucode_dict[roe_greater_zero_sorted[list_len + 1]])
        else:
            list_len = len(roe_greater_zero_sorted) / 2
            print(list_len)
            list_len = int(len(roe_greater_zero_sorted) / 2) + 1
            print(list_len)
            roe_median = roe_greater_zero_sorted[list_len]
            print(roe_median)
            print(roe_secucode_dict[roe_median])


if __name__ == '__main__':
    check_roe = TestAssetFinancialAnalysis()
    check_roe.test_check_roe_threshold_greater_zero()
    # check_roe.test_check_roe_threshold_less_zero()
