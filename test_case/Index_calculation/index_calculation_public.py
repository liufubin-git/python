# -*- coding: utf-8 -*-
""" 
@Time    : 2020/11/30 17:41
@Author  : liufubin
@FileName: index_calculation_public.py
@description: 指标计算调用公共方法
"""
import unittest
from public_method.alpha import Alpha
from public_method.beta import Beta
from public_method.calmar import Calmar
from public_method.biggest_monthly_down import BiggesrMonthlyDown
from public_method.distance_highest_rate import DistanceHighestRate
from public_method.down_capture import DownCapture
from public_method.downside_risk import DownsideRisk
from public_method.downward_capture import DownwardCapture
from public_method.information_ratio import InformationRatio
from public_method.jensen import Jensen
from public_method.kappa import Kappa
from public_method.kurtosis import Kurtosis
from public_method.omega_ratio import OmegaRtio
from public_method.range_return_rate import RangeReturnRate
from public_method.sharpe import Sharepe
from public_method.skewness import Skewness
from public_method.sotino_ratio import SotinoRatio
from public_method.sotino_ratio_MAR import SotioRatioMar
from public_method.standard_deviation import StandardDeviation
from public_method.success_rate import SuccessRate
from public_method.track_error import TrackError
from public_method.treynor import Treynor
from public_method.uplink_capture import UplinkCapture
from public_method.upward_capture import UpwardCapture
from request_date.combination_master.index_calculation_data import InvestmentCertificateBiomedical


