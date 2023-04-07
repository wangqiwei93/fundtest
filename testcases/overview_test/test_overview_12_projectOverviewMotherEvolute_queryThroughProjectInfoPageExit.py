import threading
import time

import pytest
import allure
import re
from operation.fundmapmain import get_projectOverviewEvolute_queryThroughProjectInfoPageExit
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
        "测试数据：【 {status},{areaId},{areaName},{fundtype},{isSelf},{except_result},{except_code},{except_msg}】")
    @pytest.mark.single
    @pytest.mark.parametrize(
        "status, areaId, areaName, fundtype, isSelf, year, page, limit, proType, except_result, except_code, except_msg",
        api_data["test_projectinfopageexit_year_city"])
    def test_get_mother(self, status, areaId, areaName, fundtype, isSelf, year, page,
                        limit, proType, except_result, except_code,
                        except_msg):
        logger.info("*************** 开始执行用例 ***************")
        result = get_projectOverviewEvolute_queryThroughProjectInfoPageExit(status, areaId, areaName, fundtype, isSelf,
                                                                            year, page,
                                                                            limit, proType)
        step_1(year)
        assert result.code == except_code, result.error
        assert result.success == except_result, result.error
        print(result.response.json())
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
        assert result.response.json().get("code") == except_code
        assert except_msg in result.msg
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_overview_12_projectOverviewMotherEvolute_queryThroughProjectInfoPageExit.py"])
