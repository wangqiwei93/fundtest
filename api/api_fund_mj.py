import os

from core.rest_client import RestClient
from common.read_data import data

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
# 正式
# api_root_url = data.load_ini(data_file_path)["host"]["api_root_url"]
# 测试
api_root_url = data.load_ini(data_file_path)["test_host"]["api_root_url"]


class FundMj(RestClient):

    def __init__(self, api_root_url, **kwargs):
        super(FundMj, self).__init__(api_root_url, **kwargs)

    """
        重大项目
    """

    # 重大项目-已投项目-领域分布
    def get_queryDwsFundMjCastProFieldList(self, fieldType, **kwargs):  # 重大项目领域分布
        return self.get(
            f"/stage-api/fund/mj/queryDwsFundMjCastProFieldList/{fieldType}",
            **kwargs)

    def get_group_count(self, grouptype, **kwargs):  # 主管部门储备项目情况
        return self.get(
            f"/stage-api/fund/mj/group/{grouptype}",
            **kwargs)

    def get_fund_mj_list_api(self, page, limit, **kwargs):  # 重大项目列表
        return self.get(
            f"/stage-api/fund/mj/list/%E6%B5%99%E6%B1%9F%E7%9C%81/{page}/{limit}",
            **kwargs)

    def get_fund_mj_queryDwsFundMjCityMap_api(self, **kwargs):  # 重大项目 地图个区数据统计
        return self.get(
            f"/stage-api/fund/mj/queryDwsFundMjCityMap/0",
            **kwargs)

    def post_professional_getOverview_api(self, **kwargs):  # 专精特新全国地图头部数据据统计
        return self.post(
            f"/stage-api/professional/getOverview",
            **kwargs)

    def post_professional_getlist_api(self, **kwargs):  # 专精特新全国项目列表
        return self.post(
            f"/stage-api/professional/getList",
            **kwargs)

    def post_professional_publishTimes_api(self, **kwargs):  # 专精特新发布批次企业分布
        return self.post(
            f"/stage-api/professional/publishTimes",
            **kwargs)

    def post_professional_getProvincesTimes_api(self, **kwargs):  # 专精特新省域分布
        return self.post(
            f"/stage-api/professional/getProvincesTimes",
            **kwargs)

    def post_professional_getMapOfCountry_api(self, **kwargs):  # 专精特新发地图点位数据
        return self.post(
            f"/stage-api/professional/getMapOfCountry",
            **kwargs)

    def get_professional_ipoTimes_api(self, **kwargs):  # 专精特新发地图点位数据
        return self.get(
            f"/stage-api/professional/ipoTimes",
            **kwargs)

    def get_professional_getPieChart_api(self, charttype, **kwargs):  # 专精特新领域分布
        return self.get(
            f"/stage-api/professional/getPieChart/{charttype}",
            **kwargs)

    def get_honour_ipoTimes_api(self, **kwargs):  # 光荣榜融资轮次
        return self.get(
            f"/stage-api/honour/ipoTimes",
            **kwargs)

    def get_honour_rank_api(self, ranktype, **kwargs):  # 光荣榜榜单分布
        return self.get(
            f"/stage-api/honour/rank/{ranktype}",
            **kwargs)

    def post_honour_getlist_api(self, **kwargs):  # 光荣榜项目列表
        return self.post(
            f"/stage-api/honour/getList",
            **kwargs)

    def get_honour_getSixStatistic_api(self, **kwargs):  # 光荣榜数据汇总
        return self.get(
            f"/stage-api/honour/getSixStatistic",
            **kwargs)
api_fund_mj_request = FundMj(api_root_url)
