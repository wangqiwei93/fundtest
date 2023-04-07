import json
import os

import pytest

from core.result_base import ResultBase
from api.api_projectlib import projectlib
from common.read_data import data

global headerjson
global headerform
BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")

data = data.load_ini(data_file_path)["test_token"]

tokeng = data['TOKEN']
# tokeng = 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0ZXN0d3F3MSIsImxvZ2luX3VzZXJfa2V5IjoiOGEyZDFkNmUtY2EzZi00Zjc0LWJmMmItZmU3NTBlODJlYzk4In0.7B8Ss_AdLCQnqLutbQS9xDAWyIVtNOpgk2WoXuyAODaU-Tv7bpnRuENx10Lsk_S4zp1QmRiVOYwFxbyF4uwS7w'

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


# 项目库列表接口
def get_projectlib_getgrojectlist(limit, page):
    """
    获取基金列表
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    payload = json.dumps({
        "page": page,
        "limit": limit,
        "nationalIndustryCode": "",
        "newTypeCode": "",
        "area": "",
        "isFund": 0,
        "hotProjectCode": "",
        "directoryLabel": "",
        "proChain": "",
        "year": None,
        "regScale": None,
        "comType": "",
        "sslx": "",
        "keyword": None
    })
    # print("**********************", year)
    # 产业基金详情接口
    res = projectlib.get_projectlib_getprojectlist(data=payload, headers=headerjson)
    result.success = True
    try:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['message'])
        result.msg = res.json()['message']
        result.response = res
        result.code = res.json()['code']
        result.data = res.json()['data']
    except Exception as e:
        try:
            result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['msg'])
            result.code = res.json()['code']
            result.response = res
            result.msg = res.json()['msg']
        except Exception as e:
            result.error = "接口返回码是 【 {} 】".format(res.json()['code'])
            result.code = res.json()['code']
    return result


# 项目库列表接口
def get_projectlib_getgrojectlist_one(labecode, fundtype):
    """
    获取基金列表
    :return: 自定义的关键字返回结果 result
    """

    result = ResultBase()
    payload = json.dumps({
        "page": 1,
        "limit": 100,
        "nationalIndustryCode": labecode,
        "newTypeCode": "",
        "area": "",
        "isFund": fundtype,
        "hotProjectCode": "",
        "directoryLabel": "",
        "proChain": "",
        "year": None,
        "regScale": None,
        "comType": "",
        "sslx": "",
        "keyword": None
    })
    # print("**********************", year)
    # 产业基金详情接口
    res = projectlib.get_projectlib_getprojectlist(data=payload, headers=headerjson)
    # print(res.json())
    result.success = True
    try:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['message'])
        result.msg = res.json()['message']
        result.response = res
        result.code = res.json()['code']
        result.data = res.json()['data']
    except Exception as e:
        try:
            result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['msg'])
            result.code = res.json()['code']
            result.response = res
            result.msg = res.json()['msg']
        except Exception as e:
            result.error = "接口返回码是 【 {} 】".format(res.json()['code'])
            result.code = res.json()['code']
    return result


# 项目库产业链列表接口
def get_projectlib_getgrojectlist_two(labecode):
    """
    获取基金列表
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    payload = json.dumps({
        "page": 1,
        "limit": 100,
        "nationalIndustryCode": "",
        "newTypeCode": "",
        "area": "",
        "isFund": None,
        "hotProjectCode": "",
        "directoryLabel": "",
        "proChain": labecode,
        "year": None,
        "regScale": None,
        "comType": "",
        "sslx": "",
        "keyword": None
    })
    # print("**********************", year)
    # 产业基金详情接口
    res = projectlib.get_projectlib_getprojectlist(data=payload, headers=headerjson)
    # print(res.json())
    result.success = True
    try:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['message'])
        result.msg = res.json()['message']
        result.response = res
        result.code = res.json()['code']
        result.data = res.json()['data']
    except Exception as e:
        try:
            result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()['code'], res.json()['msg'])
            result.code = res.json()['code']
            result.response = res
            result.msg = res.json()['msg']
        except Exception as e:
            result.error = "接口返回码是 【 {} 】".format(res.json()['code'])
            result.code = res.json()['code']
    return result