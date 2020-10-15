# -*- coding: utf-8 -*-
"""
@Time    : 2020/10/10 9:13
@Author  : liufubin
@FileName: login.py
@description: 组合大师登录界面用例
"""
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from ui_test.element_position.combination_login_element import LoginElement
import time


class Login(object):
    def __init__(self):
        """初始化连接谷歌浏览器并打开组合大师登录界面"""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()     # 最大窗口
        self.driver.get('https://fof.simuwang.com/login')

    def login(self):
        """组合大师登录功能"""
        time.sleep(1)
        self.driver.find_element_by_xpath(LoginElement.cellphone_xpath).send_keys('18826242365')  # 获取输入框并输入号码
        time.sleep(1)
        self.driver.find_element_by_xpath(LoginElement.password_xpath).send_keys('wn2020')   # xpath元素定位
        time.sleep(1)
        self.driver.find_element_by_xpath(LoginElement.checkbox_xpath).click()    # 获取元素并点击
        time.sleep(1)
        self.driver.find_element_by_xpath(LoginElement.loginbutton_xpath).click()
        # driver.find_element_by_xpath(LoginElement.loginbutton_xpath).send_keys(Keys.ENTER)
        time.sleep(5)

    def click_fof(self):
        """组合大师登录界面点击fof资管"""
        time.sleep(1)
        self.driver.find_element_by_xpath(LoginElement.fof_mannager_xpath).click()

    def click_agency(self):
        """组合大师登录界面点击私募代销机构"""
        time.sleep(1)
        self.driver.find_element_by_xpath(LoginElement.agency_xpath).click()

    def click_brokerage_business(self):
        """组合大师登录界面点击券商营业部"""
        time.sleep(1)
        self.driver.find_element_by_xpath(LoginElement.brokerage_business_xpath).click()

    def click_acedemic_research(self):
        """组合大师登录界面点击学术科研"""
        time.sleep(1)
        self.driver.find_element_by_xpath(LoginElement.acedemic_research_xpath).click()

    def click_product_description(self):
        """组合大师登录界面点击产品介绍"""
        time.sleep(1)
        self.driver.find_element_by_xpath(LoginElement.product_description_xpath).click()

    def click_custom_strategy(self):
        """组合大师登录界面点击自定义策略"""
        time.sleep(1)
        self.driver.find_element_by_xpath(LoginElement.custom_strategy_xpath).click()

    def click_about_ud(self):
        """组合大师登录界面点击关于我们"""
        time.sleep(1)
        self.driver.find_element_by_xpath(LoginElement.about_us).click()


if __name__ == '__main__':
    login = Login()
    login.login()
    # login.click_fof()
