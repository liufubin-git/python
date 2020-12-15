# -*- coding: utf-8 -*-
"""
@Time    : 2020/10/12 9:13
@Author  : liufubin
@FileName: registry_api.py
@description: 华润项目填写注册接口请求
"""
import unittest
import json
import random
import time
import re
from public_method.request_method import RequestMethod
from request_date.registry_request import RegistryRequestDate
from public_method.connect_redis import ConnectRedis
from public_method.connect_mysql import ConnectMysql


class RegistryRequest(unittest.TestCase):
    isskip = ['yes']

    def setUp(self) -> None:
        pass

    # @unittest.skipIf(isskip == 'no', '用例跳过')
    def test_didnot_apply_code(self):
        """未申请验证码注册场景，没有调用获取验证码接口"""
        response = RequestMethod.http_post_method(requesturl=RegistryRequestDate.registry_request_url,
                                                  headers=RegistryRequestDate.registry_request_header,
                                                  body=RegistryRequestDate.registry_request_body)
        response = response.json()
        self.assertTrue(response['data']['message'] == '未申请验证码' and response['data']['code'] == 407, '没有申请验证码未报未申请验证码的错')

    # @unittest.skipIf(isskip == 'no', '用例跳过')
    def test_normal_registry(self):
        """正常注册，先调用获取验证码接口，得到code和cookie，请求注册接口"""
        registry_cellphone = random.randint(10000000, 99999999)  # 获取手机号后八位随机号码
        registry_time = time.time()  # 获取当前时间时间戳
        get_session, getresponse = RequestMethod.request_get_method(  # 调获取code接口，会在redis中生成code码
                                                        'http://mom-test.simuwang.com/momapi/v1/system/userMgt/'
                                                        'getSmsCode?mobile=130{}&registerOrNot=true&'
                                                        't={}'
                                                        .format(registry_cellphone, registry_time))
        cookie_value = 'JSESSIONID={}'.format(get_session['JSESSIONID'])
        registry_code = ConnectRedis().redis_get('"USER_CELLPHOME_130{}"'.format(registry_cellphone))  # 获取redis中的code码
        # registry_code = int(re.sub("\"", '', registry_code))
        print(registry_code)
        registry_code = registry_code.replace("\"", "")  # 因为redis的数据是带双引号的，需要去除
        RegistryRequestDate.registry_request_body['code'] = registry_code
        RegistryRequestDate.registry_request_body['cellphone'] = '130{}'.format(registry_cellphone)
        RegistryRequestDate.registry_request_header['Cookie'] = cookie_value  # 请求header需要带cookie
        response = RequestMethod.http_post_method(requesturl=RegistryRequestDate.registry_request_url,  # 调用注册接口
                                                  headers=RegistryRequestDate.registry_request_header,
                                                  body=RegistryRequestDate.registry_request_body)
        del RegistryRequestDate.registry_request_header['Cookie']
        response = response.json()
        self.assertTrue(response['data']['result'] == 'success' and response['data']['code'] == 200, '注册失败，该用例应该注册成功')

    # @unittest.skipIf(isskip == 'no', '用例跳过')
    def test_already_registry_cellphone(self):
        """手机号与申请的手机号不一致，先调用获取验证码接口，得到code和cookie，请求注册接口"""
        registry_cellphone = random.randint(10000000, 99999999)  # 获取手机号后八位随机号码
        registry_time = time.time()  # 获取当前时间时间戳
        get_session, getresponse = RequestMethod().request_get_method('http://192.168.1.37:8080'  # 调code接口
                                                                      '/momapi/v1/system/userMgt/getSmsCode?'
                                                                      'mobile=130{}&&registerOrNot=truet={}'
                                                                      .format(registry_cellphone, registry_time))
        print(get_session)
        cookie_value = 'JSESSIONID={}'.format(get_session['JSESSIONID'])
        registry_code = ConnectRedis().redis_get('USER_CELLPHOME_130{}'.format(registry_cellphone))  # 获取redis中的code码
        # registry_code = int(re.sub("\"", '', registry_code))
        registry_code = registry_code.replace("\"", "")  # 因为redis的数据是带双引号的，需要去除
        RegistryRequestDate.registry_request_body['code'] = registry_code
        RegistryRequestDate.registry_request_body['cellphone'] = '13055866828'
        RegistryRequestDate.registry_request_header['Cookie'] = cookie_value  # 请求header需要带cookie
        response = RequestMethod().http_post_method(requesturl=RegistryRequestDate.registry_request_url,  # 调用注册接口
                                                    headers=RegistryRequestDate.registry_request_header,
                                                    body=RegistryRequestDate.registry_request_body)
        del RegistryRequestDate.registry_request_header['Cookie']   # 删除hreder字段中的cookie，避免影响其他用例
        response = response.json()
        self.assertTrue(response['data']['message'] == '手机号与申请验证码的手机号不一致'
                        and response['data']['code'] == 407, '手机号不一致没有报不一致错误')

    # def test_delete_user(self):
    #     """删除自动化跑的用户，先找出创建的，并提取返回元组中的userid，逐条调用删除接口删除"""
    #     sql = "SELECT 	userid FROM rz_combination_master.cm_user  WHERE username LIKE '姓名%'"
    #     sql_result = ConnectMysql().fetchall(sql)
    #     print(type(sql_result))
    #     for i in sql_result:
    #         response = RequestMethod.request_delete_method('http://192.168.1.37:8080/momapi/v1/'
    #                                                        'system/userMgt/delUserByUserId?userId={}'.format(i[0]))
    #         print(response)


if __name__ == '__main__':
    # registry_response = RegistryRequest()
    RegistryRequest().test_normal_registry()
