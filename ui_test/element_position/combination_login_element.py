# -*- coding: utf-8 -*-
"""
@Time    : 2020/10/9 9:13
@Author  : liufubin
@FileName: combination_login_element.py
@description:组合大师登录界面元素路径
"""

class LoginElement(object):
    """登录界面元素xpath路径，用于元素定位"""
    # 登录界面手机号输入框
    cellphone_xpath = '/html/body/section/main/div/div[1]/div/form/div[1]/div/div/div/div/input'
    # 登录界面密码输入框
    password_xpath = '/html/body/section/main/div/div[1]/div/form/div[2]/div/div/div/span/div[2]/input'
    # 登录界面记住密码选择框
    checkbox_xpath = '/html/body/section/main/div/div[1]/div/form/div[3]/div[1]/label/span[1]/span'
    # 登录界面确认登录按钮
    loginbutton_xpath = '/html/body/section/main/div/div[1]/div/form/div[4]/button'
    # 登录界面FOF资管点击按钮
    fof_mannager_xpath = '//*[@id="main"]/div/div[1]/a/img[1]'
    # 登录界面私密代销机构点击按钮
    agency_xpath = '//*[@id="main"]/div/div[2]/a/img[1]'
    # 登录界面券商营业部点击按钮
    brokerage_business_xpath = '//*[@id="main"]/div/div[3]/a/img[1]'
    # 登录界面学术科研点击按钮
    acedemic_research_xpath = '//*[@id="main"]/div/div[4]/a/img[1]'
    # 登录界面产品介绍点击按钮
    product_description_xpath = '/html/body/section/header/ul/li[2]/a'
    # 登录界面自定义策略点击按钮
    custom_strategy_xpath = '/html/body/section/header/ul/li[3]/a'
    # 登录界面关于我们点击按钮
    about_us = '/html/body/section/header/ul/li[4]/a'
