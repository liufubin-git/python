# -*- coding: utf-8 -*-
""" 
@Time    : 2021/3/13 17:02
@Author  : liufubin
@FileName: test_api_defense.py
@description: 走势图api防御测试
"""
# import pytest
import json
# import random
import time
import requests
from public_method.get_ip import TestGetIp
from public_method.request_method import RequestMethod


class TestApiDefence(object):
    @staticmethod
    def test_get_login_cookies(username='13055866827', passwd='YfGE17P0BolEz116OlJVPQ=='):
        """先登录获取cookie"""
        body = {"username": username, "pass": passwd, "usertype": 2, "rem": 0}
        # url = 'https://fof.simuwang.com/Login/login'        # 生产环境登录接口
        url = 'https://master-test.simuwang.com/Login/login'  # 测试环境登录接口
        header = {
            # "Content-Type": "application/json",
            "X-Requested-With": "XMLHttpRequest",
            "Connection": "keep-alive",
            "charset": "UTF-8"
        }
        login_cookie, login_result = RequestMethod.http_post_method(requesturl=url, headers=header, body=body)
        # cookies_value = 'PHPSESSID={}'.format(login_cookie['PHPSESSID'])
        cookies_value = RequestMethod.cookies_connection(login_cookie)  # 把登录接口返回的cookie进行拼接
        print(login_result.json(), json.dumps(cookies_value))
        return cookies_value

    @staticmethod
    def test_get_fundid(page=1, pagesize=100):
        """获取全市场的基金id和成立时间，最新净值时间"""
        # 获取cookie，在接口的header中需要用到
        cookie_value = TestApiDefence.test_get_login_cookies(username='13055866827', passwd='YfGE17P0BolEz116OlJVPQ==')
        fundid_start_end_time = {}
        print(cookie_value)
        # url = 'https://fof.simuwang.com/PrivateVolumeData/getDataList'
        url = 'https://master-test.simuwang.com/PrivateVolumeData/getDataList'
        # body = 'raiseType=3&curveType=0&keyword=&columns[0][value]=fund_short_name-0' \
        #        '&columns[1][value]=fund_id-1&columns[2][value]=inception_date-2' \
        #        '&columns[3][value]=price_date-3&columns[4][value]=weighted_rating-4' \
        #        '&order=&sort=&weightedDataDisplay[]=&weightedDataDisplay[]=&page=1&pageSize=12'
        header = {
            "X-Requested-With": "XMLHttpRequest",
            "charset": "UTF-8",
            "Content-Type": "application/x-www-form-urlencoded",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/89.0.4389.82 Safari/537.36",
            "Cookie": "{}".format(cookie_value),
        }
        for i in range(1, page+1):
            body = {
                "raiseType": 3,
                "curveType": 0,
                "columns": [
                        {"value": "fund_short_name-0"},
                        {"value": "fund_id-1"},
                        {"value": "inception_date-2"},
                        {"value": "price_date-3"},
                        {"value": "weighted_rating-4"}
                ],
                "order": "",
                "weightedDataDisplay[]": "",
                "page": i,
                "pageSize": pagesize
            }
            cookie_result, result_fundid = RequestMethod.http_post_method(requesturl=url, headers=header, body=body)
            # 获取接口返回的数据并且取出基金的id和开始结束时间封装成字典类型，key为基金id，value为列表，第一个元素开始时间，第二个元素结束时间
            for j in result_fundid.json()['data']:
                time_list = [j['inception_date-2'], j['price_date-3']]
                fundid_start_end_time[j['fund_id']] = time_list
        return cookie_value, fundid_start_end_time

    @staticmethod
    def test_ip_changes_largeten_one_hour():
        """ip在一小时变更大于等于十次触发api防御--走势图"""
        # 调用获取基金id和时间的接口，请求的page和pagesize为想要获取的列表对应页数和每页的数量,页数默认1，数量默认一百
        cookie_value, fundid_start_end_time = TestApiDefence.test_get_fundid(page=1)
        # 调用获取ip的接口，获取的ip已经封装成list，每个元素的值为ip：port的样式
        ip_port = TestGetIp.get_ip_from_66()
        print(ip_port)
        i = 0
        print(fundid_start_end_time)
        start_time = int(time.time())  # 循环开始时间
        for key, value in fundid_start_end_time.items():
            # 循环跑对应的接口，同时对应的基金id，开始时间，结束时间会根据上面基金列表接口返回的数据循环
            fund_id = key
            fund_start_time = value[0]
            fund_end_time = value[1]
            proxy = {'http': ip_port[i]}   # 获取ip接口返回的对应ip和port对应的值，作为请求参数proxies进行传参
            # url = 'https://fof.simuwang.com/dataservice/v1/secuirties/{}/growth-contrast?' \
            #       'startDate={}&endDate={}&navType=OriginalNav&timeRange=FromSetup&initValue=1.0&' \
            #       'dataSourceType=Nav&raiseType=Public&strategy=Hybrid&visibility=Both&showAssetStyleBenmark=true&' \
            #       'dataSource=Weekly&t=1615626049841'.format(fund_id, fund_start_time, fund_end_time)
            url = 'https://master-test.simuwang.com/dataservice/v1/secuirties/{}/growth-contrast?' \
                  'startDate={}&endDate={}&navType=OriginalNav&timeRange=FromSetup&initValue=1.0&' \
                  'dataSourceType=Nav&raiseType=Public&strategy=Hybrid&visibility=Both&showAssetStyleBenmark=true&' \
                  'dataSource=Weekly&t=1615626049841'.format(fund_id, fund_start_time, fund_end_time)
            header = {
                "X-Requested-With": "XMLHttpRequest",
                "charset": "UTF-8",
                "Content-Type": "application/json",
                "Connection": "keep-alive",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/89.0.4389.82 Safari/537.36",
                "Cookie": "{}".format(cookie_value)
            }
            print(proxy)
            charts_result = requests.get(url=url, headers=header, proxies=proxy)
            # ip = requests.get(url='http://httpbin.org/ip', proxies=proxy)
            # print('ip:', ip.text)
            print(charts_result.text)
            # print(charts_result.content)
            if charts_result.status_code == 200:
                i += 1
            if i > 2:
                break
            # time.sleep(10)
        end_time = int(time.time())
        print('start_time:', start_time)
        print('end_time:', end_time)

    def test_ip_changes_lessten_one_hour(self):
        """ip在一小时变更小于十次不触发api防御"""
        cookie_value, fundid_start_end_time = TestApiDefence.test_get_fundid(page=1)
        ip_port = TestGetIp.get_ip_from_66()
        i = 0
        print(fundid_start_end_time)
        for key, value in fundid_start_end_time.items():
            fund_id = key
            fund_start_time = value[0]
            fund_end_time = value[1]
            proxy = {'http': ip_port[i]}
            # url = 'https://fof.simuwang.com/dataservice/v1/secuirties/{}/growth-contrast?' \
            #       'startDate={}&endDate={}&navType=OriginalNav&timeRange=FromSetup&initValue=1.0&' \
            #       'dataSourceType=Nav&raiseType=Public&strategy=Hybrid&visibility=Both&showAssetStyleBenmark=true&' \
            #       'dataSource=Weekly&t=1615626049841'.format(fund_id, fund_start_time, fund_end_time)
            url = 'https://master-test.simuwang.com/dataservice/v1/secuirties/{}/growth-contrast?' \
                  'startDate={}&endDate={}&navType=OriginalNav&timeRange=FromSetup&initValue=1.0&' \
                  'dataSourceType=Nav&raiseType=Public&strategy=Hybrid&visibility=Both&showAssetStyleBenmark=true&' \
                  'dataSource=Weekly&t=1615626049841'.format(fund_id, fund_start_time, fund_end_time)
            header = {
                "X-Requested-With": "XMLHttpRequest",
                "charset": "UTF-8",
                "Content-Type": "application/json",
                "Connection": "keep-alive",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/89.0.4389.82 Safari/537.36",
                "Cookie": "{}".format(cookie_value)
            }
            charts_result = requests.get(url=url, headers=header, proxies=proxy)
            ip = requests.get(url='http://httpbin.org/ip')
            print('ip:', ip.text)
            print(charts_result.text)
            i += 1
            if i > 8:
                break
            time.sleep(400)

    @staticmethod
    def test_browser_changes_largethan_10():
        """浏览器在一小时内变更超过十次以上api防御测试"""
        user_agent_list = [
            'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0)',
            'Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)',
            'Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0)',
            'Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11',
            'Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 '
            'Safari/537.1 LBBROWSER',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
            'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE '
            '2.X MetaSr 1.0',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 '
            'Chrome/30.0.1599.101 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 '
            'UBrowser/4.0.3214.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 '
            'Safari/537.36 SE 2.X MetaSr 1.0 ',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/89.0.4389.82 '
            'Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
            'Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; '
            '.NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; '
            '.NET4.0E) ',
            'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET '
            'CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3) ',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET '
            'CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E; SE 2.X MetaSr '
            '1.0)'
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 '
            'QQBrowser/6.9.11079.201 '
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)'
        ]
        cookie_value, fundid_start_end_time = TestApiDefence.test_get_fundid(page=1)
        print(fundid_start_end_time)
        start_time = int(time.time())
        i = 0
        for key, value in fundid_start_end_time.items():
            fund_id = key
            fund_start_time = value[0]
            fund_end_time = value[1]
            # url = 'https://fof.simuwang.com/dataservice/v1/secuirties/{}/growth-contrast?' \
            #       'startDate={}&endDate={}&navType=OriginalNav&timeRange=FromSetup&initValue=1.0&' \
            #       'dataSourceType=Nav&raiseType=Public&strategy=Hybrid&visibility=Both&showAssetStyleBenmark=true&' \
            #       'dataSource=Weekly&t=1615626049841'.format(fund_id, fund_start_time, fund_end_time)
            url = 'https://master-test.simuwang.com/dataservice/v1/secuirties/{}/growth-contrast?startDate' \
                  '={}&endDate={}&navType=CumulativeNav&timeRange=FromSetup&initValue=1.0' \
                  '&dataSourceType=Nav&raiseType=Private&strategy=Equity&visibility=Both&showAssetStyleBenmark=true' \
                  '&dataSource=Default&t=1615943306913'.format(fund_id, fund_start_time, fund_end_time)
            print(url)
            header = {
                "X-Requested-With": "XMLHttpRequest",
                "charset": "UTF-8",
                "Content-Type": "application/json",
                "Connection": "keep-alive",
                "User-Agent": "{}".format(user_agent_list[i]),
                "Cookie": "{}".format(cookie_value)
            }
            charts_result = requests.get(url=url, headers=header)
            print(charts_result.json())
            # print(charts_result.content)
            if charts_result.status_code == 200:
                i += 1
            if i > 15:
                break
            # time.sleep(40)
        end_time = time.time()
        print(start_time)
        print(end_time)

    @staticmethod
    def test_five_minutes_morethan_100():
        """五分钟调用接口超过100次api防御测试"""
        cookie_value, fundid_start_end_time = TestApiDefence.test_get_fundid(page=2)
        i = 0
        print(fundid_start_end_time)
        start_time = int(time.time())
        print(int(start_time))
        for key, value in fundid_start_end_time.items():
            fund_id = key
            fund_start_time = value[0]
            fund_end_time = value[1]
            # url = 'https://fof.simuwang.com/dataservice/v1/secuirties/{}/growth-contrast?' \
            #       'startDate={}&endDate={}&navType=OriginalNav&timeRange=FromSetup&initValue=1.0&' \
            #       'dataSourceType=Nav&raiseType=Public&strategy=Hybrid&visibility=Both&showAssetStyleBenmark=true&' \
            #       'dataSource=Weekly&t=1615626049841'.format(fund_id, fund_start_time, fund_end_time)
            url = 'https://master-test.simuwang.com/dataservice/v1/secuirties/{}/growth-contrast?' \
                  'startDate={}&endDate={}&navType=OriginalNav&timeRange=FromSetup&initValue=1.0&' \
                  'dataSourceType=Nav&raiseType=Public&strategy=Hybrid&visibility=Both&showAssetStyleBenmark=true&' \
                  'dataSource=Weekly&t=1615626049841'.format(fund_id, fund_start_time, fund_end_time)
            header = {
                "X-Requested-With": "XMLHttpRequest",
                "charset": "UTF-8",
                "Content-Type": "application/json",
                "Connection": "keep-alive",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/89.0.4389.82 Safari/537.36",
                "Cookie": "{}".format(cookie_value)
            }
            charts_result = requests.get(url=url, headers=header)
            print(charts_result.json())
            if charts_result.status_code == 200:
                i += 1
            if i > 120:
                break
        end_time = int(time.time())
        print(int(end_time))

    @staticmethod
    def test_eight_ours_morethan_2000():
        """八小时调用接口超过2000次api防御测试"""
        cookie_value, fundid_start_end_time = TestApiDefence.test_get_fundid(page=30)
        i = 0
        print(fundid_start_end_time)
        print(time.time())
        for key, value in fundid_start_end_time.items():
            fund_id = key
            fund_start_time = value[0]
            fund_end_time = value[1]
            # url = 'https://fof.simuwang.com/dataservice/v1/secuirties/{}/growth-contrast?' \
            #       'startDate={}&endDate={}&navType=OriginalNav&timeRange=FromSetup&initValue=1.0&' \
            #       'dataSourceType=Nav&raiseType=Public&strategy=Hybrid&visibility=Both&showAssetStyleBenmark=true&' \
            #       'dataSource=Weekly&t=1615626049841'.format(fund_id, fund_start_time, fund_end_time)
            url = 'https://master-test.simuwang.com/dataservice/v1/secuirties/{}/growth-contrast?' \
                  'startDate={}&endDate={}&navType=OriginalNav&timeRange=FromSetup&initValue=1.0&' \
                  'dataSourceType=Nav&raiseType=Public&strategy=Hybrid&visibility=Both&showAssetStyleBenmark=true&' \
                  'dataSource=Weekly&t=1615626049841'.format(fund_id, fund_start_time, fund_end_time)
            header = {
                "X-Requested-With": "XMLHttpRequest",
                "charset": "UTF-8",
                "Content-Type": "application/json",
                "Connection": "keep-alive",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/89.0.4389.82 Safari/537.36",
                "Cookie": "{}".format(cookie_value)
            }
            charts_result = requests.get(url=url, headers=header)
            if charts_result.status_code == 200:
                i += 1
            print(charts_result.json())
            if i > 2222:
                break
            print('i:', i)
            time.sleep(4)
        print(time.time())


if __name__ == '__main__':
    # TestApiDefence().test_get_login_cookies()
    # TestApiDefence().test_get_fundid()
    # TestApiDefence.test_ip_changes_largeten_one_hour()
    # TestApiDefence.test_browser_changes_largethan_10()
    # TestApiDefence().test_get_ip()
    # TestApiDefence.get_ip_from_66()
    # TestApiDefence.test_ip_changes_largeten_one_hour()
    # TestApiDefence.test_five_minutes_morethan_100()
    TestApiDefence.test_eight_ours_morethan_2000()
