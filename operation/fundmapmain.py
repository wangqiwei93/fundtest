import json
import os

import pytest

from core.result_base import ResultBase
from api.fundmapmain import fundmap
from urllib.parse import urlencode
from common.logger import logger
from common.read_data import data

global headerjson
global headerform
BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")

data = data.load_ini(data_file_path)["test_token"]

tokeng = data['TOKEN']

headerjson = {
    "Content-Type": "application/json",
    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 ChannelId(0) LyraVM Nebula  AlipayDefined() AliApp(AP/10.1.80) AlipayClient/10.1.80 Language/en AlipayIDE",
    "accept-charset": "utf-8",
    "accept-encoding": "gzip, deflate",
    "Authorization": tokeng
}

headerform = {
    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 ChannelId(0) LyraVM Nebula  AlipayDefined() AliApp(AP/10.1.80) AlipayClient/10.1.80 Language/en AlipayIDE",
    "accept-charset": "utf-8",
    "accept-encoding": "gzip, deflate",
    "Authorization": tokeng
}

"""
    基金图谱页
"""


# 产业基金详情接口
def get_fundatlas_getmotherfundmap(year):
    """
    获取产业基金分布
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    payload = {
        "year": year
    }
    # print("**********************", year)
    # 产业基金详情接口
    res = fundmap.get_mother_fund_map(data=payload, headers=headerform)
    result.success = True
    try:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['message'])
        result.msg = res.json()['message']
        result.response = res
        result.code = res.json()['code']
        result.data = res.json()['data']
    except Exception as e:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['msg'])
        result.code = res.json()['code']
        result.response = res
        result.msg = res.json()['msg']
    return result


# 省市产业基金规模排名
def get_fundatlas_getScaleRank(year):
    """
        获取产业基金分布
        :return: 自定义的关键字返回结果 result
        """
    result = ResultBase()
    payload = {
        "year": year
    }

    res = fundmap.get_scale_rank(data=payload, headers=headerform)
    result.success = True
    try:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['message'])
        result.msg = res.json()['message']
        result.response = res
        result.code = res.json()['code']
        result.data = res.json()['data']
    except Exception as e:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['msg'])
        result.code = res.json()['code']
        result.response = res
        result.msg = res.json()['msg']
    return result


# 省市产业基金投资进度
def get_fundatlas_getCompleteRate(year):
    """
        获取产业基金分布
        :return: 自定义的关键字返回结果 result
        """
    result = ResultBase()
    payload = {
        "year": year,
    }

    res = fundmap.get_complete_rate(data=payload, headers=headerform)
    result.success = True
    try:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['message'])
        result.msg = res.json()['message']
        result.response = res
        result.code = res.json()['code']
        result.data = res.json()['data']
    except Exception as e:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['msg'])
        result.code = res.json()['code']
        result.response = res
        result.msg = res.json()['msg']
    return result


# 省市产业基金投资进度
def get_fundatlas_getDetail(year, city):
    """
        获取产业基金分布
        :return: 自定义的关键字返回结果 result
        """
    print(city)
    result = ResultBase()
    payload = {
        "city": city,
        "year": year
    }

    res = fundmap.get_detail(data=payload, headers=headerform)
    result.success = True
    # print(res.json())
    try:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['message'])
        result.msg = res.json()['message']
        result.response = res
        result.code = res.json()['code']
        result.data = res.json()['data']
    except Exception as e:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['msg'])
        result.code = res.json()['code']
        result.response = res
        result.msg = res.json()['msg']
    return result


# 省市产业基金投资进度  各市详情
def get_fundatlas_getCompleteRateByCity(year, city):
    """
        获取产业基金分布
        :return: 自定义的关键字返回结果 result
        """
    print(city)
    result = ResultBase()
    payload = {
        "city": city,
        "year": year
    }

    res = fundmap.get_complete_rate_by_city(data=payload, headers=headerform)
    result.success = True
    # print(res.json())
    try:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['message'])
        result.msg = res.json()['message']
        result.response = res
        result.code = res.json()['code']
        result.data = res.json()['data']
    except Exception as e:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['msg'])
        result.code = res.json()['code']
        result.response = res
        result.msg = res.json()['msg']
    return result


# 省市产业基金总规模（基金个数，基金总规模）
def get_fundatlas_getOverview(year):
    """
        获取产业基金分布
        :return: 自定义的关键字返回结果 result
        """
    result = ResultBase()
    payload = {
        "year": year
    }

    res = fundmap.get_overview(data=payload, headers=headerform)
    result.success = True
    # print(res.json())
    try:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['message'])
        result.msg = res.json()['message']
        result.response = res
        result.code = res.json()['code']
        result.data = res.json()['data']
    except Exception as e:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['msg'])
        result.code = res.json()['code']
        result.response = res
        result.msg = res.json()['msg']
    return result


# 全省产业基金投资总进度(以投资和未投资584000区域基金)
def get_fundatlas_getCompleteRateAll(year):
    """
        获取产业基金分布
        :return: 自定义的关键字返回结果 result
        """
    result = ResultBase()
    payload = {
        "year": year
    }

    res = fundmap.get_complete_rate_all(year, headers=headerform)
    result.success = True
    # print(res.json())
    try:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['message'])
        result.msg = res.json()['message']
        result.response = res
        result.code = res.json()['code']
        result.data = res.json()['data']
    except Exception as e:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['msg'])
        result.code = res.json()['code']
        result.response = res
        result.msg = res.json()['msg']
    return result


# 省市财政出资情况
def get_fundatlas_getPaidRank(year):
    """
        获取产业基金分布
        :return: 自定义的关键字返回结果 result
        """
    result = ResultBase()
    payload = {
        "year": year
    }

    res = fundmap.get_paid_rank(data=payload, headers=headerform)
    result.success = True
    # print(res.json())
    try:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['message'])
        result.msg = res.json()['message']
        result.response = res
        result.code = res.json()['code']
        result.data = res.json()['data']
    except Exception as e:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['msg'])
        result.code = res.json()['code']
        result.response = res
        result.msg = res.json()['msg']
    return result


"""
    下设子基金页
