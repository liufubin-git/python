# -*- coding: utf-8 -*-
""" 
@Time    : 2020/12/4 18:23
@Author  : liufubin
@FileName: test_indicator_api.py
@description: 收益风险指标计算接口
"""
import requests
import unittest
import pytest


class TestIndicator(unittest.TestCase):
    isskip = 1

    @staticmethod
    def combination_test_environment(fundid='MF00003TND', startdate='2019-06-01', enddate='2020-05-31'):
        """组合大师测试环境收益风险指标"""
        url = 'https://master-test.simuwang.com/dataservice/v1/secuirty/{}/indicator?' \
              'startDate={}&endDate={}&dataSource=Daily&frequency=Monthly&benchmarkId=IN00000008' \
              '&sampleId={}&riskOfFreeId=IN0000000M&userId=864859&indexs={}&' \
              't=1607076223729'.format(fundid, startdate, enddate, fundid, fundid)
        indicator_api_result = requests.get(url=url)
        return indicator_api_result

    @staticmethod
    def combination_production_enviroment(fundid='MF00003TND', startdate='2019-06-01', enddate='2020-05-31'):
        """调用组合大师生产环境风险收益指标接口"""
        url = 'https://fof.simuwang.com/dataservice/v1/secuirty/{}/indicator?' \
              'startDate={}&endDate={}&dataSource=Daily&frequency=Monthly&benchmarkId=IN00000008' \
              '&sampleId={}&riskOfFreeId=IN0000000M&userId=864859&indexs={}&' \
              't=1607076223729'.format(fundid, startdate, enddate, fundid, fundid)
        indicator_api_result = requests.get(url=url)
        return indicator_api_result

    @unittest.skipIf(isskip == 0, '收益风险指标结果测试与生产对比用例跳过')
    def test_check_test_production(self):
        """检查指标计算测试环境和生产环境返回数据是否一致"""
        test_result = TestIndicator.combination_test_environment()
        prodution_result = TestIndicator.combination_production_enviroment()
        test_result = test_result.json()
        test_result = test_result['data']['dataset'][0]  # 获取测试环境接口返回数据中对应基金的数据
        prodution_result = prodution_result.json()
        prodution_result = prodution_result['data']['dataset'][0]   # 获取生产环境接口返回数据中对应基金的数据
        self.assertEqual(test_result, prodution_result, '测试环境与生产环境两边数据不一致')

    def test_check_own_calculate_api(self):
        """检查自己计算的指标结果和接口返回的数据对比"""


if __name__ == '__main__':
    indicator = TestIndicator()
    suite = unittest.TestSuite()
    suite.addTest(TestIndicator('test_check_test_production'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
