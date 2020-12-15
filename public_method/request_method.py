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
import logging
import time


class RequestMethod(object):
    def __init__(self):
        logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                            level=logging.DEBUG)

    @staticmethod
    def request_get_method(requesturl):
        """接口请求get方法，静态方法可以直接调用，不需要实例化"""
        logging.debug(requesturl)
        response = requests.get(requesturl)
        # cookie_jar = requests.session().get(requesturl).cookies
        cookie_jar = response.cookies
        cookie_json = requests.utils.dict_from_cookiejar(cookie_jar)
        logging.debug(response)
        logging.debug(cookie_json)
        return cookie_json, response

    @staticmethod
    def http_post_method(requesturl, headers, body):
        """接口请求post方法，静态方法可以直接调用，不需要实例化"""
        body = json.dumps(body)
        response = requests.post(url=requesturl, headers=headers, data=body)
        cookie_jar = response.cookies
        cookie_json = requests.utils.dict_from_cookiejar(cookie_jar)
        # print(json.dumps(response.json()))  # jumps把字典数据转化成字符串，可以用json.cn查看,loads转化成字典，获取某个字段的值需要loads
        return cookie_json, response

    @staticmethod
    def cookies_connection(cookie_json):
        cookie_connection = ''
        for key, value in cookie_json.items():
            cookie_connection += '{}:{};'.format(key, value)
        print(cookie_connection)

    @staticmethod
    def request_delete_method(requesturl):
        """接口请求get方法，静态方法可以直接调用，不需要实例化"""
        response = requests.delete(requesturl)
        return response
