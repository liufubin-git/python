# -*- coding: utf-8 -*-
"""
@Time    : 2020/10/12 9:13
@Author  : liufubin
@FileName: registry_request.py
@description: 华润注册请求接口参数
"""
import random


class RegistryRequestDate(object):

    registry_request_body = {  # 用户注册请求参数
        "registername": "姓名{}".format(random.randint(0, 100)),
        "applyCompanyName": "所属机构{}".format(random.randint(0, 100)),
        "cellphone": "13055955875",
        "code": "7845",
        "userStatus": 0,
        "userLevel": 0,
        "applyway": 3,
        "verifiedStatus": 0
    }
    registry_request_url = "http://192.168.1.37:8080/momapi/v1/system/userMgt/registerUser"  # 用户注册url
    registry_request_header = {"Content-Type": "application/json"}
