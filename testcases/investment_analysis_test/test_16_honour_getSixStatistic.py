import pytest
import allure
import re
from operation.investment_analysis_test import *
from testcases.conftest import api_test_fund_mj_data
from common.logger import logger
from common.test_sql.investment_analysis_sql import FundMj_Sql
from common.mysql_operate import db


@allure.step("步骤1 ==>> 联动投资——主题项目库投资分析")
def step_1(year):
    logger.info("步骤1 ==>> 光荣榜：{}页".format(year))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("光荣榜")
@allure.feature("光荣榜")
class TestGetMother():
    @allure.story("用例--获取光荣榜统计数据")
    @allure.description("该用例是针对光荣榜统计数据接口的测试")
    @allure.issue("https://yzw.corptssl.com/resource/fund", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://yzw.corptssl.com/resource/fund", name="点击，跳转到对应用例的链接地址")
    @allure.title("测试数据：【 {name}，{except_result}，{except_code}，{except_msg}】")
    @pytest.mark.single
    @pytest.mark.parametrize(" name, except_result, except_code, except_msg",
                             api_test_fund_mj_data["honour_getSixStatistic"])
    def test_get_mother(self, name, except_result, except_code, except_msg):
        logger.info("*************** 开始执行用例 ***************")
        result = post_honour_getSixStatistic()
        step_1(name)
        if result.code == 401:
            logger.info("***************token失效 结束执行用例 ***************")
            assert result.code == 200
        else:
            datalist = FundMj_Sql().honour_getSixStatistic_sql()[0]
            reslist = result.response.json()['data']  # 接口返回data数据
            assert float(reslist['digitalCount']) == float(datalist['digital_count'])
            assert float(reslist['digitalFundCount']) == float(datalist['digital_fund_count'])
            assert float(reslist['makeCount']) == float(datalist['make_count'])
            assert float(reslist['makeFundCount']) == float(datalist['make_fund_count'])

            assert result.success == except_result, result.error
            assert result.code == except_code, result.error
            assert result.success == except_result, result.error
            logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
            assert result.response.json().get("code") == except_code
            assert except_msg in result.msg
            logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-s", "-q", "test_16_honour_getSixStatistic.py"])
