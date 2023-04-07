import json
import os

import pytest

from core.result_base import ResultBase
from api.api_fund_mj import api_fund_mj_request
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


# 重大项目投资领域分布
def get_queryDwsFundMjCastProFieldList(fieldType):
    """
        获取产业基金分布
        :return: 自定义的关键字返回结果 result
        """
    result = ResultBase()

    res = api_fund_mj_request.get_queryDwsFundMjCastProFieldList(fieldType, headers=headerform)
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


def get_group_count(grouptype):
    """
        获取产业基金分布
        :return: 自定义的关键字返回结果 result
        """
    result = ResultBase()

    res = api_fund_mj_request.get_group_count(grouptype, headers=headerform)
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


def get_fund_mj_list(page, limit):
    """
        获取产业基金分布
        :return: 自定义的关键字返回结果 result
        """
    result = ResultBase()

    res = api_fund_mj_request.get_fund_mj_list_api(page, limit, headers=headerform)
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


def get_fund_mj_queryDwsFundMjCityMap():
    """
        获取产业基金分布
        :return: 自定义的关键字返回结果 result
        """
    result = ResultBase()

    res = api_fund_mj_request.get_fund_mj_queryDwsFundMjCityMap_api(headers=headerform)
    # print(res.json())
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


def post_professional_getOverview(tag):
    """
        获取产业基金分布
        :return: 自定义的关键字返回结果 result
        """
    result = ResultBase()
    payload = {
        "tag": tag,
        "province": None
    }
    res = api_fund_mj_request.post_professional_getOverview_api(data=json.dumps(payload), headers=headerjson)
    # print(res.json())
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


def post_professional_getlist(tag, page, limit):  # 专精特新项目列表
    """
        获取产业基金分布
        :return: 自定义的关键字返回结果 result
        """
    result = ResultBase()
    payload = {
        "tag": tag,
        "page": page,
        "limit": limit
    }
    res = api_fund_mj_request.post_professional_getlist_api(data=json.dumps(payload), headers=headerjson)
    # print(res.json())
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


def post_professional_publishTimes(city, province, tag, page, limit):  # 专精特新发布批次企业分布
    """
        获取产业基金分布
        :return: 自定义的关键字返回结果 result
        """
    result = ResultBase()
    payload = {
        "city": city,
        "limit": limit,
        "page": page,
        "province": province,
        "tag": tag
    }
    res = api_fund_mj_request.post_professional_publishTimes_api(data=json.dumps(payload), headers=headerjson)
    # print(res.json())
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


def post_professional_getProvincesTimes(city, province, tag, page, limit):  # 专精特新省域分布
    """
        获取产业基金分布
        :return: 自定义的关键字返回结果 result
        """
    result = ResultBase()
    payload = {
        "city": city,
        "limit": limit,
        "page": page,
        "province": province,
        "tag": tag
    }
    res = api_fund_mj_request.post_professional_getProvincesTimes_api(data=json.dumps(payload), headers=headerjson)
    # print(res.json())
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


def post_professional_getMapOfCountry(province, tag):  # 专精特新发地图点位数据
    """
        获取产业基金分布
        :return: 自定义的关键字返回结果 result
        """
    result = ResultBase()
    payload = {
        "province": province,
        "tag": tag
    }
    res = api_fund_mj_request.post_professional_getMapOfCountry_api(data=json.dumps(payload), headers=headerjson)
    # print(res.json())
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


def post_professional_ipoTimes():  # 专精特新发地图点位数据
    """
        获取产业基金分布
        :return: 自定义的关键字返回结果 result
        """
    result = ResultBase()
    res = api_fund_mj_request.get_professional_ipoTimes_api(headers=headerform)
    # print(res.json())
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


def post_professional_getPieChart(charttype):  # 专精特新领域分布
    """
        获取产业基金分布
        :return: 自定义的关键字返回结果 result
        """
    result = ResultBase()
    res = api_fund_mj_request.get_professional_getPieChart_api(charttype, headers=headerform)
    # print(res.json())
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


def post_honour_ipoTimes():  # 光荣榜融资轮次
    """
        获取产业基金分布
        :return: 自定义的关键字返回结果 result
        """
    result = ResultBase()
    res = api_fund_mj_request.get_honour_ipoTimes_api(headers=headerform)
    # print(res.json())
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


def post_honour_rank(ranktype):  # 光荣榜榜单分布
    """
        获取产业基金分布
        :return: 自定义的关键字返回结果 result
        """
    result = ResultBase()
    res = api_fund_mj_request.get_honour_rank_api(ranktype, headers=headerform)
    # print(res.json())
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


def post_honour_getlist(listname, page, limit):  # 光荣榜项目列表
    """
        获取产业基金分布
        :return: 自定义的关键字返回结果 result
        """
    result = ResultBase()
    payload = {
        "province": listname,
        "page": page,
        "limit": limit
    }
    res = api_fund_mj_request.post_honour_getlist_api(data=json.dumps(payload), headers=headerjson)
    # print(res.json())
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

def post_honour_getSixStatistic():  # 光荣榜数据汇总
    """
        获取产业基金分布
        :return: 自定义的关键字返回结果 result
        """
    result = ResultBase()
    res = api_fund_mj_request.get_honour_getSixStatistic_api(headers=headerform)
    # print(res.json())
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
