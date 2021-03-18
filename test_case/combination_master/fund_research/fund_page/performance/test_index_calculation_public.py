# -*- coding: utf-8 -*-
""" 
@Time    : 2020/11/30 17:41
@Author  : liufubin
@FileName: test_index_calculation_public.py
@description: 指标计算调用公共方法(汇总指标计算)
"""
import unittest
from test_case.combination_master.fund_research.fund_page.performance import test_indicator_api
from public_method.indicator_calculation_method.alpha import Alpha
from public_method.indicator_calculation_method.beta import Beta
from public_method.indicator_calculation_method.calmar import Calmar
from public_method.indicator_calculation_method.biggest_monthly_down import BiggesrMonthlyDown
from public_method.indicator_calculation_method.distance_highest_rate import DistanceHighestRate
from public_method.indicator_calculation_method.down_capture import DownCapture
from public_method.indicator_calculation_method.downside_risk import DownsideRisk
from public_method.indicator_calculation_method.downward_capture import DownwardCapture
from public_method.indicator_calculation_method.information_ratio import InformationRatio
from public_method.indicator_calculation_method.jensen import Jensen
from public_method.indicator_calculation_method.kappa import Kappa
from public_method.indicator_calculation_method.kurtosis import Kurtosis
from public_method.indicator_calculation_method.omega_ratio import OmegaRtio
from public_method.indicator_calculation_method.range_return_rate import RangeReturnRate
from public_method.indicator_calculation_method.sharpe import Sharepe
from public_method.indicator_calculation_method.skewness import Skewness
from public_method.indicator_calculation_method.sotino_ratio import SotinoRatio
from public_method.indicator_calculation_method.sotino_ratio_MAR import SotioRatioMar
from public_method.indicator_calculation_method.standard_deviation import StandardDeviation
from public_method.indicator_calculation_method.success_rate import SuccessRate
from public_method.indicator_calculation_method.track_error import TrackError
from public_method.indicator_calculation_method.treynor import Treynor
from public_method.indicator_calculation_method.uplink_capture import UplinkCapture
from public_method.indicator_calculation_method.upward_capture import UpwardCapture
from request_date.combination_master.index_calculation_data import InvestmentCertificateBiomedical


