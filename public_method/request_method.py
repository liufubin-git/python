# -*- coding: utf-8 -*-
"""
@Time    : 2020/10/9 11:13
@Author  : liufubin
@FileName: request_method.py
@description: 接口请求公共方法
"""
import requests
import requests.utils
import json


class RequestMethod(object):
    def __init__(self):
        pass

    @staticmethod
    def request_get_method(requesturl):
        """接口请求get方法，静态方法可以直接调用，不需要实例化"""
        requests.get(requesturl)
        print(requesturl)
        cookie_jar = requests.session().get(requesturl).cookies
        cookie_json = requests.utils.dict_from_cookiejar(cookie_jar)
        return cookie_json

    @staticmethod
    def http_post_method(requesturl, headers, body):
        """接口请求post方法，静态方法可以直接调用，不需要实例化"""
        body = json.dumps(body)
        print('requesturl:', requesturl)
        print('header:', headers)
        print('body:', body)
        response = requests.post(url=requesturl, headers=headers, data=body)
        print(json.dumps(response.json()))  # jumps把字典数据转化成字符串，可以用json.cn查看,loads转化成字典，获取某个字段的值需要loads
        return response

    @staticmethod
    def request_delete_method(requesturl):
        """接口请求get方法，静态方法可以直接调用，不需要实例化"""
        response = requests.delete(requesturl)
        # print(requesturl)
        return response
