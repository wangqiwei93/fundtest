from common.logger import logger
from common.mysql_operate import db


class Overview_Sql():

    # 项目下穿
    def projectinfopage(self, year, quarter, areaName, proType):

        if areaName != '浙江省' and proType != '':
            sql = "SELECT project_id,project_name,com_city,com_county,fund_name," \
                  "CASE WHEN `investment_state` is null THEN '-' when `investment_state` = 1 then '投资期' " \
                  " when `investment_state` = 2 then '退出期' when `investment_state` = 3 then '已到期' " \
                  "END as `investment_state`,chinese_indus_type as '所属领域',sum_amount as '项目总规模'," \
                  "fund_invest_amount as '基金投资额',project_equity_amount as '社会资本出资' from " \
                  "dws_through_project_info WHERE '%s' and `data_year` =  '%s'" \
                  " and data_quarter = '%s' and data_city = '%s'" % (
                      str(proType), str(year), str(quarter), str(areaName))
        elif areaName != '浙江省' and proType == '':
            sql = "SELECT project_id,project_name,com_city,com_county,fund_name," \
                  "CASE WHEN `investment_state` is null THEN '-' when `investment_state` = 1 then '投资期' " \
                  " when `investment_state` = 2 then '退出期' when `investment_state` = 3 then '已到期' " \
                  "END as `investment_state`,chinese_indus_type as '所属领域',sum_amount as '项目总规模'," \
                  "fund_invest_amount as '基金投资额',project_equity_amount as '社会资本出资' from " \
                  "dws_through_project_info WHERE `data_year` =  '%s'" \
                  " and data_quarter = '%s' and data_city = '%s'" % (
                      str(year), str(quarter), str(areaName))
        elif areaName == '浙江省' and proType != '':
            sql = "SELECT project_id,project_name,com_city,com_county,fund_name,CASE WHEN `investment_state` is null " \
                  "THEN '-' when `investment_state` = 1 then '投资期'  when `investment_state` = 2 then '退出期' when " \
                  "`investment_state` = 3 then '已到期' END as `investment_state`,chinese_indus_type as '所属领域',sum_amount " \
                  "as '项目总规模',fund_invest_amount as '基金投资额',project_equity_amount as '社会资本出资' from " \
                  "dws_through_project_info_aera WHERE pro_type = '%s' and `data_year` = '%s'  and data_quarter = '%s' " \
                  "and data_city is null UNION ALL SELECT project_id,project_name,com_city,com_county,fund_name," \
                  "CASE WHEN `investment_state` is null THEN '-' when `investment_state` = 1 then '投资期'  when " \
                  "`investment_state` = 2 then '退出期' when `investment_state` = 3 then '已到期' END as `investment_state`," \
                  "chinese_indus_type as '所属领域',sum_amount as '项目总规模',fund_invest_amount as '基金投资额'," \
                  "project_equity_amount as '社会资本出资' from dws_through_project_info_aera WHERE `data_year` = '%s' " \
                  "and data_quarter = '%s' and data_city is null and is_area_fund_pro = 1" % (str(proType), str(year), str(quarter),
                                                                                              str(year), str(quarter))
        elif areaName == '浙江省' and proType == '':
            sql = "SELECT project_id,project_name,com_city,com_county,fund_name," \
                  "CASE WHEN `investment_state` is null THEN '-' when `investment_state` = 1 then '投资期' " \
                  " when `investment_state` = 2 then '退出期' when `investment_state` = 3 then '已到期' " \
                  "END as `investment_state`,chinese_indus_type as '所属领域',sum_amount as '项目总规模'," \
                  "fund_invest_amount as '基金投资额',project_equity_amount as '社会资本出资' from " \
                  "dws_through_project_info WHERE `data_year` = '%s' " \
                  " and data_quarter = '%s' and data_city is null " \
                  "UNION ALL SELECT project_id,project_name,com_city,com_county,fund_name," \
                  "CASE WHEN `investment_state` is null THEN '-' when `investment_state` = 1 then '投资期'  when " \
                  "`investment_state` = 2 then '退出期' when `investment_state` = 3 then '已到期' END as `investment_state`," \
                  "chinese_indus_type as '所属领域',sum_amount as '项目总规模',fund_invest_amount as '基金投资额'," \
                  "project_equity_amount as '社会资本出资' from dws_through_project_info_aera WHERE `data_year` = '%s' " \
                  "and data_quarter = '%s' and data_city is null and is_area_fund_pro = 1" % (
                      str(year), str(quarter), str(year), str(quarter))
        logger.info("执行sql：%s" % sql)
        data_list = db.select_db(sql)
        return data_list


if __name__ == '__main__':
    print(Overview_Sql().projectinfopage(2022, 2, '浙江省', ''))
    # print(Overview_Sql().projectinfopage(2021,4,'浙江省',''))
