import pytest
import allure
import re
from operation.investment_analysis_test import get_group_count
from testcases.conftest import api_test_fund_mj_data
from common.logger import logger
from common.test_sql.investment_analysis_sql import FundMj_Sql
from common.mysql_operate import db


@allure.step("步骤1 ==>> 联动投资——主题项目库投资分析")
def step_1(year):
    logger.info("步骤1 ==>> 融资列表：{}页".format(year))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("融资列表")
@allure.feature("融资列表")
class TestGetMother():
    @allure.story("用例--获取融资列表")
    @allure.description("该用例是针对融资列表接口的测试")
    @allure.issue("https://yzw.corptssl.com/resource/fund", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://yzw.corptssl.com/resource/fund", name="点击，跳转到对应用例的链接地址")
    @allure.title("测试数据：【 {groupname}，{except_result}，{except_code}，{except_msg}】")
    @pytest.mark.single
    @pytest.mark.parametrize("grouptype, groupname, except_result, except_code, except_msg",
                             api_test_fund_mj_data["group_count_test"])
    def test_get_mother(self, grouptype, groupname, except_result, except_code, except_msg):
        logger.info("*************** 开始执行用例 ***************")
        result = get_group_count(grouptype)
        step_1(groupname)
        if result.code == 401:
            logger.info("***************token失效 结束执行用例 ***************")
            assert result.code == 200
        else:
            if grouptype == -1:
                datalist = FundMj_Sql().group_count_sql(grouptype)
                reslist = result.response.json()['data']  # 接口返回data数据
                assert reslist[0]['totalCount'] == datalist[0]['countpro']
                assert round(reslist[0]['totalSum'], 1) == datalist[0]['total_scala_two']
            elif grouptype == 1:
                datalist = FundMj_Sql().group_count_sql(grouptype)
                reslist = result.response.json()['data']  # 接口返回data数据
                for i in range(len(reslist)):
                    assert reslist[i]['totalCount'] == datalist[i]['countpro']
                    assert reslist[i]['statName'] == datalist[i]['project_source']
                    assert round(reslist[i]['totalSum'], 1) == datalist[i]['total_scala_two']
            elif grouptype == 2 or grouptype == 0:
                datalist = FundMj_Sql().group_count_sql(grouptype)
                reslist = result.response.json()['data']  # 接口返回data数据
                for i in range(len(reslist)):
                    for l in range(len(datalist)):
                        if reslist[i]['statName'] == datalist[l]['creator_id']:
                            assert reslist[i]['totalCount'] == datalist[l]['countpro'], reslist[i]['statName']
                            assert reslist[i]['statName'] == datalist[l]['creator_id'], reslist[i]['statName']
                            assert round(reslist[i]['totalSum'], 1) == datalist[l]['total_scala_two'], reslist[i][
                                'statName']
                            break
            assert result.success == except_result, result.error
            assert result.code == except_code, result.error
            assert result.success == except_result, result.error
            logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
            assert result.response.json().get("code") == except_code
            assert except_msg in result.msg
            logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-s", "-q", "test_02_fund_mj_groupcount.py"])
