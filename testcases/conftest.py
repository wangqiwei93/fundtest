import pytest
import os
import allure
from common.mysql_operate import db
from common.read_data import data
from common.logger import logger

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def get_data(yaml_file_name):
    try:
        data_file_path = os.path.join(BASE_PATH, "data", yaml_file_name)
        yaml_data = data.load_yaml(data_file_path)
    except Exception as ex:
        pytest.skip(str(ex))
    else:
        return yaml_data


api_data = get_data("api_test_data.yml")
api_data_sql = get_data("api_test_sql.yml")
api_test_fundlib_data = get_data("api_test_fundlib_data.yml")  # 基金库测试用例文件
api_test_projectlib_data = get_data("api_test_projectlib_data.yml")  # 项目库测试用例文件
api_test_investreource_data = get_data("api_test_investresource_data.yml")  # 机构库测试用例文件
api_test_fund_mj_data = get_data("api_test_investment_analysis_data.yml")  # 重大项目测试用例文件