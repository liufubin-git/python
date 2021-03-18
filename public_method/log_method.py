# -*- coding: utf-8 -*-
""" 
@Time    : 2021/3/12 15:19
@Author  : liufubin
@FileName: log_method.py
@description: 测试日志公共封装方法
"""

import os
import logging

# 定义日志的绝对路径
base_url = r"D:\pycharmproject\lfbTest\log"


class Logger:
    def __init__(self, file_name, clevel=logging.DEBUG, flevel=logging.INFO):
        """传入运行的用例的文件名，生成以这个文件名命名的日志文件"""
        # 判断log文件是否存在，不存在的话创建文件以及日志文件
        project_dir = os.listdir(base_url)
        dir_name = file_name + '.log'  # log文件夹
        if dir_name not in project_dir:
            create_path = base_url + '/' + dir_name
            file = open(create_path, 'w', encoding='gb18030')
            file.close()
        # 创建logger
        path = base_url + file_name + '.log'
        self.logger = logging.getLogger(path)
        self.logger.setLevel(logging.DEBUG)
        # 防止创建多个logger对象
        if not self.logger.handlers:
            # 设置日志格式
            fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
            # 设置CMD日志
            sh = logging.StreamHandler()
            sh.setFormatter(fmt)
            sh.setLevel(clevel)
            # 设置文件日志
            fh = logging.FileHandler(path)
            fh.setFormatter(fmt)
            fh.setLevel(flevel)
            self.logger.addHandler(sh)
            self.logger.addHandler(fh)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def war(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def cri(self, message):
        self.logger.critical(message)
