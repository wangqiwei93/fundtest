import pytest
import allure
import re
from operation.fundmapmain import get_sub_fundatlas_getChildFundGovPaidList
from testcases.conftest import api_data, api_data_sql
from common.logger import logger
from common.mysql_operate import db


@allure.step("步骤1 ==>> 下设子基金财政出资情况")
def step_1(year):
    logger.info("步骤1 ==>> 下设子基金财政出资情况：{}".format(year))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("下设子基金页面")
@allure.feature("下设子基金财政出资情况")
class TestGetMother():
    @allure.story('用例--下设子基金财政出资情况')
    @allure.description("该用例是针对下设子基金财政出资情况的测试")
    @allure.issue("https://yzw.corptssl.com/fund/PCFundMap", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://yzw.corptssl.com/fund/PCFundMap", name="点击，跳转到对应用例的链接地址")
    @allure.title("测试数据：【 {year},{isChild},{except_result},{except_code},{except_msg},{sql}】")
    @pytest.mark.single
    @pytest.mark.parametrize("year, isChild, except_result, except_code, except_msg",
                             api_data["test_sub_fund_year"])
    @pytest.mark.parametrize("sql", api_data_sql["test_sub_getChildFundGovPaidList_sql"])
    def test_get_mother(self, year, isChild, except_result, except_code, except_msg, sql):
        logger.info("*************** 开始执行用例 ***************")
        result = get_sub_fundatlas_getChildFundGovPaidList(year, isChild)
        step_1(year)
        if result.code == 401:
            logger.info("***************token失效 结束执行用例 ***************")
        else:
            for i in range(0, len(sql)):
                if year == sql[i][0]:
                    sql_data = sql[i][1]
                    break
            """
                sumMoney:全省财政总认缴
                sumMoneyTwo:全省财政总实缴    
                fundCount:占比       
            """
            for data_city in range(0, len(db.select_db(sql_data))):
                for response_city in range(0, len(result.response.json()['data'])):
                    if db.select_db(sql_data)[data_city] == result.response.json()['data'][response_city]['city']:
                        assert (float(db.select_db(sql_data)[data_city]['占比']) - 1) <= float(
                            result.response.json()['data'][response_city]["rate"]) < (
                                       float(db.select_db(sql_data)[data_city]['占比']) + 1), result.error
                        assert (float(db.select_db(sql_data)[data_city]['财政认缴额']) - 1) <= float(
                            result.response.json()['data'][response_city]["sumMoney"]) < (
                                       float(db.select_db(sql_data)[data_city]['财政认缴额']) + 5), result.error
                        assert (float(db.select_db(sql_data)[data_city]['财政实缴额']) - 1) <= float(
                            result.response.json()['data'][response_city]["sumMoneyTwo"]) < (
                                       float(db.select_db(sql_data)[data_city]['财政实缴额']) + 5), result.error
            assert result.success == except_result, result.error
            assert result.code == except_code, result.error
            assert result.success == except_result, result.error
            logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
            assert result.response.json().get("code") == except_code
            assert except_msg in result.msg
            logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_subfund_03_getChildFundGovPaidList.py"])
