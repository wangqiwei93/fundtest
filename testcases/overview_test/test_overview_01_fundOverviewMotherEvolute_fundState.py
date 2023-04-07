import pytest
import allure
import re
from operation.fundmapmain import get_fundOverviewMotherEvolute_fundState
from testcases.conftest import api_data, api_data_sql
from common.logger import logger
from common.mysql_operate import db


@allure.step("步骤1 ==>> 母基金-数据总览")
def step_1(year):
    logger.info("步骤1 ==>> 母基金-数据总览：{}".format(year))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("基金总览")
@allure.feature("母基金-数据总览")
class TestGetMother():
    @allure.story('用例--母基金-数据总览')
    @allure.description("该用例是针对母基金-数据总览的测试")
    @allure.issue("https://yzw.corptssl.com/fundOverview/fundOverviewData", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://yzw.corptssl.com/fundOverview/fundOverviewData", name="点击，跳转到对应用例的链接地址")
    @allure.title(
        "测试数据：【 {year},{areaId},{areaName},{isSelf},{except_result},{except_code},{except_msg},{fund_type_0_sql}】")
    @pytest.mark.single
    @pytest.mark.parametrize("year, areaId, areaName, isSelf, except_result, except_code, except_msg",
                             api_data["test_overview_year_city"])
    @pytest.mark.parametrize("fund_type_0_sql", api_data_sql["test_overview_fundtype_0_sql"])
    def test_get_mother(self, year, areaId, areaName, isSelf, except_result, except_code, except_msg, fund_type_0_sql):
        logger.info("*************** 开始执行用例 ***************")
        result = get_fundOverviewMotherEvolute_fundState(year, areaId, areaName, isSelf)
        step_1(year)
        if result.code == 401:
            logger.info("***************token失效 结束执行用例 ***************")
        else:
            # isSelf:1本级0市
            for i in range(0, len(fund_type_0_sql)):
                if year == fund_type_0_sql[i][0] and isSelf == 0:
                    sql_data = fund_type_0_sql[i][1]
                    break
                elif year == fund_type_0_sql[i][0] and isSelf == 1:
                    sql_data = fund_type_0_sql[i][2]
                    break
            """
                sumMoney:全省财政总认缴
                sumMoneyTwo:全省财政总实缴    
                fundCount:占比       
            """
            sql_data_list = db.select_db(sql_data)
            result_data = result.response.json()['data']
            # 母基金 fundcount
            for data_city_i in range(len(sql_data_list)):
                if sql_data_list[data_city_i]["data_city"] == areaName:
                    # 母基金
                    assert int(sql_data_list[data_city_i]["母基金"]) == int(
                        result_data['fundCount']['sumData']), result.error
                    assert int(sql_data_list[data_city_i]["去年年末"]) == int(
                        result_data['fundCount']['lastYearData']), result.error
                    assert int(sql_data_list[data_city_i]["本年新增"]) == int(
                        result_data['fundCount']['toYearData']), result.error
                    # 财政认缴
                    assert float(sql_data_list[data_city_i]["总财政认缴"]) == float(
                        result_data['fundScale']['sumData']), result.error
                    assert float(sql_data_list[data_city_i]["财政认缴本年新增"]) == float(
                        result_data['fundScale']['toYearData']), result.error
                    assert round(float(sql_data_list[data_city_i]["财政认缴年末"]),0) == round(float(
                        result_data['fundScale']['lastYearData']),0), result.error
                    # 财政实缴
                    assert float(sql_data_list[data_city_i]["财政本年实缴"]) == float(
                        result_data['completeAmount']['sumData']), result.error
                    assert round(float(sql_data_list[data_city_i]["财政实缴新增"]),0) == round(float(
                        result_data['completeAmount']['toYearData']),0), result.error
                    assert float(sql_data_list[data_city_i]["财政实缴去年年末"]) == float(
                        result_data['completeAmount']['lastYearData']), result.error
                    # 撬动社会资本
                    assert float(sql_data_list[data_city_i]["撬动社会资本"]) == float(
                        result_data['socialAmount']['sumData']), result.error
                    assert float(sql_data_list[data_city_i]["撬动社会资本本年新增"]) == float(
                        result_data['socialAmount']['toYearData']), result.error
                    assert float(sql_data_list[data_city_i]["撬动社会资本去年年末"]) == float(
                        result_data['socialAmount']['lastYearData']), result.error
                    # 累计认缴投资额
                    assert float(sql_data_list[data_city_i]["累计认缴投资额"]) == float(
                        result_data['govPreAmount']['sumData']), result.error
                    assert float(sql_data_list[data_city_i]["累计认缴投资额本年新增"]) == float(
                        result_data['govPreAmount']['toYearData']), result.error
                    assert float(sql_data_list[data_city_i]["累计认缴投资额去年年末"]) == float(
                        result_data['govPreAmount']['lastYearData']), result.error
                    # 累计实缴投资额
                    assert float(sql_data_list[data_city_i]["累计实缴投资额"]) == float(
                        result_data['govRealAmount']['sumData']), result.error
                    assert round(float(sql_data_list[data_city_i]["累计实缴投资额本年新增"]), 0) == round(float(
                        result_data['govRealAmount']['toYearData']), 0), result.error
                    assert float(sql_data_list[data_city_i]["累计实缴投资额去年年末"]) == float(
                        result_data['govRealAmount']['lastYearData']), result.error
                    # 下设子基金
                    assert int(sql_data_list[data_city_i]["下设子基金总数"]) == int(
                        result_data['childAmount']['sumData']), result.error
                    assert int(sql_data_list[data_city_i]["下设子基金本年新增"]) == int(
                        result_data['childAmount']['toYearData']), result.error
                    assert int(sql_data_list[data_city_i]["下设子基金去年年末"]) == int(
                        result_data['childAmount']['lastYearData']), result.error
                    # 直投项目
                    assert int(sql_data_list[data_city_i]["直投项目"]) == int(
                        result_data['proAmount']['sumData']), result.error
                    assert int(sql_data_list[data_city_i]["直投项目本年新增"]) == int(
                        result_data['proAmount']['toYearData']), result.error
                    assert int(sql_data_list[data_city_i]["直投项目去年年末"]) == int(
                        result_data['proAmount']['lastYearData']), result.error
                    assert float(sql_data_list[data_city_i]["产业基金认缴出资额"]) == float(
                        result_data['proAmount']['rate']), result.error

            # print(db.select_db(sql_data))
            # print(result.response.json()['data']['fundScale']['sumData'])
            # print(type(float(result.response.json()['data']['fundScale']['sumData'])))
            assert result.success == except_result, result.error
            assert result.code == except_code, result.error
            assert result.success == except_result, result.error
            logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
            assert result.response.json().get("code") == except_code
            assert except_msg in result.msg
            logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_overview_01_fundOverviewMotherEvolute_fundState.py"])
