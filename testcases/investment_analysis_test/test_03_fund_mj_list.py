import pytest
import allure
import re
from operation.investment_analysis_test import get_fund_mj_list
from testcases.conftest import api_test_fund_mj_data
from common.logger import logger
from common.test_sql.investment_analysis_sql import FundMj_Sql
from common.mysql_operate import db


@allure.step("步骤1 ==>> 联动投资——主题项目库投资分析")
def step_1(year):
    logger.info("步骤1 ==>> 储备项目列表：{}页".format(year))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("储备项目列表")
@allure.feature("储备项目列表")
class TestGetMother():
    @allure.story("用例--获取储备项目列表")
    @allure.description("该用例是针对储备项目列表接口的测试")
    @allure.issue("https://yzw.corptssl.com/resource/fund", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://yzw.corptssl.com/resource/fund", name="点击，跳转到对应用例的链接地址")
    @allure.title("测试数据：【 {listname}，{except_result}，{except_code}，{except_msg}】")
    @pytest.mark.single
    @pytest.mark.parametrize("page, limit, listname, except_result, except_code, except_msg",
                             api_test_fund_mj_data["group_mj_list_test"])
    def test_get_mother(self, page, limit, listname, except_result, except_code, except_msg):
        logger.info("*************** 开始执行用例 ***************")
        result = get_fund_mj_list(page, limit)
        step_1(listname)
        if result.code == 401:
            logger.info("***************token失效 结束执行用例 ***************")
            assert result.code == 200
        else:
            datalist = FundMj_Sql().fund_mj_list()
            reslist = result.response.json()['data']['list']  # 接口返回data数据
            assert len(datalist) == len(reslist)
            for i in range(len(reslist)):
                for l in range(len(datalist)):
                    if reslist[i]['id'] == datalist[l]['id']:
                        assert reslist[i]['majorProject'] == datalist[l]['major_project'], reslist[i]['majorProject']
                        assert reslist[i]['compName'] == datalist[l]['comp_name'], reslist[i]['majorProject']
                        assert reslist[i]['projectSource'] == datalist[l]['project_source'], reslist[i]['majorProject']
                        assert reslist[i]['fieldInvestment'] == datalist[l]['field_investment'], reslist[i]['majorProject']
                        assert round(float(reslist[i]['totalScalaTwo']), 1) == round(float(datalist[l]['total_scala_two']), 1), \
                        reslist[i]['majorProject']
                        break
            assert result.success == except_result, result.error
            assert result.code == except_code, result.error
            assert result.success == except_result, result.error
            logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
            assert result.response.json().get("code") == except_code
            assert except_msg in result.msg
            logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-s", "-q", "test_03_fund_mj_list.py"])
