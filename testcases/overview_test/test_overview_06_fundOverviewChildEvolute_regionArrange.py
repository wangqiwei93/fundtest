import pytest
import allure
import re
from operation.fundmapmain import get_fundOverviewChildEvolute_regionArrange
from testcases.conftest import api_data, api_data_sql
from common.logger import logger
from common.mysql_operate import db


@allure.step("步骤1 ==>> 子基金-省市县分布")
def step_1(year, areaId, areaName, type):
    logger.info("步骤1 ==>> 子基金-省市县分布：{}".format(year, areaId, areaName, type))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("基金总览")
@allure.feature("子基金-省市县分布")
class TestGetMother():
    @allure.story('用例--子基金-省市县分布')
    @allure.description("该用例是针对子基金-省市县分布的测试")
    @allure.issue("https://yzw.corptssl.com/fundOverview/fundOverviewData", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://yzw.corptssl.com/fundOverview/fundOverviewData", name="点击，跳转到对应用例的链接地址")
    @allure.title("测试数据：【 {year},{areaId},{areaName},{fundtype},{except_result},{except_code},{except_msg},{sql}】")
    @pytest.mark.single
    @pytest.mark.parametrize("year, areaId, areaName, fundtype, except_result, except_code, except_msg",
                             api_data["test_regionArrange_year_city"])
    @pytest.mark.parametrize("sql", api_data_sql["test_overview_regionArrange_fundtype_1_sql"])
    def test_get_mother(self, year, areaId, areaName, fundtype, except_result, except_code, except_msg, sql):
        logger.info("*************** 开始执行用例 ***************")
        result = get_fundOverviewChildEvolute_regionArrange(year, areaId, areaName, fundtype)
        step_1(year, areaId, areaName, fundtype)
        if result.code == 401:
            logger.info("***************token失效 结束执行用例 ***************")
        else:
            # isSelf:1本级0市
            for i in range(0, len(sql)):
                if year == sql[i][0] and fundtype == 1:
                    sql_data = sql[i][1]
                    break
                elif year == sql[i][0] and fundtype == 2:
                    sql_data = sql[i][2]
                    break
            """
                省市区县分布 金额添加断言
                totalSum:累计或增量       
            """
            data_list = db.select_db(sql_data)
            result_data = result.response.json()['data']
            # print(data_list)
            # print(result.response.json())
            for data_city_i in range(len(data_list)):
                for response_city_i in range(0, len(result_data)):
                    if data_list[data_city_i]['data_city'] == areaName and data_list[data_city_i]['data_county'] == \
                            result_data[response_city_i]['city'] and fundtype == 1:
                        assert float(data_list[data_city_i]["累计"] - 1) <= float(
                            result_data[response_city_i]['totalSum']) <= float(
                            data_list[data_city_i]["累计"] + 2), data_list[data_city_i]['data_county']
                        break
                    elif data_list[data_city_i]['data_city'] == areaName and data_list[data_city_i]['data_county'] == \
                            result_data[response_city_i]['city'] and fundtype == 2:
                        assert float(data_list[data_city_i]["增量"] - 1) <= float(
                            result_data[response_city_i]['totalSum']) <= float(
                            data_list[data_city_i]["增量"] + 2), data_list[data_city_i]['data_county']
                        break
            assert result.success == except_result, result.error
            assert result.code == except_code, result.error
            assert result.success == except_result, result.error
            logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
            assert result.response.json().get("code") == except_code
            assert except_msg in result.msg
            logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_overview_06_fundOverviewChildEvolute_regionArrange.py.py"])
