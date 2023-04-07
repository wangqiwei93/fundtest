import pytest
import allure
import re
from operation.fundmapmain import get_fundOverviewMotherEvolute_investStatus
from testcases.conftest import api_data, api_data_sql
from common.logger import logger
from common.mysql_operate import db


@allure.step("步骤1 ==>> 母基金-基金投资状态")
def step_1(year):
    logger.info("步骤1 ==>> 母基金-基金投资状态：{}".format(year))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("基金总览")
@allure.feature("母基金-基金投资状态")
class TestGetMother():
    @allure.story('用例--母基金-基金投资状态')
    @allure.description("该用例是针对母基金-基金投资状态的测试")
    @allure.issue("https://yzw.corptssl.com/fundOverview/fundOverviewData", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://yzw.corptssl.com/fundOverview/fundOverviewData", name="点击，跳转到对应用例的链接地址")
    @allure.title("测试数据：【 {year},{areaId},{areaName},{isSelf},{fundtype},{except_result},{except_code},{except_msg},{sql}】")
    @pytest.mark.single
    @pytest.mark.parametrize("year, areaId, areaName, isSelf, fundtype, except_result, except_code, except_msg",
                             api_data["test_investStatus_year_city"])
    @pytest.mark.parametrize("sql", api_data_sql["test_overview_investStatus_fundtype_0_sql"])
    # isself:0市，1市本级，type：1累计，2增量
    def test_get_mother(self, year, areaId, areaName, isSelf, fundtype, except_result, except_code, except_msg, sql):
        logger.info("*************** 开始执行用例 ***************")
        result = get_fundOverviewMotherEvolute_investStatus(year, areaId, areaName,isSelf, fundtype)
        step_1(year)
        if result.code == 401:
            logger.info("***************token失效 结束执行用例 ***************")
        else:
            # isSelf:1本级0市
            for i in range(0, len(sql)):
                if year == sql[i][0] and fundtype == 1 and isSelf == 0:
                    sql_data = sql[i][1]
                    break
                elif year == sql[i][0] and fundtype == 1 and isSelf == 1:
                    sql_data = sql[i][2]
                    break
                elif year == sql[i][0] and fundtype == 2 and isSelf == 0:
                    sql_data = sql[i][3]
                    break
                elif year == sql[i][0] and fundtype == 2 and isSelf == 1:
                    sql_data = sql[i][4]
                    break
            """
                省市区县分布 金额添加断言
                totalSum:累计或增量       
            """
            logger.debug(sql_data)
            sql_data_list = db.select_db(sql_data)
            result_data = result.response.json()['data']
            for status_i in range(len(sql_data_list)):
                for response_status_i in range(0, len(result_data)):
                    if sql_data_list[status_i]['data_city'] == areaName and \
                            sql_data_list[status_i]['status'] == \
                            result_data[response_status_i]['city'] and fundtype == 1:
                        assert sql_data_list[status_i]["累计"] == result_data[response_status_i]['totalCount'], sql_data_list[status_i]
                        break
                    elif sql_data_list[status_i]['data_city'] == areaName and \
                            sql_data_list[status_i]['status'] == \
                            result_data[response_status_i]['city'] and fundtype == 2:
                        assert sql_data_list[status_i]["增量"] == result_data[response_status_i]['totalCount'], result.error
                        break
            assert result.success == except_result, result.error
            assert result.code == except_code, result.error
            assert result.success == except_result, result.error
            logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
            assert result.response.json().get("code") == except_code
            assert except_msg in result.msg
            logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_overview_03_fundOverviewMotherEvolute_investStatus.py"])
