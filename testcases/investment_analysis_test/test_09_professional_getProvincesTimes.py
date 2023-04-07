import pytest
import allure
import re
from operation.investment_analysis_test import *
from testcases.conftest import api_test_fund_mj_data
from common.logger import logger
from common.test_sql.investment_analysis_sql import FundMj_Sql
from common.mysql_operate import db


@allure.step("步骤1 ==>> 联动投资——主题项目库投资分析")
def step_1(year):
    logger.info("步骤1 ==>> 专精特新：{}页".format(year))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("专精特新省域分布")
@allure.feature("专精特新省域分布")
class TestGetMother():
    @allure.story("用例--获取专精特新省域分布")
    @allure.description("该用例是针对专精特新省域分布接口的测试")
    @allure.issue("https://yzw.corptssl.com/resource/fund", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://yzw.corptssl.com/resource/fund", name="点击，跳转到对应用例的链接地址")
    @allure.title("测试数据：【 {tag}，{except_result}，{except_code}，{except_msg}】")
    @pytest.mark.single
    @pytest.mark.parametrize(" city, province, tag, page, limit, except_result, except_code, except_msg",
                             api_test_fund_mj_data["professional_publishTimes"])
    def test_get_mother(self, city, province, tag, page, limit, except_result, except_code, except_msg):
        logger.info("*************** 开始执行用例 ***************")
        result = post_professional_getProvincesTimes(city, province, tag, page, limit)
        step_1(tag)
        if result.code == 401:
            logger.info("***************token失效 结束执行用例 ***************")
            assert result.code == 200
        else:
            datalist = FundMj_Sql().professional_getProvincesTimes_sql()
            reslist = result.response.json()['data']  # 接口返回data数据
            for i in range(len(reslist)):
                for l in range(len(datalist)):
                    if reslist[i]['listName'] == datalist[l]['project_province']:
                        ProvincesTimes = reslist[i]['statInfos']
                        for n in range(len(ProvincesTimes)):
                            if ProvincesTimes[n]['statName'] == datalist[l]['specialization_batch']:
                                assert ProvincesTimes[n]['statName'] == datalist[l]['specialization_batch'], \
                                ProvincesTimes[n]['city']
                                assert ProvincesTimes[n]['totalCount'] == datalist[l]['totalCount'], ProvincesTimes[n][
                                    'city']

            assert result.success == except_result, result.error
            assert result.code == except_code, result.error
            assert result.success == except_result, result.error
            logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
            assert result.response.json().get("code") == except_code
            assert except_msg in result.msg
            logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-s", "-q", "test_09_professional_getProvincesTimes_api.py"])