"""


# 下设子基金规模情况
def get_fundatlas_getProvinceChildFundInfo(year, isChild):
    """
        获取产业基金分布
        :return: 自定义的关键字返回结果 result
        """
    result = ResultBase()
    payload = {
        "year": year
    }

    res = fundmap.get_province_child_fund_info(data=payload, headers=headerform)
    result.success = True
    # print(res.json())
    try:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['message'])
        result.msg = res.json()['message']
        result.response = res
        result.code = res.json()['code']
        result.data = res.json()['data']
    except Exception as e:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['msg'])
        result.code = res.json()['code']
        result.response = res
        result.msg = res.json()['msg']
    return result


# 下设子基金规模情况  详情
def get_sub_fundatlas_getDetail(year, isChild, city):
    """
        获取产业基金分布
        :return: 自定义的关键字返回结果 result
        """
    print(city)
    result = ResultBase()
    payload = {
        "city": city,
        "isChild": isChild,
        "year": year
    }

    res = fundmap.get_detail(data=payload, headers=headerform)
    result.success = True
    # print(res.json())
    try:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['message'])
        result.msg = res.json()['message']
        result.response = res
        result.code = res.json()['code']
        result.data = res.json()['data']
    except Exception as e:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['msg'])
        result.code = res.json()['code']
        result.response = res
        result.msg = res.json()['msg']
    return result


# 下设子基金财政出资情况
def get_sub_fundatlas_getChildFundGovPaidList(year, isChild):
    """
        获取产业基金分布
        :return: 自定义的关键字返回结果 result
        """
    result = ResultBase()
    payload = {
        "isChild": isChild,
        "year": year
    }

    res = fundmap.get_child_fund_gov_paid_list(data=payload, headers=headerform)
    result.success = True
    # print(res.json())
    try:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['message'])
        result.msg = res.json()['message']
        result.response = res
        result.code = res.json()['code']
        result.data = res.json()['data']
    except Exception as e:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['msg'])
        result.code = res.json()['code']
        result.response = res
        result.msg = res.json()['msg']
    return result


# 下设子基金投资进度
def get_sub_fundatlas_getChildCompleteRate(year, isChild):
    """
        获取产业基金分布
        :return: 自定义的关键字返回结果 result
        """
    result = ResultBase()
    payload = {
        "isChild": isChild,
        "year": year
    }

    res = fundmap.get_child_com_plete_rate(data=payload, headers=headerform)
    result.success = True
    # print(res.json())
    try:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['message'])
        result.msg = res.json()['message']
        result.response = res
        result.code = res.json()['code']
        result.data = res.json()['data']
    except Exception as e:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['msg'])
        result.code = res.json()['code']
        result.response = res
        result.msg = res.json()['msg']
    return result


# 省内项目投资情况
def get_sub_fundatlas_getProvinceFundChildRate(year, isChild):
    """
        获取产业基金分布
        :return: 自定义的关键字返回结果 result
        """
    result = ResultBase()
    payload = {
        "isChild": isChild,
        "year": year
    }

    res = fundmap.get_province_fund_child_rate(data=payload, headers=headerform)
    result.success = True
    # print(res.json())
    try:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['message'])
        result.msg = res.json()['message']
        result.response = res
        result.code = res.json()['code']
        result.data = res.json()['data']
    except Exception as e:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['msg'])
        result.code = res.json()['code']
        result.response = res
        result.msg = res.json()['msg']
    return result


# 下设子基金
def get_sub_fundatlas_getChildOverview(year, isChild):
    """
        获取产业基金分布
        :return: 自定义的关键字返回结果 result
        """
    result = ResultBase()
    payload = {
        "isChild": isChild,
        "year": year
    }

    res = fundmap.get_child_overview(data=payload, headers=headerform)
    result.success = True
    # print(res.json())
    try:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['message'])
        result.msg = res.json()['message']
        result.response = res
        result.code = res.json()['code']
        result.data = res.json()['data']
    except Exception as e:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['msg'])
        result.code = res.json()['code']
        result.response = res
        result.msg = res.json()['msg']
    return result


# 项目投资数
def get_sub_fundatlas_getProjectOverview(year, isChild):
    """
        获取产业基金分布
        :return: 自定义的关键字返回结果 result
        """
    result = ResultBase()
    payload = {
        "isChild": isChild,
        "year": year
    }

    res = fundmap.get_project_overview(data=payload, headers=headerform)
    result.success = True
    # print(res.json())
    try:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['message'])
        result.msg = res.json()['message']
        result.response = res
        result.code = res.json()['code']
        result.data = res.json()['data']
    except Exception as e:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['msg'])
        result.code = res.json()['code']
        result.response = res
        result.msg = res.json()['msg']
    return result


# 下设子基金条数详情
def get_sub_fundatlas_getChildFundMap(year):
    """
        获取产业基金分布
        :return: 自定义的关键字返回结果 result
        """
    result = ResultBase()
    # payload = {
    #     "isChild": isChild,
    #     "year": year
    # }

    res = fundmap.get_child_fund_map(year, headers=headerform)
    result.success = True
    # print(res.json())
    try:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['message'])
        result.msg = res.json()['message']
        result.response = res
        result.code = res.json()['code']
        result.data = res.json()['data']
    except Exception as e:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['msg'])
        result.code = res.json()['code']
        result.response = res
        result.msg = res.json()['msg']
    return result


"""
    基金总览
