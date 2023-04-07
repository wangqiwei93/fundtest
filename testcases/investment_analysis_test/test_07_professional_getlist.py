import pytest
import allure
import re
from operation.investment_analysis_test import post_professional_getlist
from testcases.conftest import api_test_fund_mj_data
from common.logger import logger
from common.test_sql.investment_analysis_sql import FundMj_Sql
from common.mysql_operate import db


@allure.step("步骤1 ==>> 联动投资——主题项目库投资分析")
def step_1(year):
    logger.info("步骤1 ==>> 已投项目：{}页".format(year))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("产业基金投资项目列表")
@allure.feature("产业基金投资项目列表")
class TestGetMother():
    @allure.story("用例--获取产业基金投资项目列表")
    @allure.description("该用例是针对产业基金投资项目列表接口的测试")
    @allure.issue("https://yzw.corptssl.com/resource/fund", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://yzw.corptssl.com/resource/fund", name="点击，跳转到对应用例的链接地址")
    @allure.title("测试数据：【 {tag}，{except_result}，{except_code}，{except_msg}】")
    @pytest.mark.single
    @pytest.mark.parametrize(" tag, page, limit, except_result, except_code, except_msg",
                             api_test_fund_mj_data["professional_getlist"])
    def test_get_mother(self, tag, page, limit, except_result, except_code, except_msg):
        logger.info("*************** 开始执行用例 ***************")
        result = post_professional_getlist(tag, page, limit)
        step_1(tag)
        if result.code == 401:
            logger.info("***************token失效 结束执行用例 ***************")
            assert result.code == 200
        else:
            datalist = FundMj_Sql().professional_getlist_sql(tag)
            reslist = result.response.json()['data']['records']  # 接口返回data数据
            # logger.info(reslist)
            for i in range(len(reslist)):
                for l in range(len(datalist)):
                    if reslist[i]['creditCode'] == datalist[l]['credit_code'] and reslist[i]['id'] == datalist[l]['id']:
                        assert reslist[i]['compName'] == datalist[l]['comp_name'], reslist[i]['compName']
                        assert reslist[i]['compIndustry'] == datalist[l]['comp_industry'], reslist[i]['compName']
                        assert reslist[i]['creditCode'] == datalist[l]['credit_code'], reslist[i]['compName']
                        assert reslist[i]['fundInvestAmount'] == datalist[l]['fund_invest_amount'], reslist[i]['compName']
                        assert reslist[i]['isFund'] == datalist[l]['is_fund'], reslist[i]['compName']
                        assert reslist[i]['projectCity'] == datalist[l]['project_city'], reslist[i]['compName']
                        assert reslist[i]['projectDistrict'] == datalist[l]['project_district'], reslist[i]['compName']
                        assert reslist[i]['projectProvince'] == datalist[l]['project_province'], reslist[i]['project_province']
                        assert reslist[i]['regCapitalNumber'] == datalist[l]['reg_capital_number'], reslist[i]['compName']
                        assert reslist[i]['specializationBatch'] == datalist[l]['specialization_batch'], reslist[i]['compName']
                        assert reslist[i]['fundProjectId'] == datalist[l]['fund_project_id'], reslist[i]['compName']
                        break

            assert result.success == except_result, result.error
            assert result.code == except_code, result.error
            assert result.success == except_result, result.error
            logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
            assert result.response.json().get("code") == except_code
            assert except_msg in result.msg
            logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-s", "-q", "test_07_professional_getlist.py"])
