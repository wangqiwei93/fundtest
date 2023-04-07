import pytest
import allure
import re
from operation.fundmapmain import get_fundOverviewChildEvolute_fundState
from testcases.conftest import api_data, api_data_sql
from common.logger import logger
from common.mysql_operate import db


@allure.step("步骤1 ==>> 子基金-数据总览")
def step_1(year):
    logger.info("步骤1 ==>> 子基金-数据总览：{}".format(year))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("基金总览")
@allure.feature("子基金-数据总览")
class TestGetMother():
    @allure.story('用例--子基金-数据总览')
    @allure.description("该用例是针对子基金-数据总览的测试")
    @allure.issue("https://yzw.corptssl.com/fundOverview/fundOverviewData", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://yzw.corptssl.com/fundOverview/fundOverviewData", name="点击，跳转到对应用例的链接地址")
    @allure.title("测试数据：【 {year},{areaId},{areaName},{isSelf},{except_result},{except_code},{except_msg},{sql}】")
    @pytest.mark.single
    @pytest.mark.parametrize("year, areaId, areaName, isSelf, except_result, except_code, except_msg",
                             api_data["test_overview_year_city"])
    @pytest.mark.parametrize("sql", api_data_sql["test_overview_fundState_sql"])
    def test_get_mother(self, year, areaId, areaName, isSelf, except_result, except_code, except_msg, sql):
        logger.info("*************** 开始执行用例 ***************")
        result = get_fundOverviewChildEvolute_fundState(year, areaId, areaName, isSelf)
        step_1(year)
        if result.code == 401:
            logger.info("***************token失效 结束执行用例 ***************")
        else:
            # isSelf:1本级0市
            for i in range(0, len(sql)):
                if year == sql[i][0] and isSelf == 0:
                    sql_data = sql[i][1]
                    break
                elif year == sql[i][0] and isSelf == 1:
                    sql_data = sql[i][2]
                    break
            """
                sumMoney:全省财政总认缴
                sumMoneyTwo:全省财政总实缴    
                fundCount:占比       
            """
            data_list = db.select_db(sql_data)
            result_data = result.response.json()['data']
            # 母基金 fundcount
            for data_city_i in range(len(data_list)):
                if data_list[data_city_i]["data_city"] == areaName:
                    # 子基金
                    assert int(data_list[data_city_i]["子基金"]) == int(
                        result_data['fundCount']['sumData']), result.error
                    assert int(data_list[data_city_i]["子基金去年年末"]) == int(
                        result_data['fundCount']['lastYearData']), result.error
                    assert int(data_list[data_city_i]["子基金本年新增"]) == int(
                        result_data['fundCount']['toYearData']), result.error
                    # 总规模
                    assert float(data_list[data_city_i]["总规模"] - 1) <= float(
                        result_data['fundScale']['sumData']) <= float(
                        data_list[data_city_i]["总规模"] + 2), result.error
                    assert float(data_list[data_city_i]["总规模本年新增"] - 1) <= float(
                        result_data['fundScale']['toYearData']) <= float(
                        data_list[data_city_i]["总规模本年新增"] + 2), result.error
                    assert float(data_list[data_city_i]["总规模去年年末"] - 1) <= float(
                        result_data['fundScale']['lastYearData']) <= float(
                        data_list[data_city_i]["总规模去年年末"] + 2), result.error
                    # 产业基金出资额
                    assert float(data_list[data_city_i]["产业基金出资额"] - 1) <= float(
                        result_data['masterAmount']['sumData']) <= float(
                        data_list[data_city_i]["产业基金出资额"] + 2), result.error
                    assert float(data_list[data_city_i]["产业基金出资额本年新增"] - 1) <= float(
                        result_data['masterAmount']['toYearData']) <= float(
                        data_list[data_city_i]["产业基金出资额本年新增"] + 2), result.error
                    assert float(data_list[data_city_i]["产业基金出资额去年年末"] - 1) <= float(
                        result_data['masterAmount']['lastYearData']) <= float(
                        data_list[data_city_i]["产业基金出资额去年年末"] + 2), result.error
                    # 社会资本出资额
                    assert float(data_list[data_city_i]["社会资本出资额"] - 1) <= float(
                        result_data['socialAmount']['sumData']) <= float(
                        data_list[data_city_i]["社会资本出资额"] + 2), result.error
                    assert float(data_list[data_city_i]["社会资本出资额本年新增"] - 1) <= float(
                        result_data['socialAmount']['toYearData']) <= float(
                        data_list[data_city_i]["社会资本出资额本年新增"] + 2), result.error
                    assert float(data_list[data_city_i]["社会资本出资额去年年末"] - 1) <= float(
                        result_data['socialAmount']['lastYearData']) <= float(
                        data_list[data_city_i]["社会资本出资额去年年末"] + 2), result.error
                    # 累计认缴投资额
                    assert float(data_list[data_city_i]["累计投资额"] - 1) <= float(
                        result_data['sumInvestAmount']['sumData']) <= float(
                        data_list[data_city_i]["累计投资额"] + 2), result.error
                    assert float(data_list[data_city_i]["累计投资额本年新增"] - 1) <= float(
                        result_data['sumInvestAmount']['toYearData']) <= float(
                        data_list[data_city_i]["累计投资额本年新增"] + 2), result.error
                    assert float(data_list[data_city_i]["累计投资额去年年末"] - 1) <= float(
                        result_data['sumInvestAmount']['lastYearData']) <= float(
                        data_list[data_city_i]["累计投资额去年年末"] + 2), result.error
                    assert float(data_list[data_city_i]["占比"] - 1) <= float(
                        result_data['sumInvestAmount']['rate']) <= float(
                        data_list[data_city_i]["占比"] + 2), result.error
            assert result.success == except_result, result.error
            assert result.code == except_code, result.error
            assert result.success == except_result, result.error
            logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
            assert result.response.json().get("code") == except_code
            assert except_msg in result.msg
            logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_overview_05_fundOverviewChildEvolute_fundState.py"])
