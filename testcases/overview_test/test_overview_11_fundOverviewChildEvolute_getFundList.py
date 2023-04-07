import threading
import time

import pytest
import allure
import re
from operation.fundmapmain import get_fundOverviewChildEvolute_getFundList
from testcases.conftest import api_data, api_data_sql
from common.logger import logger
from common.mysql_operate import db


@allure.step("步骤1 ==>> 子基金-下穿")
def step_1(year):
    logger.info("步骤1 ==>> 子基金-下穿：{}".format(year))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("基金总览")
@allure.feature("子基金-下穿")
class TestGetMother():
    @allure.story('用例--子基金-下穿')
    @allure.description("该用例是针对子基金-下穿的测试")
    @allure.issue("https://yzw.corptssl.com/fundOverview/fundOverviewData", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://yzw.corptssl.com/fundOverview/fundOverviewData", name="点击，跳转到对应用例的链接地址")
    @allure.title(
        "测试数据：【 {year},{areaId},{areaName},{isSelf},{fundtype},{pageNum},{pageSize},{except_result},{except_code},{except_msg}】")
    @pytest.mark.single
    @pytest.mark.parametrize(
        "year, areaId, areaName, isSelf, fundtype, pageNum, pageSize, except_result, except_code, except_msg",
        api_data["test_getfundlist_fundtype_1_year_city"])
    @pytest.mark.parametrize("sql", api_data_sql["test_overview_fundOverviewChildEvolute_getfundlist_sql"])
    # isself:0市，1市本级，hadExit: 1是 0不是
    def test_get_mother(self, year, areaId, areaName, isSelf, fundtype, pageNum, pageSize, except_result, except_code,
                        except_msg, sql):
        logger.info("*************** 开始执行用例 ***************")
        result = get_fundOverviewChildEvolute_getFundList(year, areaId, areaName, isSelf, fundtype, pageNum, pageSize)
        step_1(year)
        if result.code == 401:
            logger.info("***************token失效 结束执行用例 ***************")
        else:
            # sql_data = ''
            # isSelf:1本级0市,type:1累计2新增，
            for i in range(0, len(sql)):
                if year == sql[i][0] and year != 2020 and fundtype == 1 and isSelf == 0:
                    sql_data = sql[i][1]
                    break
                elif year == sql[i][0] and year != 2020 and fundtype == 2 and isSelf == 0:
                    sql_data = sql[i][2]
                    break
                elif year == sql[i][0] and year != 2020 and fundtype == 1 and isSelf == 1:
                    sql_data = sql[i][3]
                    break
                elif year == sql[i][0] and year != 2020 and fundtype == 2 and isSelf == 1:
                    sql_data = sql[i][4]
                    break

            """
                省市区县分布 金额添加断言
                sumMoneyTwo:去年末
                sumMoney:新增      
            """
            data_list = db.select_db(sql_data)
            response_list = result.response.json()['data']['list']
            for status_i in range(len(data_list)):
                for response_status_i in range(0, len(response_list)):
                    if response_list[response_status_i]['fundId'] == data_list[status_i]['fund_id']:
                        if response_list[response_status_i]['totalInvestAmount'] != '':
                            assert float(data_list[status_i]['已投金额'] - 1) <= float(
                                response_list[response_status_i]['totalInvestAmount']) <= float(
                                data_list[status_i]['已投金额'] + 1), response_list[response_status_i]['fundName']
                            assert float(data_list[status_i]['基金规模'] - 1) <= float(
                                response_list[response_status_i]['fundAmount']) <= float(
                                data_list[status_i]['基金规模'] + 1), response_list[response_status_i]['fundName']
                            assert float(data_list[status_i]['所属基金投资金额'] - 1) <= float(
                                response_list[response_status_i]['investAmountProvince']) <= float(
                                data_list[status_i]['所属基金投资金额'] + 1), response_list[response_status_i]['fundName']
                            assert float(data_list[status_i]['社会资本出资金额'] - 1) <= float(
                                response_list[response_status_i]['investAmountSocial']) <= float(
                                data_list[status_i]['社会资本出资金额'] + 1), response_list[response_status_i]['fundName']
                            assert float(data_list[status_i]['到位资金'] - 1) <= float(
                                response_list[response_status_i]['sumPlaceAmount']) <= float(
                                data_list[status_i]['到位资金'] + 1), response_list[response_status_i]['fundName']
                            if not response_list[response_status_i]['dictNum'] is None:
                                assert response_list[response_status_i]['dictNum'] == data_list[status_i][
                                    '已投项目数'], result.error
                            assert float(data_list[status_i]['投资进度'] - 1) <= float(
                                response_list[response_status_i]['investProgress']) <= float(
                                data_list[status_i]['投资进度'] + 1), response_list[response_status_i]['fundName']
                        elif response_list[response_status_i]['totalInvestAmount'] == '':
                            assert float(data_list[status_i]['基金规模'] - 1) <= float(
                                response_list[response_status_i]['fundAmount']) <= float(
                                data_list[status_i]['基金规模'] + 1), response_list[response_status_i]['fundName']
                            assert float(data_list[status_i]['所属基金投资金额'] - 1) <= float(
                                response_list[response_status_i]['investAmountProvince']) <= float(
                                data_list[status_i]['所属基金投资金额'] + 1), response_list[response_status_i]['fundName']
                            assert float(data_list[status_i]['社会资本出资金额'] - 1) <= float(
                                response_list[response_status_i]['investAmountSocial']) <= float(
                                data_list[status_i]['社会资本出资金额'] + 1), response_list[response_status_i]['fundName']
                            assert float(data_list[status_i]['到位资金'] - 1) <= float(
                                response_list[response_status_i]['sumPlaceAmount']) <= float(
                                data_list[status_i]['到位资金'] + 1), response_list[response_status_i]['fundName']
                            if not response_list[response_status_i]['dictNum'] is None:
                                assert response_list[response_status_i]['dictNum'] == data_list[status_i][
                                    '已投项目数'], result.error
                            assert float(data_list[status_i]['投资进度'] - 1) <= float(
                                response_list[response_status_i]['investProgress']) <= float(
                                data_list[status_i]['投资进度'] + 1), response_list[response_status_i]['fundName']
            assert result.success == except_result, result.error
            assert result.code == except_code, result.error
            assert result.success == except_result, result.error
            logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
            assert result.response.json().get("code") == except_code
            assert except_msg in result.msg
            logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-v", "-p", "test_overview_11_fundOverviewChildEvolute_getFundList.py"])
