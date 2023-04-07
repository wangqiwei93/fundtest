import pytest
import allure
import re
from operation.investment_analysis_test import get_queryDwsFundMjCastProFieldList
from testcases.conftest import api_test_fund_mj_data
from common.logger import logger
from common.test_sql.investment_analysis_sql import FundMj_Sql
from common.mysql_operate import db


@allure.step("步骤1 ==>> 联动投资——主题项目库投资分析")
def step_1(year):
    logger.info("步骤1 ==>> 重大项目领域分布：{}页".format(year))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("重大项目领域分布列表")
@allure.feature("重大项目领域分布列表")
class TestGetMother():
    @allure.story("用例--获取重大项目领域分布列表")
    @allure.description("该用例是针对重大项目领域分布列表接口的测试")
    @allure.issue("https://yzw.corptssl.com/resource/fund", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://yzw.corptssl.com/resource/fund", name="点击，跳转到对应用例的链接地址")
    @allure.title("测试数据：【 {fieldtype}，{fieldname}，{except_result}，{except_code}，{except_msg}】")
    @pytest.mark.single
    @pytest.mark.parametrize("fieldtype, fieldname, except_result, except_code, except_msg",
                             api_test_fund_mj_data["FieldList_test"])
    def test_get_mother(self, fieldtype, fieldname, except_result, except_code, except_msg):
        logger.info("*************** 开始执行用例 ***************")
        result = get_queryDwsFundMjCastProFieldList(fieldtype)
        step_1(fieldname)
        if result.code == 401:
            logger.info("***************token失效 结束执行用例 ***************")
            assert result.code == 200
        else:
            datalist = FundMj_Sql().field_list_sql(fieldtype)
            reslist = result.response.json()['data']  # 接口返回data数据
            for i in range(len(datalist)):
                assert reslist[i]['fieldCount'] == datalist[i]['field_count'], reslist[i]['fieldType']
                assert reslist[i]['fieldType'] == datalist[i]['field_type'], reslist[i]['fieldType']
                assert round(float(reslist[i]['fieldProportion']), 2) == round(
                    float(datalist[i]['field_proportion']) * 100,
                    2), reslist[i]['fieldType']
                logger.info(
                    '返回参数：{},数据库：{}'.format(float(reslist[i]['fieldCount']), float(datalist[i]['field_proportion'])))
            assert result.success == except_result, result.error
            assert result.code == except_code, result.error
            assert result.success == except_result, result.error
            logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
            assert result.response.json().get("code") == except_code
            assert except_msg in result.msg
            logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-s", "-q", "test_01_fund_mj_queryDwsFundMjCastProFieldList.py"])
