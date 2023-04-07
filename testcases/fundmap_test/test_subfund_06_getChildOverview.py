import pytest
import allure
import re
from operation.fundmapmain import get_sub_fundatlas_getChildOverview
from testcases.conftest import api_data, api_data_sql
from common.logger import logger
from common.mysql_operate import db


@allure.step("步骤1 ==>> 下设子基金")
def step_1(year):
    logger.info("步骤1 ==>> 下设子基金：{}".format(year))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("下设子基金页面")
@allure.feature("下设子基金")
class TestGetMother():
    @allure.story("用例--下设子基金")
    @allure.description("该用例是针对下设子基金的测试")
    @allure.issue("https://yzw.corptssl.com/fund/fundMapMain", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://yzw.corptssl.com/fund/fundMapMain", name="点击，跳转到对应用例的链接地址")
    @allure.title("测试数据：【 {year},{isChild},{except_result},{except_code},{except_msg}】")
    @pytest.mark.single
    @pytest.mark.parametrize("year, isChild, except_result, except_code, except_msg", api_data["test_sub_fund_year"])
    @pytest.mark.parametrize("sql", api_data_sql["test_sub_getChildOverview_sql"])
    def test_get_mother(self, year, isChild, except_result, except_code, except_msg, sql):
        logger.info("*************** 开始执行用例 ***************")
        result = get_sub_fundatlas_getChildOverview(year, isChild)
        step_1(year)
        if result.code == 401:
            logger.info("***************token失效 结束执行用例 ***************")
        else:
            for i in range(0, len(sql)):
                if year == sql[i][0]:
                    sql_data = sql[i][1]
                    break
            """
                govPaidSumMoney：全省财政总实缴
                fundSumMoney：基金总规模
                govSumMoney：全省财政总认缴
                fundCount：产业基金
            """
            fundChildCount = result.response.json()['data']['fundChildCount']
            # print(type(result.response.json()["data"]["fundChildSumMoney"]))
            fundChildSumMoney = re.findall("\d+\.\d+", result.response.json()["data"]["fundChildSumMoney"])[0]
            assert db.select_db(sql_data)[0]['下设子基金'] == fundChildCount, result.error
            assert round(float(db.select_db(sql_data)[0]['总规模']),0) == round(float(fundChildSumMoney),0), result.error
            assert result.success == except_result, result.error
            assert result.code == except_code, result.error
            assert result.success == except_result, result.error
            logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
            assert result.response.json().get("code") == except_code
            assert except_msg in result.msg
            logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_subfund_06_getChildOverview.py"])
