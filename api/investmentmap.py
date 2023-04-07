import os

from common.logger import logger
from core.rest_client import RestClient
from common.read_data import data

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
# 正式
# api_root_url = data.load_ini(data_file_path)["host"]["api_root_url"]
# 测试
api_root_url = data.load_ini(data_file_path)["test_host"]["api_root_url"]


class InvestmentMap(RestClient):

    def __init__(self, api_root_url, **kwargs):
        super(InvestmentMap, self).__init__(api_root_url, **kwargs)

    """
        基金图谱
    """

    # 根据年份获取全省和地市投资总情况 regionType:0全国,1全省
    def get_map_province(self, year, regionType, **kwargs):
        return self.get("/stage-api/invest/project/map/province/{year}/{regionType}", **kwargs)


investmentmap = InvestmentMap(api_root_url)