"""


# 下设子基金条数详情
def get_fundOverviewMotherEvolute_fundState(year, areaId, areaName, isSelf):
    """
        获取产业基金分布
        :return: 自定义的关键字返回结果 result
        """
    result = ResultBase()
    # payload = {
    #     "isChild": isChild,
    #     "year": year
    # }

    res = fundmap.fundOverviewMotherEvolute_fund_State(year, areaId, areaName, isSelf, headers=headerform)
    result.success = True
    try:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['message'])
        result.msg = res.json()['message']
        result.response = res
        result.code = res.json()['code']
        result.data = res.json()['data']
    except Exception as e:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['msg'])
        result.code = res.json()['code']
        result.response = res
        result.msg = res.json()['msg']
    return result


# 母基金  省市县区域分布
def get_fundOverviewMotherEvolute_regionArrange(year, areaId, areaName, fundtype):
    """
        获取产业基金分布
        :return: 自定义的关键字返回结果 result
        """
    result = ResultBase()
    # payload = {
    #     "isChild": isChild,
    #     "year": year
    # }

    res = fundmap.fundOverviewMotherEvolute_region_Arrange(year, areaId, areaName, fundtype, headers=headerform)
    result.success = True
    try:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['message'])
        result.msg = res.json()['message']
        result.response = res
        result.code = res.json()['code']
        result.data = res.json()['data']
    except Exception as e:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['msg'])
        result.code = res.json()['code']
        result.response = res
        result.msg = res.json()['msg']
    return result


# 基金投资状态  母基金
def get_fundOverviewMotherEvolute_investStatus(year, areaId, areaName, isSelf, fundtype):
    """
        获取产业基金分布
        :return: 自定义的关键字返回结果 result
        """
    result = ResultBase()
    # payload = {
    #     "isChild": isChild,
    #     "year": year
    # }

    res = fundmap.fundOverviewMotherEvolute_invest_Status(year, areaId, areaName, isSelf, fundtype, headers=headerform)
    result.success = True
    try:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['message'])
        result.msg = res.json()['message']
        result.response = res
        result.code = res.json()['code']
        result.data = res.json()['data']
    except Exception as e:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['msg'])
        result.code = res.json()['code']
        result.response = res
        result.msg = res.json()['msg']
    return result


# 基金投资状态  子基金
def get_fundOverviewChildEvolute_investStatus(year, areaId, areaName, isSelf, fundtype):
    """
        获取产业基金分布
        :return: 自定义的关键字返回结果 result
        """
    result = ResultBase()
    # payload = {
    #     "isChild": isChild,
    #     "year": year
    # }

    res = fundmap.fundOverviewChildEvolute_invest_Status(year, areaId, areaName, isSelf, fundtype, headers=headerform)
    result.success = True
    try:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['message'])
        result.msg = res.json()['message']
        result.response = res
        result.code = res.json()['code']
        result.data = res.json()['data']
    except Exception as e:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['msg'])
        result.code = res.json()['code']
        result.response = res
        result.msg = res.json()['msg']
    return result


# 各地子基金规模情况  子基金
def get_fundOverviewChildEvolute_scaleState(year, areaId, areaName, isSelf):
    """
        获取产业基金分布
        :return: 自定义的关键字返回结果 result
        """
    result = ResultBase()
    # payload = {
    #     "isChild": isChild,
    #     "year": year
    # }

    res = fundmap.fundOverviewChildEvolute_scale_State(year, areaId, areaName, isSelf, headers=headerform)
    result.success = True
    try:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['message'])
        result.msg = res.json()['message']
        result.response = res
        result.code = res.json()['code']
        result.data = res.json()['data']
    except Exception as e:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['msg'])
        result.code = res.json()['code']
        result.response = res
        result.msg = res.json()['msg']
    return result


# 基金投资进度   母基金
def get_fundOverviewMotherEvolute_investProgress(year, areaId, areaName, isSelf, hadExit):
    """
        获取产业基金分布
        :return: 自定义的关键字返回结果 result
        """
    result = ResultBase()
    # payload = {
    #     "isChild": isChild,
    #     "year": year
    # }

    res = fundmap.fundOverviewMotherEvolute_invest_Progress(year, areaId, areaName, isSelf, hadExit, headers=headerform)
    # print(res.json())
    # result = 1
    result.success = True
    try:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['message'])
        result.msg = res.json()['message']
        result.response = res
        result.code = res.json()['code']
        result.data = res.json()['data']
    except Exception as e:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['msg'])
        result.code = res.json()['code']
        result.response = res
        result.msg = res.json()['msg']
    return result


# 基金投资进度   子基金
def get_fundOverviewChildEvolute_investProgress(year, areaId, areaName, isSelf, hadExit):
    """
        获取产业基金分布
        :return: 自定义的关键字返回结果 result
        """
    result = ResultBase()
    # payload = {
    #     "isChild": isChild,
    #     "year": year
    # }

    res = fundmap.fundOverviewChildEvolute_invest_Progress(year, areaId, areaName, isSelf, hadExit, headers=headerform)
    # print(res.json())
    # result = 1
    result.success = True
    try:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['message'])
        result.msg = res.json()['message']
        result.response = res
        result.code = res.json()['code']
        result.data = res.json()['data']
    except Exception as e:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['msg'])
        result.code = res.json()['code']
        result.response = res
        result.msg = res.json()['msg']
    return result


# 子基金  基金总览
def get_fundOverviewChildEvolute_fundState(year, areaId, areaName, isSelf):
    """
        获取产业基金分布
        :return: 自定义的关键字返回结果 result
        """
    result = ResultBase()
    # payload = {
    #     "isChild": isChild,
    #     "year": year
    # }

    res = fundmap.fundOverviewChildEvolute_fund_State(year, areaId, areaName, isSelf, headers=headerform)
    result.success = True
    try:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['message'])
        result.msg = res.json()['message']
        result.response = res
        result.code = res.json()['code']
        result.data = res.json()['data']
    except Exception as e:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['msg'])
        result.code = res.json()['code']
        result.response = res
        result.msg = res.json()['msg']
    return result


# 子基金   省市县分布
def get_fundOverviewChildEvolute_regionArrange(year, areaId, areaName, fundtype):
    """
        获取产业基金分布
        :return: 自定义的关键字返回结果 result
        """
    result = ResultBase()
    # payload = {
    #     "isChild": isChild,
    #     "year": year
    # }

    res = fundmap.fundOverviewChildEvolute_region_Arrange(year, areaId, areaName, fundtype, headers=headerform)
    result.success = True
    try:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['message'])
        result.msg = res.json()['message']
        result.response = res
        result.code = res.json()['code']
        result.data = res.json()['data']
    except Exception as e:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['msg'])
        result.code = res.json()['code']
        result.response = res
        result.msg = res.json()['msg']
    return result


# 子基金   各地子基金财政出资情况
def get_fundOverviewChildEvolute_fincInvest(year, areaId, areaName, isSelf, fundtype):
    """
        获取产业基金分布
        :return: 自定义的关键字返回结果 result
        """
    result = ResultBase()
    # payload = {
    #     "isChild": isChild,
    #     "year": year
    # }

    res = fundmap.fundOverviewChildEvolute_finc_Invest(year, areaId, areaName, isSelf, fundtype, headers=headerform)
    result.success = True
    # print(res.json())
    try:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['message'])
        result.msg = res.json()['message']
        result.response = res
        result.code = res.json()['code']
        result.data = res.json()['data']
    except Exception as e:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['msg'])
        result.code = res.json()['code']
        result.response = res
        result.msg = res.json()['msg']
    return result


# 子基金   下穿弹窗
def get_fundOverviewChildEvolute_getFundList(year, areaId, areaName, isSelf, fundtype, pageNum, pageSize):
    """
        获取产业基金分布
        :return: 自定义的关键字返回结果 result
        """
    result = ResultBase()
    payload = {
        "isSelf": isSelf,
        "year": year,
        "areaId": areaId,
        "type": fundtype,
        "areaName": areaName,
        "pageNum": pageNum,
        "pageSize": pageSize
    }

    res = fundmap.fundOverviewChildEvolute_getFundList(data=json.dumps(payload), headers=headerjson)
    result.success = True
    try:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['message'])
        result.msg = res.json()['message']
        result.response = res
        result.code = res.json()['code']
        result.data = res.json()['data']
    except Exception as e:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['msg'])
        result.code = res.json()['code']
        result.response = res
        result.msg = res.json()['msg']
    return result


# 母基金下穿  退出回报率   项目接口
def get_projectOverviewEvolute_queryThroughProjectInfoPageExit(status, areaId, areaName, fundtype, isSelf, year, page,
                                                               limit, proType):
    """
        获取产业基金分布
        :return: 自定义的关键字返回结果 result
        """
    result = ResultBase()
    payload = {
        "status": status,
        "areaId": areaId,
        "areaName": areaName,
        "type": fundtype,
        "isSelf": isSelf,
        "year": year,
        "page": page,
        "limit": limit,
        "proType": proType
    }
    res = fundmap.projectOverviewEvolute_queryThroughProjectInfoPageExit(data=json.dumps(payload), headers=headerjson)
    result.success = True
    try:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['message'])
        result.msg = res.json()['message']
        result.response = res
        result.code = res.json()['code']
        result.data = res.json()['data']
    except Exception as e:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['msg'])
        result.code = res.json()['code']
        result.response = res
        result.msg = res.json()['msg']
    return result


# 母基金下穿  退出回报率   项目接口
def get_projectOverviewEvolute_queryThroughProjectInfoPage(areaId, areaName, fundtype, isSelf, year, page,
                                                               limit, proType):
    """
        获取产业基金分布
        :return: 自定义的关键字返回结果 result
        """
    result = ResultBase()
    payload = {
        "areaId": areaId,
        "areaName": areaName,
        "type": fundtype,
        "isSelf": isSelf,
        "year": year,
        "page": page,
        "limit": limit,
        "proType": proType
    }
    res = fundmap.projectOverviewEvolute_queryThroughProjectInfoPage(data=json.dumps(payload), headers=headerjson)
    result.success = True
    try:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['message'])
        result.msg = res.json()['message']
        result.response = res
        result.code = res.json()['code']
        result.data = res.json()['data']
    except Exception as e:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['msg'])
        result.code = res.json()['code']
        result.response = res
        result.msg = res.json()['msg']
    return result