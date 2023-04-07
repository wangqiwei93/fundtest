import time

import pytest
import allure
import re
from operation.fundmapmain import get_fundatlas_getmotherfundmap
from testcases.conftest import api_data, api_data_sql
from common.logger import logger
import threading
from common.mysql_operate import db


@allure.step("步骤1 ==>> 产业基金母基金分布")
def step_1(year):
    logger.info("步骤1 ==>> 产业基金母基金分布：{}".format(year))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("基金图谱页面")
@allure.feature("基金图谱产业基金模块")
class TestGetMother():
    @allure.story("用例--获取各市莫母基金分布")
    @allure.description("该用例是针对获取各市母基金分布的测试")
    @allure.issue("https://yzw.corptssl.com/fund/fundMapMain", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://yzw.corptssl.com/fund/fundMapMain", name="点击，跳转到对应用例的链接地址")
    @allure.title("测试数据：【 {year}，{except_result}，{except_code}，{except_msg}】")
    @pytest.mark.single
    @pytest.mark.parametrize("year, except_result, except_code, except_msg", api_data["test_year"])
    @pytest.mark.parametrize("sql", api_data_sql["test_getmotherfundmap_sql"])
    @pytest.mark.parametrize("city", api_data["test_city"])
    def test_get_mother(self, year, except_result, except_code, except_msg, sql, city):
        logger.info("*************** 开始执行用例 ***************")
        starttime = time.time()
        result = get_fundatlas_getmotherfundmap(year)
        end = time.time()
        logger.debug(end-starttime)
        step_1(year)
        global sql_data
        if result.code == 401:
            logger.info("***************token失效 结束执行用例 ***************")
        else:
            for i in range(0, len(sql)):
                if year == sql[i][0]:
                    sql_data = sql[i][1]
                    fund_list_sql = sql[i][2]
                    break

            global l
            l = 0
            # 判断各市基金名称
            for i in range(0, len(city)):
                for k in range(0, len(db.select_db(fund_list_sql))):
                    if city[i] == "db.select_db(fund_list_sql)[k]['data_city']":
                        for l in range(0, len(result.response.json()['data'][city[i]])):
                            assert result.response.json()['data'][city[i]][l]['proName'] in \
                                   db.select_db(fund_list_sql)[k]['fund_name'], result.error
                            k += 1
            assert result.success == except_result, result.error
            assert result.code == except_code, result.error
            assert result.success == except_result, result.error
            logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
            assert result.response.json().get("code") == except_code
            assert except_msg in result.msg
            logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-s", "-q", "test_01_getmotherfundmap.py"])
