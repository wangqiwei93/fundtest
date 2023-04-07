import pytest
import allure
import re
from operation.fundmapmain import get_fundOverviewChildEvolute_investProgress
from testcases.conftest import api_data, api_data_sql
from common.logger import logger
from common.mysql_operate import db


@allure.step("步骤1 ==>> 子基金-各地子基金投资进度")
def step_1(year):
    logger.info("步骤1 ==>> 子基金-各地子基金投资进度：{}".format(year))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("基金总览")
@allure.feature("子基金-各地子基金投资进度")
class TestGetMother():
    @allure.story('用例--子基金-各地子基金投资进度')
    @allure.description("该用例是针对子基金-各地子基金投资进度的测试")
    @allure.issue("https://yzw.corptssl.com/fundOverview/fundOverviewData", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://yzw.corptssl.com/fundOverview/fundOverviewData", name="点击，跳转到对应用例的链接地址")
    @allure.title(
        "测试数据：【 {year},{areaId},{areaName},{isSelf},{hadExit},{except_result},{except_code},{except_msg}】")
    @pytest.mark.single
    @pytest.mark.parametrize("year, areaId, areaName, isSelf, hadExit, except_result, except_code, except_msg",
                             api_data["test_investProgress_year_city"])
    @pytest.mark.parametrize("sql", api_data_sql["test_overview_fundOverviewChildEvolute_investProgress_sql"])
    # isself:0市，1市本级，hadExit: 1是 0不是
    def test_get_mother(self, year, areaId, areaName, isSelf, hadExit, except_result, except_code, except_msg, sql):
        logger.info("*************** 开始执行用例 ***************")
        result = get_fundOverviewChildEvolute_investProgress(year, areaId, areaName, isSelf, hadExit)
        step_1(year)
        if result.code == 401:
            logger.info("***************token失效 结束执行用例 ***************")
        else:
            # isSelf:1本级0市
            for i in range(0, len(sql)):
                if year == sql[i][0] and hadExit == 1:
                    sql_data = sql[i][1]
                    break
                elif year == sql[i][0] and hadExit == 0:
                    sql_data = sql[i][2]
                    break
            """
                省市区县分布 金额添加断言
                sumMoneyTwo:去年末
                sumMoney:新增      
            """
            # print(result)
            logger.debug(sql_data)
            data_list = db.select_db(sql_data)
            result_data = result.response.json()['data']
            for status_i in range(len(data_list)):
                for response_status_i in range(0, len(result_data)):
                    if data_list[status_i]['data_city'] == areaName and \
                            data_list[status_i]['data_county'] == \
                            result_data[response_status_i]['city'] and hadExit == 1 and result_data[response_status_i][
                        'city'] != '市级':
                        assert float(data_list[status_i]["2021年投资额"] - 1) <= float(
                            result_data[response_status_i]['sumMoneyTwo']) <= float(
                            data_list[status_i]["2021年投资额"] + 2), result.error
                        assert float(data_list[status_i]["2022年新增"] - 1) <= float(
                            result_data[response_status_i]['sumMoney']) <= float(
                            data_list[status_i]["2022年新增"] + 2), result.error
                        break
                    elif data_list[status_i]['data_city'] == areaName and \
                            data_list[status_i]['data_county'] == \
                            result_data[response_status_i]['city'] and hadExit == 0 and result_data[response_status_i][
                        'city'] != '市级':
                        assert float(data_list[status_i]["2021年投资额"] - 1) <= float(
                            result_data[response_status_i]['sumMoneyTwo']) <= float(
                            data_list[status_i]["2021年投资额"] + 2), result.error
                        assert float(data_list[status_i]["2022年新增"] - 5) <= float(
                            result_data[response_status_i]['sumMoney']) <= float(
                            data_list[status_i]["2022年新增"] + 2), result_data[response_status_i]['city']
                        break
            assert result.success == except_result, result.error
            assert result.code == except_code, result.error
            assert result.success == except_result, result.error
            logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
            assert result.response.json().get("code") == except_code
            assert except_msg in result.msg
            logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_overview_09_fundOverviewChildEvolute_investProgress.py"])