class TestIndexCalculationPublic(unittest.TestCase):
    isskip = 1
    monthly_fund = InvestmentCertificateBiomedical.month_fund  # 获取的计算指标的月度收益率
    benchmark_monthlys = InvestmentCertificateBiomedical.benchmark_monthlys  # 获取的计算指标的基准收益率
    years = InvestmentCertificateBiomedical.years   # 获取的需要年化的年数
    risk_frees = 0.015   # 无风险收益率
    date_start_fund = InvestmentCertificateBiomedical.date_start_fund  # 获取需要的日频净值数据(carmar指标计算需要)
    date_end_fund = InvestmentCertificateBiomedical.date_end_fund  # 或许需要的日频净值数据(carmar指标计算需要)
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
        monthly_fund = TestIndexCalculationPublic.monthly_fund
        benchmark_monthlys = TestIndexCalculationPublic.benchmark_monthlys
        alpha_result = Alpha.alpha(monthly_fund_field=monthly_fund,
                                   benchmark_monthly=benchmark_monthlys, isannual=isannual)
        indicator_api_result = test_indicator_api.TestIndicator.combination_test_environment().json()
        api_alpha_result = float(indicator_api_result['data']['dataset'][0]['map']['Alpha'])
        self.assertTrue(round(alpha_result * 100, 2) == round(api_alpha_result * 100, 2), '计算的阿尔法与接口返回的结果不一致')
        print('阿尔法计算结果：', alpha_result)

    @unittest.skipIf(isskip == 0, '计算贝塔用例跳过')
    def test_calculate_beta(self):
        """计算贝塔测试用例，monthly_fund为基金月度收益率，benchmark_monthlys为基准月度收益率"""
        monthly_fund = TestIndexCalculationPublic.monthly_fund
        benchmark_monthlys = InvestmentCertificateBiomedical.benchmark_monthlys
        beta_result = Beta.beta(monthly_fund_field=monthly_fund, benchmark_monthly=benchmark_monthlys)
        indicator_api_result = test_indicator_api.TestIndicator.combination_test_environment().json()
        api_beta_result = float(indicator_api_result['data']['dataset'][0]['map']['Beta'])
        self.assertTrue(round(api_beta_result, 2) == round(beta_result, 2), '计算的贝塔与接口返回的结果不一致')
        print('贝塔计算结果：', beta_result)

    @unittest.skipIf(isskip == 0, '计算当月最大下跌用例跳过')
    def test_biggest_monthly_down(self):
        """计算当月最大下跌，monthly_fund为基金月度收益率"""
        monthly_fund = TestIndexCalculationPublic.monthly_fund
        down_min_result = BiggesrMonthlyDown.biggest_monthly_down(month_fund_yield=monthly_fund)
        print('当月最大下跌计算结果：', down_min_result)

    @unittest.skipIf(isskip == 0, '计算下跌月份比用例跳过')
    def test_down_month_ratio(self):
        """计算下跌月份比，monthly_fund为基金月度收益率"""
        monthly_fund = TestIndexCalculationPublic.monthly_fund
        down_rate_result = BiggesrMonthlyDown.down_month_ratio(month_fund_yield=monthly_fund)
        print('下跌月份比计算结果为：', down_rate_result)

    @unittest.skipIf(isskip == 0, '计算跑赢指数用例跳过')
    def test_batting_average(self):
        """计算跑赢指数（胜率），monthly_fund为基金月度收益率"""
        monthly_fund = TestIndexCalculationPublic.monthly_fund
        benchmark_monthlys = InvestmentCertificateBiomedical.benchmark_monthlys
        win_rate_result = BiggesrMonthlyDown.batting_average(monthly_fund_field=monthly_fund,
                                                             benchmark_monthly=benchmark_monthlys)
        indicator_api_result = test_indicator_api.TestIndicator.combination_test_environment().json()
        api_winrate_result = float(indicator_api_result['data']['dataset'][0]['map']['WinRate'])
        self.assertTrue(round(api_winrate_result * 100, 2) == round(win_rate_result * 100, 2), '计算的胜率与接口返回的结果不一致')
        print('胜率计算结果为：', win_rate_result)

    @unittest.skipIf(isskip == 0, '计算盈亏比用例跳过')
    def tset_profit_loss_ratio(self):
        """计算盈亏比，monthly_fund为基金月度收益率"""
        monthly_fund = TestIndexCalculationPublic.monthly_fund
        prolit_loss_result = BiggesrMonthlyDown.profit_loss_ratio(monthly_fund_field=monthly_fund)
        print('盈亏比计算结果：', prolit_loss_result)

    @unittest.skipIf(isskip == 0, '计算卡玛用例跳过')
    def test_calculate_calmar(self):
        """计算卡玛测试用例，monthly_fund为基金月度收益率，benchmark_monthlys为基准月度收益率"""
        date_start_value = TestIndexCalculationPublic.date_start_fund
        date_end_value = TestIndexCalculationPublic.date_end_fund
        fund_net_value = TestIndexCalculationPublic.monthly_fund
        max_fund = 1.069973   # 计算最大回撤的最高点
        min_fund = 0.940556   # 计算最大回撤的最低点
        calmar_result = Calmar.calmar(startvalue=date_start_value, endvalue=date_end_value, max_fund=max_fund,
                                      min_fund=min_fund, valuedates=362, fund_net_value=fund_net_value)
        print(calmar_result)
        indicator_api_result = test_indicator_api.TestIndicator.combination_test_environment().json()
        api_calmar_result = float(indicator_api_result['data']['dataset'][0]['map']['CalmarRatio'])
        print(api_calmar_result)
        self.assertTrue(round(calmar_result, 2) == round(api_calmar_result, 2), '计算的calmar与接口返回的结果不一致')
        print('卡玛计算结果：', calmar_result)

    @unittest.skipIf(isskip == 0, '距最高净值比用例跳过')
    def test_distance_highest_rate(self):
        """计算距最高净值比，daily_fund为基金日频净值列表"""
        daily_fund = TestIndexCalculationPublic.monthly_fund
        distance_highest_result = DistanceHighestRate.distance_highest_rate(fund_daily_rate=daily_fund)
        print('距最高净值比计算结果为：', distance_highest_result)

    @unittest.skipIf(isskip == 0, '下行捕获率用例跳过')
    def test_down_capture(self):
        """计算下行捕获率测试用例，monthly_fund为基金月度收益率，benchmark_monthlys为基准月度收益率"""
        monthly_fund = TestIndexCalculationPublic.monthly_fund
        benchmark_monthlys = InvestmentCertificateBiomedical.benchmark_monthlys
        down_capture_result = DownCapture.down_capture(monthly_fund_field=monthly_fund,
                                                       benchmark_monthly=benchmark_monthlys)
        indicator_api_result = test_indicator_api.TestIndicator.combination_test_environment().json()
        api_down_capture_result = float(indicator_api_result['data']['dataset'][0]['map']['DownCaptureRatio'])
        self.assertTrue(round(down_capture_result, 2) == round(api_down_capture_result, 2), '计算的下行捕获率与接口返回的结果不一致')
        print('下行捕获率计算结果为：', down_capture_result)

    @unittest.skipIf(isskip == 0, '下行风险用例跳过')
    def test_downside_risk(self, isannual=True):
        """计算下行风险测试用例，monthly_fund为基金月度收益率，benchmark_monthlys为基准月度收益率"""
        monthly_fund = TestIndexCalculationPublic.monthly_fund
        risk_frees = TestIndexCalculationPublic.risk_frees
        downside_risk_result = DownsideRisk.downside_risk(monthly_fund_field=monthly_fund,
                                                          risk_free=risk_frees, isannual=isannual)
        indicator_api_result = test_indicator_api.TestIndicator.combination_test_environment().json()
        api_downside_risk_result = float(indicator_api_result['data']['dataset'][0]['map']['DownsideStdDev'])
        self.assertTrue(round(api_downside_risk_result * 100, 2) == round(downside_risk_result * 100, 2),
                        '计算的下行风险与接口返回的结果不一致')
        print('下行风险计算结果为：', downside_risk_result)

    @unittest.skipIf(isskip == 0, '下行捕获收益率用例跳过')
    def test_downward_capture(self):
        """计算下行下行捕获收益测试用例，monthly_fund为基金月度收益率，benchmark_monthlys为基准月度收益率"""
        monthly_fund = TestIndexCalculationPublic.monthly_fund
        benchmark_monthlys = InvestmentCertificateBiomedical.benchmark_monthlys
        downward_capture = DownwardCapture.downward_capture(monthly_fund_field=monthly_fund,
                                                            benchmark_monthly=benchmark_monthlys)
        indicator_api_result = test_indicator_api.TestIndicator.combination_test_environment().json()
        api_down_capture_result = float(indicator_api_result['data']['dataset'][0]['map']['DownCaptureReturn'])
        self.assertTrue(round(api_down_capture_result * 100, 2) == round(downward_capture * 100, 2),
                        '计算的下行捕获收益率与接口返回的结果不一致')
        print('下行捕获收益率计算结果：', downward_capture)

    @unittest.skipIf(isskip == 0, '信息比率用例跳过')
    def test_information_ratio(self):
        """计算信息比率测试用例，monthly_fund为基金月度收益率，benchmark_monthlys为基准月度收益率"""
        monthly_fund = TestIndexCalculationPublic.monthly_fund
        benchmark_monthlys = InvestmentCertificateBiomedical.benchmark_monthlys
        information_ratio_result = InformationRatio.information_ratio(monthly_fund_field=monthly_fund,
                                                                      benchmark_monthly=benchmark_monthlys,
                                                                      isannual=True)
        indicator_api_result = test_indicator_api.TestIndicator.combination_test_environment().json()
        api_information_result = float(indicator_api_result['data']['dataset'][0]['map']['InformationRatio'])
        self.assertTrue(round(api_information_result, 2) == round(information_ratio_result, 2),
                        '计算的信息比率与接口返回的结果不一致')
        print('信息比率计算结果为：', information_ratio_result)

    @unittest.skipIf(isskip == 0, '詹森指数用例跳过')
    def test_jensen(self):
        """计算詹森比率测试用例，monthly_fund为基金月度收益率，benchmark_monthlys为基准月度收益率"""
        monthly_fund = TestIndexCalculationPublic.monthly_fund
        benchmark_monthlys = InvestmentCertificateBiomedical.benchmark_monthlys
        risk_frees = TestIndexCalculationPublic.risk_frees
        jensen_result = Jensen.jensern(monthly_fund_field=monthly_fund, benchmark_monthly=benchmark_monthlys,
                                       risk_free=risk_frees, isannual=True)
        indicator_api_result = test_indicator_api.TestIndicator.combination_test_environment().json()
        api_jensen_result = float(indicator_api_result['data']['dataset'][0]['map']['Jensen'])
        self.assertTrue(round(jensen_result * 100, 2) == round(api_jensen_result * 100, 2),
                        '计算的詹森指数与接口返回的结果不一致')
        print('詹森指数计算结果为：', jensen_result)

    @unittest.skipIf(isskip == 0, '卡帕指数用例跳过')
    def test_kappa(self, isannual=True):
        """计算卡帕指数测试用例，monthly_fund为基金月度收益率，benchmark_monthlys为基准月度收益率"""
        startvalue = TestIndexCalculationPublic.start_fund
        endvalue = TestIndexCalculationPublic.end_fund
        monthly_fund = TestIndexCalculationPublic.monthly_fund
        risk_frees = TestIndexCalculationPublic.risk_frees
        kappa_result = Kappa.kappa(startvalue=startvalue, endvalue=endvalue, yesrs=1,
                                   monthly_fund_field=monthly_fund, risk_free=risk_frees, isannual=isannual)
        indicator_api_result = test_indicator_api.TestIndicator.combination_test_environment().json()
        api_kappa_result = float(indicator_api_result['data']['dataset'][0]['map']['Kappa'])
        self.assertTrue(round(kappa_result, 2) == round(api_kappa_result, 2),
                        '计算的卡帕与接口返回的结果不一致')
        print('卡帕计算结果为：', kappa_result)

    @unittest.skipIf(isskip == 0, '峰度计算用例跳过')
    def test_kurtosis(self):
        """计算峰度测试用例，monthly_fund为基金月度收益率，benchmark_monthlys为基准月度收益率"""
        monthly_fund = TestIndexCalculationPublic.monthly_fund
        kurtosis_result = Kurtosis.kurtosis(month_fund_yield=monthly_fund)
        indicator_api_result = test_indicator_api.TestIndicator.combination_test_environment().json()
        api_kurtosis_result = float(indicator_api_result['data']['dataset'][0]['map']['Kurtosis'])
        self.assertTrue(round(kurtosis_result, 2) == round(api_kurtosis_result, 2),
                        '计算的卡帕与接口返回的结果不一致')
        print('峰度计算结果为：', kurtosis_result)

    @unittest.skipIf(isskip == 0, '欧米伽用例跳过')
    def test_omega_ratio(self):
        """计算下欧米伽测试用例，monthly_fund为基金月度收益率，benchmark_monthlys为基准月度收益率"""
        startvalue = TestIndexCalculationPublic.start_fund
        endvalue = TestIndexCalculationPublic.end_fund
        monthly_fund = TestIndexCalculationPublic.monthly_fund
        risk_frees = TestIndexCalculationPublic.risk_frees
        omega_result = OmegaRtio.omega_ratio(startvalue=startvalue, endvalue=endvalue,
                                             valuedates=365, risk_free_year=risk_frees, monthly_fund_field=monthly_fund)
        indicator_api_result = test_indicator_api.TestIndicator.combination_test_environment().json()
        api_omega_result = float(indicator_api_result['data']['dataset'][0]['map']['Omega'])
        self.assertTrue(round(omega_result, 2) == round(api_omega_result, 2),
                        '计算的欧米伽与接口返回的结果不一致')
        print('欧米伽计算结果为：', omega_result)

    @unittest.skipIf(isskip == 0, '区间收益率用例跳过')
    def test_interval_return_rate(self, isannual=False):
        """计算区间收益测试用例，monthly_fund为基金月度收益率，benchmark_monthlys为基准月度收益率"""
        startvalue = TestIndexCalculationPublic.start_fund
        endvalue = TestIndexCalculationPublic.end_fund
        interval_return_result = RangeReturnRate.annual_earnning_dates(startvalue=startvalue, endvalue=endvalue,
                                                                       isannual=isannual, valuedates=365)
        indicator_api_result = test_indicator_api.TestIndicator.combination_test_environment().json()
        api_interval_return_result = float(indicator_api_result['data']['dataset'][0]['map']['IntervalReturn'])
        self.assertTrue(round(interval_return_result * 100, 2) == round(api_interval_return_result * 100, 2),
                        '计算的区间收益与接口返回的结果不一致')
        print('区间收益率计算结果为', interval_return_result)

    @unittest.skipIf(isskip == 0, '区间收益率年化用例跳过')
    def test_interval_return_rate_annual(self, isannual=True):
        """计算下区间年化收益测试用例，monthly_fund为基金月度收益率，benchmark_monthlys为基准月度收益率"""
        startvalue = TestIndexCalculationPublic.start_fund
        endvalue = TestIndexCalculationPublic.end_fund
        interval_return_result = RangeReturnRate.annual_earnning_dates(startvalue=startvalue, endvalue=endvalue,
                                                                       isannual=isannual, valuedates=365)
        indicator_api_result = test_indicator_api.TestIndicator.combination_test_environment().json()
        api_interval_return_result = float(indicator_api_result['data']['dataset'][0]['map']['AnnualReturn'])
        self.assertTrue(round(interval_return_result * 100, 2) == round(api_interval_return_result * 100, 2),
                        '计算的年化收益与接口返回的结果不一致')
        print('年化收益率计算结果为', interval_return_result)

    @unittest.skipIf(isskip == 0, '夏普用例跳过')
    def test_sharpe(self, isannual=True):
        """计算夏普比率测试用例，monthly_fund为基金月度收益率，benchmark_monthlys为基准月度收益率"""
        monthly_fund = TestIndexCalculationPublic.monthly_fund
        risk_frees = TestIndexCalculationPublic.risk_frees
        sharp_result = Sharepe.sharpe(monthly_fund_field=monthly_fund, risk_free=risk_frees, isannual=isannual)
        indicator_api_result = test_indicator_api.TestIndicator.combination_test_environment().json()
        api_sharpe_result = float(indicator_api_result['data']['dataset'][0]['map']['SharpeRatio'])
        self.assertTrue(round(sharp_result, 2) == round(api_sharpe_result, 2),
                        '计算的夏普比率与接口返回的结果不一致')
        print('夏普计算结果为：', sharp_result)

    @unittest.skipIf(isskip == 0, '偏度用例跳过')
    def test_skewness(self):
        """计算偏度测试用例，monthly_fund为基金月度收益率，benchmark_monthlys为基准月度收益率"""
        monthly_fund = TestIndexCalculationPublic.monthly_fund
        skewness_result = Skewness.skewness(month_fund_yield=monthly_fund)
        indicator_api_result = test_indicator_api.TestIndicator.combination_test_environment().json()
        api_skewness_result = float(indicator_api_result['data']['dataset'][0]['map']['Skewness'])
        self.assertTrue(round(skewness_result, 2) == round(api_skewness_result, 2),
                        '计算的偏度比率与接口返回的结果不一致')
        print('偏度计算结果为：', skewness_result)

    @unittest.skipIf(isskip == 0, '索提诺用例跳过')
    def test_sotino_ratio(self, isannual=True):
        """计算索提诺比率测试用例，monthly_fund为基金月度收益率，benchmark_monthlys为基准月度收益率"""
        monthly_fund = TestIndexCalculationPublic.monthly_fund
        risk_frees = TestIndexCalculationPublic.risk_frees
        sotino_result = SotinoRatio.sotio_ratio(monthly_fund_field=monthly_fund, risk_free=risk_frees,
                                                isannual=isannual)
        indicator_api_result = test_indicator_api.TestIndicator.combination_test_environment().json()
        api_sotino_result = float(indicator_api_result['data']['dataset'][0]['map']['SortinoRatio'])
        self.assertTrue(round(sotino_result, 2) == round(api_sotino_result, 2),
                        '计算的索提诺比率与接口返回的结果不一致')
        print('索提诺计算结果为：', sotino_result)

    @unittest.skipIf(isskip == 0, '索提诺MAR用例跳过')
    def test_sotino_mar(self, isannual=True):
        """计算索提诺MAR测试用例，monthly_fund为基金月度收益率，benchmark_monthlys为基准月度收益率"""
        monthly_fund = TestIndexCalculationPublic.monthly_fund
        risk_frees = TestIndexCalculationPublic.risk_frees
        sotio_mar_result = SotioRatioMar.sotio_ratio_mar(monthly_fund_field=monthly_fund, risk_free=risk_frees,
                                                         isannual=isannual)
        indicator_api_result = test_indicator_api.TestIndicator.combination_test_environment().json()
        api_sotino_mar_result = float(indicator_api_result['data']['dataset'][0]['map']['SortinoRatioMAR'])
        self.assertTrue(round(sotio_mar_result, 2) == round(api_sotino_mar_result, 2),
                        '计算的索提诺比率(MAR)与接口返回的结果不一致')
        print('索提诺mar计算结果为：', sotio_mar_result)

    @unittest.skipIf(isskip == 0, '标准差用例跳过')
    def test_standard_deviation(self, isannual=True):
        """计算标准差测试用例，monthly_fund为基金月度收益率，benchmark_monthlys为基准月度收益率"""
        monthly_fund = TestIndexCalculationPublic.monthly_fund
        standard_annual_result = StandardDeviation.standard_deviation(month_earning_list=monthly_fund,
                                                                      is_annual=isannual)
        indicator_api_result = test_indicator_api.TestIndicator.combination_test_environment().json()
        api_standard_annual_result = float(indicator_api_result['data']['dataset'][0]['map']['AnnualStdDev'])
        self.assertTrue(round(standard_annual_result * 100, 2) == round(api_standard_annual_result * 100, 2),
                        '计算的年化标准差与接口返回的结果不一致')
        print('标准差计算结果为：', standard_annual_result)

    @unittest.skipIf(isskip == 0, '胜率用例跳过')
    def test_success_rate(self):
        """计算胜率测试用例，monthly_fund为基金月度收益率，benchmark_monthlys为基准月度收益率"""
        monthly_fund = TestIndexCalculationPublic.monthly_fund
        benchmark_monthlys = InvestmentCertificateBiomedical.benchmark_monthlys
        success_result = SuccessRate.success_rate(monthly_fund_field=monthly_fund, benchmark_monthly=benchmark_monthlys)
        indicator_api_result = test_indicator_api.TestIndicator.combination_test_environment().json()
        api_winrate_result = float(indicator_api_result['data']['dataset'][0]['map']['WinRate'])
        self.assertTrue(round(api_winrate_result * 100, 2) == round(success_result * 100, 2), '计算的胜率与接口返回的结果不一致')
        print('胜率计算结果为：', success_result)

    @unittest.skipIf(isskip == 0, '跟踪误差用例跳过')
    def test_track_error(self, isannual=True):
        """计算跟踪误差测试用例，monthly_fund为基金月度收益率，benchmark_monthlys为基准月度收益率"""
        monthly_fund = TestIndexCalculationPublic.monthly_fund
        benchmark_monthlys = InvestmentCertificateBiomedical.benchmark_monthlys
        track_error_result = TrackError.track_error(monthly_fund_field=monthly_fund,
                                                    benchmark_monthly=benchmark_monthlys, isannual=isannual)
        indicator_api_result = test_indicator_api.TestIndicator.combination_test_environment().json()
        api_track_error_result = float(indicator_api_result['data']['dataset'][0]['map']['TrackingError'])
        self.assertTrue(round(track_error_result * 100, 2) == round(api_track_error_result * 100, 2),
                        '计算的跟踪误差与接口返回的结果不一致')
        print('跟踪误差计算结果为：', track_error_result)

    @unittest.skipIf(isskip == 0, '特雷诺用例跳过')
    def test_treynor(self):
        """计算特雷诺测试用例，monthly_fund为基金月度收益率，benchmark_monthlys为基准月度收益率"""
        risk_frees = TestIndexCalculationPublic.risk_frees
        month_fund = TestIndexCalculationPublic.monthly_fund
        benchmark_monthlys = TestIndexCalculationPublic.benchmark_monthlys
        start_fund = TestIndexCalculationPublic.start_fund
        end_fund = TestIndexCalculationPublic.end_fund
        treynor_result = Treynor.treynor(risk_free_year=risk_frees, monthly_fund_field=month_fund,
                                         benchmark_monthly=benchmark_monthlys, startvalue=start_fund,
                                         endvalue=end_fund)
        indicator_api_result = test_indicator_api.TestIndicator.combination_test_environment().json()
        api_treynor_result = float(indicator_api_result['data']['dataset'][0]['map']['TreynorRatio'])
        self.assertTrue(round(treynor_result, 2) == round(api_treynor_result, 2),
                        '计算的特雷诺比率与接口返回的结果不一致')
        print('特雷诺计算结果为：', treynor_result)

    @unittest.skipIf(isskip == 0, '上行捕获率用例跳过')
    def test_uplink_capture(self):
        """计算上行捕获率测试用例，monthly_fund为基金月度收益率，benchmark_monthlys为基准月度收益率"""
        month_fund = TestIndexCalculationPublic.monthly_fund
        benchmark_monthlys = TestIndexCalculationPublic.benchmark_monthlys
        uplink_capture_result = UplinkCapture.uplink_capture(monthly_fund_field=month_fund,
                                                             benchmark_monthly=benchmark_monthlys)
        indicator_api_result = test_indicator_api.TestIndicator.combination_test_environment().json()
        api_upcapture_result = float(indicator_api_result['data']['dataset'][0]['map']['UpCaptureRatio'])
        self.assertTrue(round(uplink_capture_result, 2) == round(api_upcapture_result, 2),
                        '计算的上行捕获率与接口返回的结果不一致')
        print('上行捕获率计算结果为：', uplink_capture_result)

    @unittest.skipIf(isskip == 0, '上行捕获收益率用例跳过')
    def test_upward_capture(self):
        """计算上行捕获收益率测试用例，monthly_fund为基金月度收益率，benchmark_monthlys为基准月度收益率"""
        month_fund = TestIndexCalculationPublic.monthly_fund
        benchmark_monthlys = TestIndexCalculationPublic.benchmark_monthlys
        upward_capture_result = UpwardCapture.upward_capture(monthly_fund_field=month_fund,
                                                             benchmark_monthly=benchmark_monthlys)
        indicator_api_result = test_indicator_api.TestIndicator.combination_test_environment().json()
        api_upcapture_result = float(indicator_api_result['data']['dataset'][0]['map']['UpCaptureReturn'])
        self.assertTrue(round(upward_capture_result, 2) == round(api_upcapture_result, 2),
                        '计算的上行捕获收益率与接口返回的结果不一致')
        print('上行捕获收益率计算结果为：', upward_capture_result)

    @staticmethod
    def owner_calculation_result_dict():
        """计算指标汇总成字典展示"""
        # risk_frees = TestIndexCalculationPublic.risk_frees
        month_fund = TestIndexCalculationPublic.monthly_fund
        benchmark_monthlys = TestIndexCalculationPublic.benchmark_monthlys
        start_fund = TestIndexCalculationPublic.start_fund
        end_fund = TestIndexCalculationPublic.end_fund
        owner_calculation_dict = dict()
        owner_calculation_dict['Alpha'] = Alpha.alpha(monthly_fund_field=month_fund,
                                                      benchmark_monthly=benchmark_monthlys, isannual=True)
        owner_calculation_dict['IntervalReturn'] = RangeReturnRate.annual_earnning_dates(startvalue=start_fund,
                                                                                         endvalue=end_fund,
                                                                                         isannual=False,
                                                                                         valuedates=365)


if __name__ == '__main__':
    dir_name = dir(TestIndexCalculationPublic)
    case_name = []
    suite = unittest.TestSuite()
    for value in dir_name:
        if value.startswith('test'):
            case_name.append(value)
            suite.addTest(TestIndexCalculationPublic(value))
    print(case_name)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
