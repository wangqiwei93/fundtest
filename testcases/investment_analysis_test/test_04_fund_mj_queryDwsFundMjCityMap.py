import pytest
import allure
import re
from operation.investment_analysis_test import get_fund_mj_queryDwsFundMjCityMap
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
    @allure.title("测试数据：【 {listname}，{except_result}，{except_code}，{except_msg}】")
    @pytest.mark.single
    @pytest.mark.parametrize(" listname, except_result, except_code, except_msg",
                             api_test_fund_mj_data["fund_mj_queryDwsFundMjCityMap"])
    def test_get_mother(self, listname, except_result, except_code, except_msg):
        logger.info("*************** 开始执行用例 ***************")
        result = get_fund_mj_queryDwsFundMjCityMap()
        step_1(listname)
        if result.code == 401:
            logger.info("***************token失效 结束执行用例 ***************")
            assert result.code == 200
        else:
            datalist = FundMj_Sql().fund_mj_queryDwsFundMjCityMap_sql()
            reslist = result.response.json()['data']  # 接口返回data数据
            # logger.info("1222222222222222222211111111", reslist, '222222', len(reslist))

            for m in range(len(reslist)):
                for l in range(len(datalist)):
                    for i in range(len(reslist[datalist[l]['project_city']])):
                        if reslist[datalist[l]['project_city']][i]['proId'] == datalist[l]['pro_id']:
                            assert reslist[datalist[l]['project_city']][i]['creditCode'] == datalist[l]['credit_code']
                            assert reslist[datalist[l]['project_city']][i]['majorProject'] == datalist[l][
                                'major_project']
                            assert reslist[datalist[l]['project_city']][i]['projectCity'] == datalist[l]['project_city']
                            assert reslist[datalist[l]['project_city']][i]['projectDistrict'] == datalist[l][
                                'project_district']
                            assert float(reslist[datalist[l]['project_city']][i]['projectEquityAmount']) <= round(
                                (float(datalist[l]['project_equity_amount']) / 10000) + 1, 1) or float(
                                reslist[datalist[l]['project_city']][i]['projectEquityAmount']) > round(
                                (float(datalist[l]['project_equity_amount']) / 10000) - 1, 1)
                            assert float(reslist[datalist[l]['project_city']][i]['totalScale']) <= round(
                                (float(datalist[l]['total_scale']) / 10000) + 1, 1) or float(
                                reslist[datalist[l]['project_city']][i]['totalScale']) > round(
                                (float(datalist[l]['total_scale']) / 10000) - 1, 1)
                            break

                # logger.info("2222222222222222", len(reslist[m]))
                # for i in range(len(reslist[m])):
                #     logger.info("2222222222222222", reslist[m][i])
                #     for l in range(len(datalist)):
                #         # if reslist[i]['proId'] == datalist[l]['pro_id']:
                #         #     logger.info("-------------", reslist[i]['proId'], datalist[l]['pro_id'])
                #         if reslist[m][i]['proId'] == datalist[l]['pro_id']:
                #             assert reslist[m][i]['creditCode'] == datalist[l]['credit_code']
                #             assert reslist[m][i]['majorProject'] == datalist[l]['major_project']
                #             assert reslist[m][i]['projectCity'] == datalist[l]['project_city']
                #             assert reslist[m][i]['projectDistrict'] == datalist[l]['project_district']
                #             assert float(reslist[m][i]['projectEquityAmount']) == round(
                #                 float(datalist[l]['projectequity_amount']) / 10000, 1)
                #             assert float(reslist[m][i]['totalScale']) == round(
                #                 float(datalist[l]['total_scale']) / 10000, 1)
                #             break

            assert result.success == except_result, result.error
            assert result.code == except_code, result.error
            assert result.success == except_result, result.error
            logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
            assert result.response.json().get("code") == except_code
            assert except_msg in result.msg
            logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-s", "-q", "test_04_fund_mj_queryDwsFundMjCityMap.py"])
