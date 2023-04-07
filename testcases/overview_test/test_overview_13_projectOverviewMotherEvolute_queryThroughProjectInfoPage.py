import pytest
import allure
import re
from operation.fundmapmain import get_projectOverviewEvolute_queryThroughProjectInfoPage
from testcases.conftest import api_data, api_data_sql
from common.logger import logger
from common.test_sql.overviewprojectinfopage_sql import Overview_Sql


@allure.step("步骤1 ==>> 项目：子基金直投项目和直投项目-下穿")
def step_1(year):
    logger.info("步骤1 ==>> 子基金直投项目和直投项目-下穿：{}".format(year))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("基金总览")
@allure.feature("子基金直投项目和直投项目-下穿")
class TestGetMother():
    @allure.story('用例--子基金直投项目和直投项目-下穿')
    @allure.description("该用例是针对子基金直投项目和直投项目-下穿的测试")
    @allure.issue("https://yzw.corptssl.com/fundOverview/fundOverviewData", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://yzw.corptssl.com/fundOverview/fundOverviewData", name="点击，跳转到对应用例的链接地址")
    @allure.title(
        "测试数据：【 {year},{quarter},{areaId},{areaName},{isSelf},{fundtype},{page},{limit},{proType},{except_result},{except_code},{except_msg}】")
    @pytest.mark.single
    @pytest.mark.parametrize(
        "year, quarter, areaId, areaName, isSelf, fundtype, page, limit, proType, except_result, except_code, except_msg",
        api_data["test_projectinfopage_year_city"])
    def test_get_mother(self, year, quarter, areaId, areaName, isSelf, fundtype, page, limit, proType, except_result,
                        except_code, except_msg):
        logger.info("*************** 开始执行用例 ***************")
        result = get_projectOverviewEvolute_queryThroughProjectInfoPage(areaId, areaName, fundtype, isSelf,
                                                                        year, page,
                                                                        limit, proType)
        step_1(year)
        assert result.code == except_code, result.error
        assert result.success == except_result, result.error
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
        assert result.response.json().get("code") == except_code
        assert except_msg in result.msg
        # 判断具体项目
        data_list = Overview_Sql().projectinfopage(year, quarter, areaName, proType)
        response_list = result.response.json()['data']['list']
        for status_i in range(len(data_list)):
            for response_status_i in range(0, len(response_list)):
            # if response_list[response_status_i]['projectId'] == data_list[status_i]['project_id'] and \
            #         response_list[response_status_i]['projectName'] == '上海森亿医疗科技有限公司':
            #     print(data_list[status_i]['project_name'], response_list[response_status_i][
            #         'projectName'])
            #     print(response_list[response_status_i]['projectId'], data_list[status_i]['project_id'])
            #     print(data_list[status_i]['fund_name'] == response_list[response_status_i][
            #         'fundName'])
            #     print(float(data_list[status_i]['项目总规模']), float(response_list[response_status_i][
            #                                                          'sumAmount']))
            #     print(float(data_list[status_i]['基金投资额']), float(response_list[response_status_i][
            #                                                          'fundInvestAmount']))
            #     print(float(data_list[status_i]['社会资本出资']), float(response_list[response_status_i][
            #                                                           'projectEquityAmount']))
                if response_list[response_status_i]['projectId'] == data_list[status_i]['project_id'] and \
                        data_list[status_i]['fund_name'] == response_list[response_status_i][
                    'fundName'] and data_list[status_i]['project_name'] == response_list[response_status_i][
                    'projectName']:
                    assert data_list[status_i]['project_name'] == response_list[response_status_i][
                        'projectName'], result.error
                    assert data_list[status_i]['fund_name'] == response_list[response_status_i][
                        'fundName'], result.error
                    assert data_list[status_i]['所属领域'] == response_list[response_status_i][
                        'chineseIndusType'], result.error
                    if data_list[status_i]['项目总规模'] != None:
                        assert round(float(data_list[status_i]['项目总规模']),0) == round(float(response_list[response_status_i][
                                                                                'sumAmount']),0), \
                        response_list[response_status_i]['projectId']
                    if response_list[response_status_i]['fundInvestAmount'] != None:
                        assert float(data_list[status_i]['基金投资额']) == float(response_list[response_status_i][
                                                                                'fundInvestAmount']), result.error
                    if data_list[status_i]['社会资本出资'] != None:
                        assert float(data_list[status_i]['社会资本出资']) == float(response_list[response_status_i][
                                                                                 'projectEquityAmount']), result.error
                elif response_list[response_status_i]['projectId'] == '' and data_list[status_i]['project_id'] == None and \
                        data_list[status_i]['fund_name'] == response_list[response_status_i][
                    'fundName'] and data_list[status_i]['project_name'] == response_list[response_status_i][
                    'projectName']:
                    assert data_list[status_i]['project_name'] == response_list[response_status_i][
                        'projectName'], result.error
                    assert data_list[status_i]['fund_name'] == response_list[response_status_i][
                        'fundName'], result.error
                    assert data_list[status_i]['所属领域'] == response_list[response_status_i][
                        'chineseIndusType'], result.error
                    if data_list[status_i]['项目总规模'] != None:
                        assert float(data_list[status_i]['项目总规模']) == float(response_list[response_status_i][
                                                                                'sumAmount']), \
                        response_list[response_status_i]['projectId']
                    if response_list[response_status_i]['fundInvestAmount'] != None:
                        assert float(data_list[status_i]['基金投资额']) == float(response_list[response_status_i][
                                                                                'fundInvestAmount']), result.error
                    if data_list[status_i]['社会资本出资'] != None:
                        assert float(data_list[status_i]['社会资本出资']) == float(response_list[response_status_i][
                                                                                 'projectEquityAmount']), result.error

        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-v", "-s",
                 "test_overview_13_projectOverviewMotherEvolute_queryThroughProjectInfoPage.py"])
