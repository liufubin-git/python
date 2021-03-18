# -*- coding: utf-8 -*-
""" 
@Time    : 2020/12/8 15:37
@Author  : liufubin
@FileName: test_login_api.py
@description: 登录接口
"""
import pytest
import requests
import time
from public_method.request_method import RequestMethod


class Login(object):
    @staticmethod
    def login():
        registry_time = time.time()  # 获取当前时间时间戳
        get_session, getresponse = RequestMethod.request_get_method(  # 调获取code接口，会在redis中生成code码
                            'http://mom-test.simuwang.com/momapi/v1/system/userMgt/'
                            'getSmsCode?mobile=13055866827&registerOrNot=false&t={}'
                            .format(registry_time))
        print(getresponse)
        print(get_session)
        cookie_value = 'JSESSIONID={}'.format(get_session['JSESSIONID'])
        # for codes in range(1000, 9999, 1):
        body = {'mobile': '13055866827', 'code': 4568}
        url = 'http://mom-test.simuwang.com/momapi/api/sms/login'
        header = {"Content-Type": "application/json", "Cookie": cookie_value}
        response = requests.post(url=url, headers=header, data=body)
        print(response.json())


if __name__ == '__main__':
    Login.login()
