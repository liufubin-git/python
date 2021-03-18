# -*- coding: utf-8 -*-
""" 
@Time    : 2020/12/8 16:29
@Author  : liufubin
@FileName: test_combination_master_login.py
@description: 组合大师登录测试用例
"""
from public_method.request_method import RequestMethod
import pytest
import requests
import unittest


class TestCombinationMaterLogin(unittest.TestCase):
    isskip = 1

    @unittest.skipIf(isskip == 0, '正常登陆用例跳过')
    def test_normal_password_login(self):
        """密码正常登陆"""
        body = {"username": "13055866827", "pass": "lfb13055866827", "usertype": 2, "rem": 0}
        url = 'https://fof.simuwang.com/Login/login'
        header = {
                    # "Content-Type": "application/json",
                    "X-Requested-With": "XMLHttpRequest",
                    "charset": "UTF-8"
                  }
        result = requests.post(url=url, headers=header, data=body)
        result = result.json()
        print(result)
        self.assertTrue(result['msg'] == '登录成功!' and result['suc'] == 1, '登陆失败')

    @unittest.skipIf(isskip == 0, '错误密码登陆用例跳过')
    def test_error_password_login(self):
        """错误密码登陆"""
        body = {"username": "18826242365", "pass": "wn20201", "usertype": 2, "rem": 0}
        url = 'https://fof.simuwang.com/Login/login'
        header = {
            # "Content-Type": "application/json",
            "X-Requested-With": "XMLHttpRequest",
            "charset": "UTF-8"
        }
        result = requests.post(url=url, headers=header, data=body)
        result = result.json()
        print(result)
        self.assertTrue(result['msg'] == '用户名/手机号或密码不正确!' and result['suc'] == 4, '错误密码的登录有问题')

    @unittest.skipIf(isskip == 0, '错误用户名登陆用例跳过')
    def test_error_username_login(self):
        """错误用户名登陆"""
        body = {"username": "13000000000", "pass": "wn2020", "usertype": 2, "rem": 0}
        url = 'https://fof.simuwang.com/Login/login'
        header = {
            # "Content-Type": "application/json",
            "X-Requested-With": "XMLHttpRequest",
            "charset": "UTF-8"
        }
        result = requests.post(url=url, headers=header, data=body)
        result = result.json()
        print(result)
        self.assertTrue(result['msg'] == '用户名/手机号或密码不正确!' and result['suc'] == 4, '错误密码的登录有问题')

    @staticmethod
    def test_logout():
        """退出登陆"""
        url = 'https://fof.simuwang.com/Login/logout'
        requests.get(url=url)


if __name__ == '__main__':
    # CombinationMaterLogin().test_logout()
    suite = unittest.TestSuite()
    suite.addTest(TestCombinationMaterLogin('test_normal_password_login'))
    # suite.addTest(CombinationMaterLogin('test_error_password_login'))
    # suite.addTest(CombinationMaterLogin('test_error_username_login'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
