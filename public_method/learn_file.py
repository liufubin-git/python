# # -*- coding: utf-8 -*-
# """
# @Time    : 2020/10/14 9:13
# @Author  : liufubin
# @FileName: learn_file.py
# @description:
# """
# import numpy
import requests
# # a = 'ed'
# # c = a
# # b = 'ed'
# # print(c == b)  # 主要看value是否一致，值一致就返回true
# # print(a is b)  # 主要是看地址是否一致，id不一致返回false
# # print(id(b))
# # print(id(c))
# a = [
#             -0.006516,
#             0.020473,
#             8.3E-4,
#             2.16E-4,
#             0.045634,
#             1.77E-4,
#             5.61E-4,
#             -0.004807,
#             0.014613,
#             -0.023852,
#             0.049441,
#             -0.041449,
#             -0.007999,
#             -0.059332,
#             0.015925,
#             0.003571,
#             -0.006975,
#             0.070636,
#             0.034556,
#             -0.005026,
#             -0.004061,
#             0.016513,
#             0.004659,
#             -0.014596,
#             -0.015487,
#             -0.022641,
#             0.016027,
#             0.005114,
#             0.008439,
#             0.040694,
#             -0.004615,
#             0.013973,
#             0.005136,
#             0.015058,
#             0.10281,
#             -4.91E-4,
#             -0.02573,
#             -0.015634]
# # sum1 = 0
# # for i in a:
# #     print(i*100)
# #     sum1 = sum1 + i * 100
# # print(sum1)
#
# list1 = [25.826, -17.16, 24.955, 31.468, 20.552, 19.389, 27.799, -9.927, -13.158, -8.146, 10.244, -3.468]
# sum1 = 0
# for i in list1:
#     sum1 += i
# print(sum1)
# sum1 = sum1/12
# print(sum1)
# print(numpy.average(list1))
# print(sum(list1))
#
#
#
import datetime
#
# ll = '0.5792'
# print(type(ll))
# ll = float(ll)
# print(round(ll, 2))
#
#
# d1 = datetime.date(2020, 2, 21)
# d2 = datetime.date(2020, 6, 11)
# print((d2 - d1).days/7)

# print(pow((1+0.004), 365))
# print(0.004 * 365)
#
# print(pow(1.0465, 30))
url = 'https://ssa.crctrust.com/momapi/v1/hbsa/bond/bondCampisi-data'
body = {
        "token": "90f8cc553498578f8a1cb6001587eed1",
        "dbName": "master",
        "content": "select * from information_schema.processlist where info is not null"

}
r = requests.post(url, data=body)
print(r)
