import pytest
import allure
import re
from operation.fundmapmain import get_fundatlas_getCompleteRateByCity
from testcases.conftest import api_data, api_data_sql
from common.logger import logger
from common.mysql_operate import db


@allure.step("步骤1 ==>> 省市产业基金规模排名")
def step_1(year):
    logger.info("步骤1 ==>> 省市产业基金规模排名：{}".format(year))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("基金图谱页面")
@allure.feature("省市产业基金规模地方总览详情")
class TestGetMother():
    @allure.story("用例--省市产业基金规模地方总览详情")
    @allure.description("该用例是针对省市产业基金规模地方总览详情的测试")
    @allure.issue("https://yzw.corptssl.com/fund/fundMapMain", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://yzw.corptssl.com/fund/fundMapMain", name="点击，跳转到对应用例的链接地址")
    @allure.title("测试数据：【 {year},{city},{except_result},{except_code},{except_msg}】")
    @pytest.mark.single
    @pytest.mark.parametrize("year, city, except_result, except_code, except_msg", api_data["test_year_city"])
    @pytest.mark.parametrize("sql", api_data_sql["test_getcompleteratebycity_sql"])
    def test_get_mother(self, year, city, except_result, except_code, except_msg, sql):
        logger.info("*************** 开始执行用例 ***************")
        result = get_fundatlas_getCompleteRateByCity(year, city)
        step_1(year)
        print(result.response.json())
        if result.code == 401:
            logger.info("***************token失效 结束执行用例 ***************")
        else:
            for i in range(0, len(sql)):
                if year == sql[i][0]:
                    sql_data = sql[i][1]
                    break
            for i in range(0, len(db.select_db(sql_data))):
                if city == db.select_db(sql_data)[i]['data_city']:
                    """
                    fundCount:产业基金,
                    sumMoney:基金总规模,
                    fundCountThree:下设子基金,
                    fundCountTwo:直投项目,
                    sumMoneyFour:下设子基金投资额,
                    sumMoneyTwo:直投项目投资额,
                    rate ： 投资进度
                    """
                    fundCount = result.response.json()['data']['fundCount']
                    sumMoney = re.findall('\d+\.\d+', result.response.json()['data']['sumMoney'])
                    fundCountThree = result.response.json()['data']['fundCountThree']
                    fundCountTwo = result.response.json()['data']['fundCountTwo']
                    sumMoneyTwo = re.findall('\d+\.\d+', result.response.json()['data']['sumMoneyTwo'])
                    sumMoneyFour = re.findall('\d+\.\d+', result.response.json()['data']['sumMoneyFour'])
                    rate = re.findall('\d+\.\d+', result.response.json()['data']['rate'])
                    # print(fundCount, sumMoney, fundCountThree, fundCountTwo, sumMoneyTwo, sumMoneyFour, rate)
                    # print(type(fundCount), type(float(sumMoney[0])), type(int(fundCountThree)), type(fundCountTwo), type(sumMoneyTwo),
                    #       type(sumMoneyFour), type(rate))
                    assert int(db.select_db(sql_data)[i]['产业基金']) == int(fundCount), result.error
                    assert (float(db.select_db(sql_data)[i]['基金总规模']) - 1) <= float(
                            sumMoney[0]) < (
                                       float(db.select_db(sql_data)[i]['基金总规模']) + 5), result.error
                    assert int(db.select_db(sql_data)[i]['下设子基金']) == int(fundCountThree), result.error
                    assert int(db.select_db(sql_data)[i]['直投项目']) == int(fundCountTwo), result.error
                    assert (float(db.select_db(sql_data)[i]['下设子基金投资额']) - 1) <= float(
                        sumMoneyFour[0]) < (
                                   float(db.select_db(sql_data)[i]['下设子基金投资额']) + 5), result.error
                    assert (float(db.select_db(sql_data)[i]['直投项目投资额']) - 1) <= float(
                        sumMoneyTwo[0]) < (
                                   float(db.select_db(sql_data)[i]['直投项目投资额']) + 5), result.error
                    assert (float(db.select_db(sql_data)[i]['投资进度']) - 1) <= float(
                        rate[0]) < (
                                   float(db.select_db(sql_data)[i]['投资进度']) + 1), result.error
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
    pytest.main(["-v", "-q", "test_09_getcompleteratebycitydetail.py"])
