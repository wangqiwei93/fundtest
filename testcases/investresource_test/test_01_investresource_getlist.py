import pytest
import allure
import re
from operation.investresource_list import *
from testcases.conftest import api_test_investreource_data
from common.logger import logger
from common.mysql_operate import db


@allure.step("步骤1 ==>> 库连群")
def step_1(year):
    logger.info("步骤1 ==>> 机构库列表：{}页".format(year))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("机构库列表")
@allure.feature("机构库列表")
class TestGetMother():
    @allure.story("用例--获取机构库列表")
    @allure.description("该用例是针对机构库列表接口的测试")
    @allure.issue("https://yzw.corptssl.com/resource/fund", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://yzw.corptssl.com/resource/fund", name="点击，跳转到对应用例的链接地址")
    @allure.title("测试数据：【 {officeType}，{limit}，{page}，{except_result}，{except_code}，{except_msg}】")
    @pytest.mark.single
    @pytest.mark.parametrize("officeType,limit,page, except_result, except_code, except_msg",
                             api_test_investreource_data["investresource_page_limit"])
    def test_get_mother(self, officeType, limit, page, except_result, except_code, except_msg):
        logger.info("*************** 开始执行用例 ***************")
        result = get_investresource_getlist(officeType, limit, page)
        step_1(page)
        if result.code == 401:
            logger.info("***************token失效 结束执行用例 ***************")
            assert result.code == 200
        else:
            assert result.success == except_result, result.error
            assert result.code == except_code, result.error
            assert result.success == except_result, result.error
            logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
            assert result.response.json().get("code") == except_code
            assert except_msg in result.msg
            logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-s", "-q", "test_01_investresource_getlist.py"])
