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


class FundMap(RestClient):

    def __init__(self, api_root_url, **kwargs):
        super(FundMap, self).__init__(api_root_url, **kwargs)

    """
        基金图谱
    """

    # 产业基金详情接口
    def get_mother_fund_map(self, **kwargs):
        return self.post("/stage-api/fundAtlas/getMotherFundMap", **kwargs)

    # 省市产业基金规模排名
    def get_scale_rank(self, **kwargs):
        return self.post("/stage-api/fundAtlas/getScaleRank", **kwargs)

    # 省市产业基金投资进度
    def get_complete_rate(self, **kwargs):
        return self.post("/stage-api/fundAtlas/getCompleteRate", **kwargs)

    # 省市产业基金规模  地方总览详情
    def get_detail(self, **kwargs):
        return self.post("/stage-api/fundAtlas/getDetail", **kwargs)

    # 省市产业基金投资进度
    def get_complete_rate_by_city(self, **kwargs):
        return self.post("/stage-api/fundAtlas/getCompleteRateByCity", **kwargs)

    # 省市产业基金投资进度
    def get_overview(self, **kwargs):
        return self.post("/stage-api/fundAtlas/getOverview", **kwargs)

    # 省市产业基金投资进度
    def get_complete_rate_all(self, year, **kwargs):
        return self.post(f"/stage-api/fundAtlas/getCompleteRateAll/{year}", **kwargs)

    # 省市产业基金投资进度
    def get_paid_rank(self, **kwargs):
        return self.post(f"/stage-api/fundAtlas/getPaidRank", **kwargs)

    """
        下设子基金页面涉及接口
    """

    # 下设子基金规模情况
    def get_province_child_fund_info(self, **kwargs):
        return self.post(f"/stage-api/fundAtlas/getProvinceChildFundInfo", **kwargs)

    # 下设子基金财政出资情况
    def get_child_fund_gov_paid_list(self, **kwargs):
        return self.get(f"/stage-api/fundAtlas/getChildFundGovPaidList", **kwargs)

    # 下设子基金投资进度
    def get_child_com_plete_rate(self, **kwargs):
        return self.post(f"/stage-api/fundAtlas/getChildCompleteRate", **kwargs)

    # 省内项目投资情况
    def get_province_fund_child_rate(self, **kwargs):
        return self.post(f"/stage-api/fundAtlas/getProvinceFundChildRate", **kwargs)

    # 下设子基金
    def get_child_overview(self, **kwargs):
        return self.post(f"/stage-api/fundAtlas/getChildOverview", **kwargs)

    # 项目投资数
    def get_project_overview(self, **kwargs):
        return self.post(f"/stage-api/fundAtlas/getProjectOverview", **kwargs)

    # 下设子基金  条数详情
    def get_child_fund_map(self, year, **kwargs):
        return self.post(f"/stage-api/fundAtlas/getChildFundMap/{year}", **kwargs)

    """
        基金总览
    """

    # 数据总览
    def fundOverviewMotherEvolute_fund_State(self, year, areaId, areaName, isSelf, **kwargs):
        return self.get(f"/stage-api/fundOverviewMotherEvolute/fundState/{areaId}/{areaName}/{year}/{isSelf}", **kwargs)

    # 省市县区域分布   母基金
    def fundOverviewMotherEvolute_region_Arrange(self, year, areaId, areaName, fundtype, **kwargs):
        return self.get(
            f"/stage-api/fundOverviewMotherEvolute/regionArrange/{areaId}/{areaName}/{year}/{fundtype}",
            **kwargs)

    # 省市县区域分布   子基金
    def fundOverviewChildEvolute_region_Arrange(self, year, areaId, areaName, fundtype, **kwargs):
        return self.get(
            f"/stage-api/fundOverviewChildEvolute/regionArrange/{areaId}/{areaName}/{year}/{fundtype}",
            **kwargs)

    # 地子基金财政出资情况   子基金
    def fundOverviewChildEvolute_finc_Invest(self, year, areaId, areaName, isSelf, fundtype, **kwargs):
        return self.get(
            f"/stage-api/fundOverviewChildEvolute/fincInvest/{areaId}/{areaName}/{year}/{isSelf}/{fundtype}",
            **kwargs)

    # 基金投资状态  母基金
    def fundOverviewMotherEvolute_invest_Status(self, year, areaId, areaName, isSelf, fundtype, **kwargs):
        return self.get(f"/stage-api/fundOverviewMotherEvolute/investStatus/{areaId}/{areaName}/{year}/{isSelf}/{fundtype}",
                        **kwargs)

    # 基金投资状态  子基金
    def fundOverviewChildEvolute_invest_Status(self, year, areaId, areaName, isSelf, fundtype, **kwargs):
        return self.get(
            f"/stage-api/fundOverviewChildEvolute/investStatus/{areaId}/{areaName}/{year}/{isSelf}/{fundtype}",
            **kwargs)

    # 基金投资状态  子基金
    def fundOverviewChildEvolute_scale_State(self, year, areaId, areaName, isSelf, **kwargs):
        return self.get(
            f"/stage-api/fundOverviewChildEvolute/scaleState/{areaId}/{areaName}/{year}/{isSelf}",
            **kwargs)

    # 基金投资状态
    def fundOverviewMotherEvolute_invest_Progress(self, year, areaId, areaName, isSelf, hadExit, **kwargs):
        return self.get(
            f"/stage-api/fundOverviewMotherEvolute/investProgress/{areaId}/{areaName}/{year}/{isSelf}/{hadExit}",
            **kwargs)

    # 各地子基金投资进度
    def fundOverviewChildEvolute_invest_Progress(self, year, areaId, areaName, isSelf, hadExit, **kwargs):
        return self.get(
            f"/stage-api/fundOverviewChildEvolute/investProgress/{areaId}/{areaName}/{year}/{isSelf}/{hadExit}",
            **kwargs)

    # 子基金投资详情
    def fundOverviewChildEvolute_fund_State(self, year, areaId, areaName, isSelf, **kwargs):
        return self.get(f"/stage-api/fundOverviewChildEvolute/fundState/{areaId}/{areaName}/{year}/{isSelf}", **kwargs)

    # 下穿弹窗   子基金
    def fundOverviewChildEvolute_getFundList(self, **kwargs):
        return self.post(
            f"/stage-api/fundOverviewChildEvolute/getFundList",
            **kwargs)

    # 母基金  退出回报率   项目下穿
    def projectOverviewEvolute_queryThroughProjectInfoPageExit(self, **kwargs):
        return self.post(
            f"/stage-api/projectOverviewEvolute/queryThroughProjectInfoPageExit",
            **kwargs)

    # 基金总览项目  退出回报率   项目下穿
    def projectOverviewEvolute_queryThroughProjectInfoPage(self, **kwargs):
        return self.post(
            f"/stage-api/projectOverviewEvolute/queryThroughProjectInfoPage",
            **kwargs)
fundmap = FundMap(api_root_url)