class IndexCalculationPublic(unittest.TestCase):
    isskip = 1
    monthly_fund = InvestmentCertificateBiomedical.month_fund  # 获取的计算指标的月度收益率
    benchmark_monthlys = InvestmentCertificateBiomedical.benchmark_monthlys  # 获取的计算指标的基准收益率
    years = InvestmentCertificateBiomedical.years   # 获取的需要年化的年数
    risk_frees = 0.015   # 无风险收益率
    start_fund = InvestmentCertificateBiomedical.start_fund   # 计算指标的开始净值
    end_fund = InvestmentCertificateBiomedical.end_fund  # 计算指标的结束净值
    # url = 'https://master-test.simuwang.com/dataservice/v1/secuirty/MF00003TND/indicator?' \
    #       'startDate=2019-06-01&endDate=2020-05-31&dataSource=Daily&frequency=Monthly&benchmarkId=IN00000008' \
    #       '&sampleId=MF00003TND&riskOfFreeId=IN0000000M&userId=864859&indexs=MF00003TND&t=1607076223729'
    # indicator_api_result = requests.get(url=url)

    def setUp(self) -> None:
        pass

    @unittest.skipIf(isskip == 0, '计算阿尔法用例跳过')
    def test_calculate_alpha(self, isannual=True):
        """计算阿尔法测试用例，monthly_fund为基金月度收益率，benchmark_monthlys为基准月度收益率"""
        monthly_fund = IndexCalculationPublic.monthly_fund
        benchmark_monthlys = IndexCalculationPublic.benchmark_monthlys
        alpha_result = Alpha.alpha(monthly_fund_field=monthly_fund,
                                   benchmark_monthly=benchmark_monthlys, isannual=isannual)
        print('阿尔法计算结果：', alpha_result)

    @unittest.skipIf(isskip == 0, '计算贝塔用例跳过')
    def test_calculate_beta(self):
        """计算贝塔测试用例，monthly_fund为基金月度收益率，benchmark_monthlys为基准月度收益率"""
        monthly_fund = IndexCalculationPublic.monthly_fund
        benchmark_monthlys = InvestmentCertificateBiomedical.benchmark_monthlys
        beta_result = Beta.beta(monthly_fund_field=monthly_fund, benchmark_monthly=benchmark_monthlys)
        print('贝塔计算结果：', beta_result)

    @unittest.skipIf(isskip == 0, '计算当月最大下跌用例跳过')
    def test_biggest_monthly_down(self):
        """计算当月最大下跌，monthly_fund为基金月度收益率"""
        monthly_fund = IndexCalculationPublic.monthly_fund
        down_min_result = BiggesrMonthlyDown.biggest_monthly_down(month_fund_yield=monthly_fund)
        print('当月最大下跌计算结果：', down_min_result)

    @unittest.skipIf(isskip == 0, '计算下跌月份比用例跳过')
    def test_down_month_ratio(self):
        """计算下跌月份比，monthly_fund为基金月度收益率"""
        monthly_fund = IndexCalculationPublic.monthly_fund
        down_rate_result = BiggesrMonthlyDown.down_month_ratio(month_fund_yield=monthly_fund)
        print('下跌月份比计算结果为：', down_rate_result)

    @unittest.skipIf(isskip == 0, '计算跑赢指数用例跳过')
    def test_batting_average(self):
        """计算跑赢指数，monthly_fund为基金月度收益率"""
        monthly_fund = IndexCalculationPublic.monthly_fund
        benchmark_monthlys = InvestmentCertificateBiomedical.benchmark_monthlys
        batting_average_result = BiggesrMonthlyDown.batting_average(monthly_fund_field=monthly_fund,
                                                                    benchmark_monthly=benchmark_monthlys)
        print('跑赢指数月份比计算结果为：', batting_average_result)

    @unittest.skipIf(isskip == 0, '计算盈亏比用例跳过')
    def tset_profit_loss_ratio(self):
        """计算盈亏比，monthly_fund为基金月度收益率"""
        monthly_fund = IndexCalculationPublic.monthly_fund
        prolit_loss_result = BiggesrMonthlyDown.profit_loss_ratio(monthly_fund_field=monthly_fund)
        print('盈亏比计算结果：', prolit_loss_result)

    @unittest.skipIf(isskip == 0, '计算卡玛用例跳过')
    def test_calculate_calmar(self):
        """计算卡玛测试用例，monthly_fund为基金月度收益率，benchmark_monthlys为基准月度收益率"""
        startvalue = IndexCalculationPublic.start_fund
        endvalue = IndexCalculationPublic.end_fund
        fund_net_value = IndexCalculationPublic.monthly_fund
        year = IndexCalculationPublic.years
        calmar_result = Calmar.calmar(startvalue, endvalue, fund_net_value, year)
        print('卡玛计算结果：', calmar_result)

    @unittest.skipIf(isskip == 0, '距最高净值比用例跳过')
    def test_distance_highest_rate(self):
        """计算距最高净值比，daily_fund为基金日频净值列表"""
        daily_fund = IndexCalculationPublic.monthly_fund
        distance_highest_result = DistanceHighestRate.distance_highest_rate(fund_daily_rate=daily_fund)
        print('距最高净值比计算结果为：', distance_highest_result)

    @unittest.skipIf(isskip == 0, '下行捕获率用例跳过')
    def test_down_capture(self):
        """计算下行捕获率测试用例，monthly_fund为基金月度收益率，benchmark_monthlys为基准月度收益率"""
        monthly_fund = IndexCalculationPublic.monthly_fund
        benchmark_monthlys = InvestmentCertificateBiomedical.benchmark_monthlys
        down_capture_result = DownCapture.down_capture(monthly_fund_field=monthly_fund,
                                                       benchmark_monthly=benchmark_monthlys)
        print('下行捕获率计算结果为：', down_capture_result)

    @unittest.skipIf(isskip == 0, '下行风险用例跳过')
    def test_downside_risk(self, isannual=True):
        """计算下行捕获率测试用例，monthly_fund为基金月度收益率，benchmark_monthlys为基准月度收益率"""
        monthly_fund = IndexCalculationPublic.monthly_fund
        risk_frees = IndexCalculationPublic.risk_frees
        downside_risk_result = DownsideRisk.downside_risk(monthly_fund_field=monthly_fund,
                                                          risk_free=risk_frees, isannual=isannual)
        print('下行风险计算结果为：', downside_risk_result)

    @unittest.skipIf(isskip == 0, '下行捕获收益率用例跳过')
    def test_downward_capture(self):
        monthly_fund = IndexCalculationPublic.monthly_fund
        benchmark_monthlys = InvestmentCertificateBiomedical.benchmark_monthlys
        downward_capture = DownwardCapture.downward_capture(monthly_fund_field=monthly_fund,
                                                            benchmark_monthly=benchmark_monthlys)
        print('下行捕获收益率计算结果：', downward_capture)

    @unittest.skipIf(isskip == 0, '信息比率用例跳过')
    def test_information_ratio(self):
        monthly_fund = IndexCalculationPublic.monthly_fund
        benchmark_monthlys = InvestmentCertificateBiomedical.benchmark_monthlys
        information_ratio_result = InformationRatio.information_ratio(monthly_fund_field=monthly_fund,
                                                                      benchmark_monthly=benchmark_monthlys,
                                                                      isannual=True)
        print('信息比率计算结果为：', information_ratio_result)

    @unittest.skipIf(isskip == 0, '詹森指数用例跳过')
    def test_jensen(self):
        monthly_fund = IndexCalculationPublic.monthly_fund
        benchmark_monthlys = InvestmentCertificateBiomedical.benchmark_monthlys
        risk_frees = IndexCalculationPublic.risk_frees
        jensen_result = Jensen.jensern(monthly_fund_field=monthly_fund, benchmark_monthly=benchmark_monthlys,
                                       risk_free=risk_frees, isannual=True)
        print('詹森指数计算结果为：', jensen_result)

    @unittest.skipIf(isskip == 0, '卡帕指数用例跳过')
    def test_kappa(self, isannual=True):
        startvalue = IndexCalculationPublic.start_fund
        endvalue = IndexCalculationPublic.end_fund
        monthly_fund = IndexCalculationPublic.monthly_fund
        year = IndexCalculationPublic.years
        risk_frees = IndexCalculationPublic.risk_frees
        kappa_result = Kappa.kappa(startvalue=startvalue, endvalue=endvalue, year=year,
                                   monthly_fund_field=monthly_fund, risk_free=risk_frees, isannual=isannual)
        print('卡帕计算结果为：', kappa_result)

    @unittest.skipIf(isskip == 0, '峰度计算用例跳过')
    def test_kurtosis(self):
        monthly_fund = IndexCalculationPublic.monthly_fund
        kurtosis_result = Kurtosis.kurtosis(month_fund_yield=monthly_fund)
        print('峰度计算结果为：', kurtosis_result)

    @unittest.skipIf(isskip == 0, '欧米伽用例跳过')
    def test_omega_ratio(self):
        startvalue = IndexCalculationPublic.start_fund
        endvalue = IndexCalculationPublic.end_fund
        monthly_fund = IndexCalculationPublic.monthly_fund
        year = IndexCalculationPublic.years
        risk_frees = IndexCalculationPublic.risk_frees
        omega_result = OmegaRtio.omega_ratio(startvalue=startvalue, endvalue=endvalue,
                                             year=year, risk_free_year=risk_frees, monthly_fund_field=monthly_fund)
        print('欧米伽计算结果为：', omega_result)

    @unittest.skipIf(isskip == 0, '区间收益率用例跳过')
    def test_range_return_rate(self, isannual=False):
        startvalue = IndexCalculationPublic.start_fund
        endvalue = IndexCalculationPublic.end_fund
        year = IndexCalculationPublic.years
        result = RangeReturnRate.annual_earnning(startvalue=startvalue,
                                                 endvalue=endvalue, isannual=isannual, years=year)
        print('区间收益率计算结果为', result)

    @unittest.skipIf(isskip == 0, '夏普用例跳过')
    def test_sharpe(self, isannual=True):
        monthly_fund = IndexCalculationPublic.monthly_fund
        risk_frees = IndexCalculationPublic.risk_frees
        sharp_result = Sharepe.sharpe(monthly_fund_field=monthly_fund, risk_free=risk_frees, isannual=isannual)
        print('夏普计算结果为：', sharp_result)

    @unittest.skipIf(isskip == 0, '偏度用例跳过')
    def test_skewness(self):
        monthly_fund = IndexCalculationPublic.monthly_fund
        skewness_result = Skewness.skewness(month_fund_yield=monthly_fund)
        print('偏度计算结果为：', skewness_result)

    @unittest.skipIf(isskip == 0, '索提诺用例跳过')
    def test_sotino_ratio(self, isannual=True):
        monthly_fund = IndexCalculationPublic.monthly_fund
        risk_frees = IndexCalculationPublic.risk_frees
        sotino_result = SotinoRatio.sotio_ratio(monthly_fund_field=monthly_fund, risk_free=risk_frees,
                                                isannual=isannual)
        print('索提诺计算结果为：', sotino_result)

    @unittest.skipIf(isskip == 0, '索提诺MAR用例跳过')
    def test_sotino_mar(self, isannual=True):
        monthly_fund = IndexCalculationPublic.monthly_fund
        risk_frees = IndexCalculationPublic.risk_frees
        sotio_mar_result = SotioRatioMar.sotio_ratio_mar(monthly_fund_field=monthly_fund, risk_free=risk_frees,
                                                         isannual=isannual)
        print('索提诺mar计算结果为：', sotio_mar_result)

    @unittest.skipIf(isskip == 0, '标准差用例跳过')
    def test_standard_deviation(self, isannual=True):
        monthly_fund = IndexCalculationPublic.monthly_fund
        standard_result = StandardDeviation.standard_deviation(month_earning_list=monthly_fund, is_annual=isannual)
        print('标准差计算结果为：', standard_result)

    @unittest.skipIf(isskip == 0, '胜率用例跳过')
    def test_success_rate(self):
        monthly_fund = IndexCalculationPublic.monthly_fund
        benchmark_monthlys = InvestmentCertificateBiomedical.benchmark_monthlys
        success_result = SuccessRate.success_rate(monthly_fund_field=monthly_fund, benchmark_monthly=benchmark_monthlys)
        print('胜率计算结果为：', success_result)

    @unittest.skipIf(isskip == 0, '跟踪误差用例跳过')
    def test_track_error(self, isannual=True):
        monthly_fund = IndexCalculationPublic.monthly_fund
        benchmark_monthlys = InvestmentCertificateBiomedical.benchmark_monthlys
        track_error_result = TrackError.track_error(monthly_fund_field=monthly_fund,
                                                    benchmark_monthly=benchmark_monthlys, isannual=isannual)
        print('跟踪误差计算结果为：', track_error_result)

    @unittest.skipIf(isskip == 0, '特雷诺用例跳过')
    def test_treynor(self):
        risk_frees = IndexCalculationPublic.risk_frees
        month_fund = IndexCalculationPublic.monthly_fund
        benchmark_monthlys = IndexCalculationPublic.benchmark_monthlys
        start_fund = IndexCalculationPublic.start_fund
        end_fund = IndexCalculationPublic.end_fund
        treynor_result = Treynor.treynor(risk_free_year=risk_frees, monthly_fund_field=month_fund,
                                         benchmark_monthly=benchmark_monthlys, startvalue=start_fund,
                                         endvalue=end_fund)
        print('特雷诺计算结果为：', treynor_result)

    @unittest.skipIf(isskip == 0, '上行捕获率用例跳过')
    def test_uplink_capture(self):
        month_fund = IndexCalculationPublic.monthly_fund
        benchmark_monthlys = IndexCalculationPublic.benchmark_monthlys
        uplink_capture_result = UplinkCapture.uplink_capture(monthly_fund_field=month_fund,
                                                             benchmark_monthly=benchmark_monthlys)
        print('上行捕获率计算结果为：', uplink_capture_result)

    @unittest.skipIf(isskip == 0, '上行捕获收益率用例跳过')
    def test_upward_capture(self):
        month_fund = IndexCalculationPublic.monthly_fund
        benchmark_monthlys = IndexCalculationPublic.benchmark_monthlys
        upward_capture_result = UpwardCapture.upward_capture(monthly_fund_field=month_fund,
                                                             benchmark_monthly=benchmark_monthlys)
        print('上行捕获收益率计算结果为：', upward_capture_result)


if __name__ == '__main__':
    dir_name = dir(IndexCalculationPublic)
    case_name = []
    suite = unittest.TestSuite()
    for value in dir_name:
        if value.startswith('test'):
            case_name.append(value)
            suite.addTest(IndexCalculationPublic(value))
    print(case_name)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
