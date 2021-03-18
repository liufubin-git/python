# -*- coding: utf-8 -*-
""" 
@Time    : 2021/3/4 10:08
@Author  : liufubin
@FileName: test_qianlong_competition.py
@description: 潜龙杯实盘大赛数据测试
"""
import pytest
from public_method.indicator_calculation_method.sharpe import Sharepe
from public_method.indicator_calculation_method.calmar import Calmar
from public_method.indicator_calculation_method.information_ratio import InformationRatio
from public_method.indicator_calculation_method.sotino_ratio import SotinoRatio
from public_method.indicator_calculation_method.maximum_retracement import MaximumRetracement


class QianlongCompetition(object):
    @classmethod
    def test_check_date(cls):
        week_fund = [3.2774, 3.1904, 3.1880, 3.1954, 3.1911, 3.2014]   # 周净值
        risk_frees = 0.015
        week_fund_earnings = []  # 周收益率
        for i in range(len(week_fund)-1):
            week_fund_earnings.append((week_fund[i+1]-week_fund[i])/week_fund[i])
        wind_rate = (week_fund[len(week_fund)-1]-week_fund[0])/week_fund[0]
        print('月收益率：', wind_rate)
        max_ratracement, max_ratracement_list = MaximumRetracement.maxiunm_retracement(week_fund)
        print('月最大回撤：', max_ratracement)
        sharp = Sharepe.sharpe(week_fund_earnings, risk_frees, isannual=True)
        print('夏普比率：', sharp)
        carmar = Calmar.calmar(startvalue=week_fund[0], endvalue=week_fund[len(week_fund)-1],
                               fund_net_value=week_fund, valuedates=1)
        print('卡玛比率：', carmar)
        # information = InformationRatio.information_ratio()


if __name__ == '__main__':
    QianlongCompetition.test_check_date()
