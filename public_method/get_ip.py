# -*- coding: utf-8 -*-
""" 
@Time    : 2021/3/16 16:30
@Author  : liufubin
@FileName: get_ip.py
@description: 获取代理ip公共方法
"""
from public_method.request_method import RequestMethod
from pyquery import PyQuery
import requests
import telnetlib


class TestGetIp(object):
    # @staticmethod
    # def test_get_ip():
    #     """获取爬虫所需要的ip"""
    #     print('222')
    #     global address_port
    #     for i in range(1, 2):
    #         start_url = 'http://www.kuaidaili.com/free/inha/{}/'.format(i)
    #         header = {
    #             "X-Requested-With": "XMLHttpRequest",
    #             "charset": "UTF-8",
    #             "Connection": "keep-alive",
    #             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
    #                           "Chrome/89.0.4389.82 Safari/537.36",
    #             'Accept-Encoding': 'gzip, deflate, sdch',
    #             'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7'
    #         }
    #         print('111')
    #         cookies, response = RequestMethod.request_get_method(start_url, headers=header)
    #         print('555', response.text)
    #         if response.text:
    #             ip_address = re.compile('<td data-title="IP">(.*?)</td>')
    #             print(ip_address)
    #             re_ip_address = ip_address.findall(response.text)
    #             print(re_ip_address)
    #             port = re.compile('<td data-title="PORT">(.*?)</td>')
    #             re_port = port.findall(response.text)
    #             for address, port in zip(re_ip_address, re_port):
    #                 address_port = address + ':' + port
    #                 address_port.replace(' ', '')
    #         print(address_port)

    @staticmethod
    def get_page(url, headers):
        print('正在抓取', url)
        try:
            cookie, response = RequestMethod.request_get_method(url, headers=headers)
            print('抓取成功', url, response.status_code)
            if response.status_code == 200:
                return response.text
        except ConnectionError:
            print('抓取失败', url)
            return None

    @staticmethod
    def get_ip_from_66():
        """获取代理ip"""
        ip_port = []
        header = {
            "X-Requested-With": "XMLHttpRequest",
            "charset": "UTF-8",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/89.0.4389.82 Safari/537.36",
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7'
        }
        # ip_url = 'http://www.66ip.cn/{}.html'
        for i in range(5, 20):
            ip_url = 'http://www.66ip.cn/{}.html'.format(i)
            html = TestGetIp.get_page(ip_url, headers=header)
            if html:
                doc = PyQuery(html)
                trs = doc('.containerbox table tr:gt(0)').items()
                for tr in trs:
                    ip = tr.find('td:nth-child(1)').text()
                    port = tr.find('td:nth-child(2)').text()
                    ip_port = ip + ':' + port
                    # proxy = {'http:': ip_port}
                    # 校验ip是否可用方法1：
                    try:
                        telnetlib.Telnet(ip, port, timeout=5)
                        print('可用ip：', ip_port)
                        ip_port.append(ip_port)
                    except Exception as e:
                        print(ip + '不可用' + e)
                    # 校验ip是否可用方法2：
                    # try:
                    #     res = requests.get(url='https://www.baidu.com/', headers=header, proxies={'https': ip},
                    #                        timeout=5).text
                    #     print(len(res), '可用ip：', ip)  # 判断URL返回的数据长度是否大于5000
                    #     ip_port.append(ip_port)
                    # except Exception as e:
                    #     print('不可用ip', ip, e)
        print(ip_port)
        return ip_port
