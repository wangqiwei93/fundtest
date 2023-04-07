import pytest
import allure
import re
from operation.fundmapmain import get_fundOverviewChildEvolute_scaleState
from testcases.conftest import api_data, api_data_sql
from common.logger import logger
from common.mysql_operate import db


@allure.step("步骤1 ==>> 子基金-各地子基金规模情况")
def step_1(year):
    logger.info("步骤1 ==>> 子基金-各地子基金规模情况：{}".format(year))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("基金总览")
@allure.feature("子基金-各地子基金规模情况")
class TestGetMother():
    @allure.story('用例--子基金-各地子基金规模情况')
    @allure.description("该用例是针对子基金-各地子基金规模情况的测试")
    @allure.issue("https://yzw.corptssl.com/fundOverview/fundOverviewData", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://yzw.corptssl.com/fundOverview/fundOverviewData", name="点击，跳转到对应用例的链接地址")
    @allure.title("测试数据：【 {year},{areaId},{areaName},{isSelf},{except_result},{except_code},{except_msg},{sql}】")
    @pytest.mark.single
    @pytest.mark.parametrize("year, areaId, areaName, isSelf, except_result, except_code, except_msg",
                             api_data["test_overview_scaleState_year_city"])
    @pytest.mark.parametrize("sql", api_data_sql["test_fundOverviewChildEvolute_scaleState_sql"])
    # isself:0市，1市本级，type：1累计，2增量
    def test_get_mother(self, year, areaId, areaName, isSelf, except_result, except_code, except_msg, sql):
        logger.info("*************** 开始执行用例 ***************")
        result = get_fundOverviewChildEvolute_scaleState(year, areaId, areaName, isSelf)
        step_1(year)
        if result.code == 401:
            logger.info("***************token失效 结束执行用例 ***************")
        else:
            # isSelf:1本级0市
            for i in range(0, len(sql)):
                if year == sql[i][0]:
                    sql_data = sql[i][1]
                    break
            """
                省市区县分布 金额添加断言
                totalSum:累计或增量       
            """
            data_list = db.select_db(sql_data)
            result_data = result.response.json()['data']
            for data_i in range(len(data_list)):
                if data_list[data_i]['data_city'] == areaName:
                    for response_status_i in range(0, len(result_data)):
                        # print(data_list[data_i]['data_county'])
                        # print(result_data[response_status_i])
                        if data_list[data_i]['data_county'] == result_data[response_status_i]['city']:
                            assert float(data_list[data_i]['去年年末累计投资规模'] - 1) <= float(
                                result_data[response_status_i]['totalSub']) <= float(
                                data_list[data_i]['去年年末累计投资规模'] + 2), result.error
                            assert float(data_list[data_i]['去年新增规模'] - 1) <= float(
                                result_data[response_status_i]['totalSum']) <= float(
                                data_list[data_i]['去年新增规模'] + 2), result.error

            assert result.success == except_result, result.error
            assert result.code == except_code, result.error
            assert result.success == except_result, result.error
            logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
            assert result.response.json().get("code") == except_code
            assert except_msg in result.msg
            logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_overview_08_fundOverviewChildEvolute_scaleState.py"])
