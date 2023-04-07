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


class InvestResource(RestClient):

    def __init__(self, api_root_url, **kwargs):
        super(InvestResource, self).__init__(api_root_url, **kwargs)

    """
        机构库
    """

    # 机构库所有机构列表
    def get_investresource_getlist(self, officeType, limit, page, **kwargs):
        return self.get(
            f"/stage-api/investResource/getList?officeType={officeType}&officeName=&page={page}&limit={limit}",
            **kwargs)


api_investresource_list = InvestResource(api_root_url)
