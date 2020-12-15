# -*- coding: utf-8 -*-
""" 
@Time    : 2020/12/8 18:36
@Author  : liufubin
@FileName: combination_master_login_date.py
@description: 组合大师登录请求参数
"""


class CombinationMasterLoginDate(object):
    @staticmethod
    def password_login_date(cellphone='13055866827', password='123456', usertype=2):
        """密码登录请求参数"""
        body = {"username": cellphone, "pass": password, "usertype": usertype, "rem": 0}
        url = 'https://fof.simuwang.com//Login/login'
        header = {
                    "Content-Type": "application/json",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ",
                    "X-Requested-With": "XMLHttpRequest",
                    "Accept": "application/json, text/plain, */*",
                    "charset": "UTF-8"
                  }
        return body, url, header

    @staticmethod
    def code_login_date():
        pass
