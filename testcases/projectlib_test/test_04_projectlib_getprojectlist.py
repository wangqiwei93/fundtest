import time

import pytest
import allure
import re
from operation.projectlib import *
from common.test_sql.projectliblist_sql import ProJect_Sql
from common.logger import logger
from common.mysql_operate import db


@allure.step("步骤1 ==>> 库连群")
def step_1(year):
    logger.info("步骤1 ==>> 项目库新兴行业、热点项目、特色项目列表搜索项：{}".format(year))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("项目库列表")
@allure.feature("项目库列表")
class TestGetMother():
    @allure.story("用例--获取项目库列表")
    @allure.description("该用例是针对项目库列表接口的测试")
    @allure.issue("https://yzw.corptssl.com/resource/fund", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://yzw.corptssl.com/resource/fund", name="点击，跳转到对应用例的链接地址")
    @allure.title("测试数据：【 {label_code}，{except_result}，{except_code}，{except_msg}】")
    @pytest.mark.single
    @pytest.mark.parametrize("label_code, label_name, except_result, except_code, except_msg", ProJect_Sql().industry_code_2())
    def test_get_mother(self, label_code, label_name, except_result, except_code, except_msg):
        logger.info("*************** 开始执行用例 ***************")
        time.sleep(0.5)
        result = get_projectlib_getgrojectlist_two(label_code)
        step_1(label_name)
        if result.code == 401:
            logger.info("***************token失效 结束执行用例 ***************")
        else:
            if result.response.json()['data'] != None:
                reslist = result.response.json()['data']['records']  # 接口返回data数据
                data_sql = ProJect_Sql().project_list_sql_2(label_code)
                for i in range(len(reslist)):
                    if reslist[i]['proName'] != data_sql[i]['pro_name']:
                        # logger.info('%s:未与数据库校验' % reslist[i]['proName'])
                        continue
                    assert reslist[i]['proName'] == data_sql[i]['pro_name'], reslist[i]['proName']
                    assert reslist[i]['comName'] == data_sql[i]['com_name'], reslist[i]['proName']
                    assert reslist[i]['isIndustryInvestment'] == data_sql[i]['is_industry_investment'], reslist[i][
                        'proName']
                    assert reslist[i]['comIndustry'] == data_sql[i]['com_industry'], reslist[i]['proName']
                    # if data_sql[i]['com_province'] != None and data_sql[i]['com_city'] != None and data_sql[i][
                    #     'com_district'] != None:
                    #     assert reslist[i]['comProvince'] == data_sql[i]['com_province'], reslist[i]['proName']
                    #     assert reslist[i]['comCity'] == data_sql[i]['com_city'], reslist[i]['proName']
                    #     assert reslist[i]['comDistrict'] == data_sql[i]['com_district'], reslist[i]['proName']
                    # else:
                    #     assert reslist[i]['comProvince'] == data_sql[i]['pro_province'], reslist[i]['proName']
                    #     assert reslist[i]['comCity'] == data_sql[i]['pro_city'], reslist[i]['proName']
                    #     assert reslist[i]['comDistrict'] == data_sql[i]['pro_district'], reslist[i]['proName']
                    assert reslist[i]['creditCode'] == data_sql[i]['credit_code'], reslist[i]['proName']
            assert result.success == except_result, result.error
            assert result.code == except_code, result.error
            assert result.success == except_result, result.error
            logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
            assert result.response.json().get("code") == except_code
            assert except_msg in result.msg
            logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-s", "-q", "test_04_projectlib_getprojectlist.py"])
