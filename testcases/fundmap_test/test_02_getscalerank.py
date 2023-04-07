import pytest
import allure
from operation.fundmapmain import get_fundatlas_getScaleRank
from testcases.conftest import api_data, api_data_sql
from common.logger import logger
from common.mysql_operate import db
import re


@allure.step("步骤1 ==>> 省市产业基金规模排名")
def step_1(year):
    logger.info("步骤1 ==>> 省市产业基金规模排名：{}".format(year))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("基金图谱页面")
@allure.feature("省市产业基金规模排名")
class TestGetMother():
    @allure.story("用例--省市产业基金规模排名")
    @allure.description("该用例是针对省市产业基金规模排名的测试")
    @allure.issue("https://yzw.corptssl.com/fund/fundMapMain", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://yzw.corptssl.com/fund/fundMapMain", name="点击，跳转到对应用例的链接地址")
    @allure.title("测试数据：【 {year}，{except_result}，{except_code}，{except_msg}，{sql}】")
    @pytest.mark.single
    @pytest.mark.parametrize("year, except_result, except_code, except_msg", api_data["test_year"])
    @pytest.mark.parametrize("sql", api_data_sql["test_getscalerank_sql"])
    def test_get_mother(self, year, except_result, except_code, except_msg, sql):
        logger.info("*************** 开始执行用例 ***************")
        result = get_fundatlas_getScaleRank(year)
        step_1(year)
        if result.code == 401:
            logger.info("***************token失效 结束执行用例 ***************")
        else:
            for i in range(0, len(sql)):
                if year == sql[i][0]:
                    sql_data = sql[i][1]
                    break
            data_sql_list = db.select_db(sql_data)
            for i in range(len(data_sql_list)):
                for result_i in range(0, len(result.response.json()['data'])):
                    if db.select_db(sql_data)[i]['data_city'] == result.response.json()['data'][result_i]['city'] and \
                                            result.response.json()['data'][result_i]['city'] != '省级':
                        """
                        fundCount:产业基金数,
                        childMoney：基金规模
                        sumMoney： 基金总规模
                        city: 地区
                        """
                        fundCount = int(result.response.json()['data'][result_i]['fundCount'])
                        sumMoney = float(result.response.json()['data'][result_i]['sumMoney'])
                        # print(type(sumMoney))
                        # print((data_list[i]))
                        assert int(db.select_db(sql_data)[i]['基金数']) == fundCount, result.error
                        assert float(db.select_db(sql_data)[i]['基金总规模']) >= sumMoney or float(
                            db.select_db(sql_data)[i]['基金总规模'] - 1) <= sumMoney, result.error
                        break
                    else:
                        continue

            assert result.success == except_result, result.error
            assert result.code == except_code, result.error
            assert result.success == except_result, result.error
            logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
            assert result.response.json().get("code") == except_code
            assert except_msg in result.msg
            logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-s", "-q", "test_02_getscalerank.py"])
