import pytest
import allure
import re
from operation.fundmapmain import get_fundatlas_getCompleteRateAll
from testcases.conftest import api_data, api_data_sql
from common.logger import logger
from common.mysql_operate import db


@allure.step("步骤1 ==>> 省市产业基金总规模")
def step_1(year):
    logger.info("步骤1 ==>> 省市产业基金总规模：{}".format(year))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("基金图谱页面")
@allure.feature("全省产业基金投资总进度")
class TestGetMother():
    @allure.story("用例--全省产业基金投资总进度")
    @allure.description("该用例是针对全省产业基金投资总进度的测试")
    @allure.issue("https://yzw.corptssl.com/fund/fundMapMain", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://yzw.corptssl.com/fund/fundMapMain", name="点击，跳转到对应用例的链接地址")
    @allure.title("测试数据：【 {year},{except_result},{except_code},{except_msg}】")
    @pytest.mark.single
    @pytest.mark.parametrize("year, except_result, except_code, except_msg", api_data["test_year"])
    @pytest.mark.parametrize("sql", api_data_sql["test_getcompleterateall_sql"])
    def test_get_mother(self, year, except_result, except_code, except_msg, sql):
        logger.info("*************** 开始执行用例 ***************")
        result = get_fundatlas_getCompleteRateAll(year)
        step_1(year)
        if result.code == 401:
            logger.info("***************token失效 结束执行用例 ***************")
        else:
            for i in range(0, len(sql)):
                if year == sql[i][0]:
                    sql_data = sql[i][1]
                    break
            """
                city:投资状态
                totalSub:投资额            
            """
            resultdata = result.response.json()['data']
            datasql = db.select_db(sql_data)
            for i in range(0,len(resultdata)):
                if resultdata[i]['statName'] == "未投资":
                    assert float(resultdata[i]['totalSub']) == float(datasql[0]['未投资'])
                elif resultdata[i]['statName'] == "直投项目投资额":
                    assert float(datasql[0]['直投项目'])-5 <= float(resultdata[i]['totalSub']) <= float(datasql[0]['直投项目'])+5
                else:
                    assert float(resultdata[i]['totalSub']) == float(datasql[0]['子基金'])
            assert result.success == except_result, result.error
            assert result.code == except_code, result.error
            assert result.success == except_result, result.error
            logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
            assert result.response.json().get("code") == except_code
            assert except_msg in result.msg
            logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_07_getcompleterateall.py"])
