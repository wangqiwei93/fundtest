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


class FundLib(RestClient):

    def __init__(self, api_root_url, **kwargs):
        super(FundLib, self).__init__(api_root_url, **kwargs)

    """
        基金图谱
    """

    # 产业基金详情接口
    def get_fundlib_getlist(self, **kwargs):
        return self.post("/stage-api/fundLib/getList", **kwargs)


fundlib = FundLib(api_root_url)
