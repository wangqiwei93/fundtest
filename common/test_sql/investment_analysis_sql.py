from common.logger import logger
from common.mysql_operate import db


class FundMj_Sql():

    def field_list_sql(self, label):  # 重大项目领域分布

        sql = "SELECT field_type,field_count,CASE WHEN domanial_type = 1 THEN '先进制造' WHEN domanial_type = 2" \
              " THEN '三大科创' WHEN domanial_type = 3 THEN '十大标志性产业' END as domanial_type,field_proportion FROM " \
              "dws_fund_mj_cast_pro_field_basic_info WHERE type_flag = 0 and domanial_type = %d" % (int(label))
        logger.info("执行sql：%s" % sql)
        data_list = db.select_db(sql)
        return data_list

    def group_count_sql(self, grouptype):
        if grouptype == 1:
            sql = "SELECT COUNT(*) as countpro,ROUND(SUM(total_scala_two),1) as total_scala_two,project_source FROM " \
                  "dws_fund_mj_reserve_pro_reform_basic_info GROUP BY project_source ORDER BY project_source DESC"
        elif grouptype == -1:
            sql = "SELECT COUNT(*) as countpro,ROUND(SUM(total_scala_two),1) as total_scala_two FROM " \
                  "dws_fund_mj_reserve_pro_reform_basic_info"
        elif grouptype == 2:
            sql = "SELECT COUNT(*) as countpro,ROUND(SUM(total_scala_two),1) as total_scala_two,creator_id FROM " \
                  "dws_fund_mj_reserve_pro_reform_basic_info WHERE (creator_id is not null and creator_id != '其他') " \
                  "GROUP BY creator_id ORDER BY creator_id DESC"
        elif grouptype == 0:
            sql = "SELECT COUNT(*) as countpro,ROUND(SUM(total_scala_two),1) as total_scala_two,project_city as " \
                  "creator_id FROM dws_fund_mj_reserve_pro_reform_basic_info WHERE project_city != '' GROUP BY project_city"
        logger.info("执行sql：%s" % sql)
        data_list = db.select_db(sql)
        return data_list

    def fund_mj_list(self):
        sql = "SELECT id,major_project,comp_name,project_source,field_investment,total_scala_two FROM " \
              "dws_fund_mj_reserve_pro_reform_basic_info ORDER BY total_scala_two desc"
        logger.info("执行sql：%s" % sql)
        data_list = db.select_db(sql)
        return data_list

    def fund_mj_queryDwsFundMjCityMap_sql(self):  # 产业已投项目列表
        sql = "SELECT * FROM dws_fund_mj_cast_pro_reform_basic_info ORDER  BY project_city"
        logger.info("执行sql：%s" % sql)
        data_list = db.select_db(sql)
        return data_list

    def professional_getOverview_sql(self, tag):
        if tag == '全国':
            sql = "SELECT SUM(countpro) countpro,SUM(fundcount) fundcount,SUM(fundamount) fundamount FROM( SELECT COUNT(*) as countpro," \
                  "0 as fundcount,0 as fundamount FROM dws_fund_mj_specialization_new_basic_info WHERE area_flag = 0 " \
                  "UNION ALL SELECT 0 as countpro,COUNT(*) as fundcount,round(SUM(reg_capital_number)/10000,1) as " \
                  "fundamount FROM dws_fund_mj_specialization_new_basic_info WHERE area_flag = 0 and is_fund = 1 )a"
        else:
            sql = "SELECT SUM(countpro) countpro,SUM(fundcount) fundcount,SUM(fundamount) fundamount FROM(SELECT COUNT(*) as countpro,0 as fundcount" \
                  ",0 as fundamount FROM dws_fund_mj_specialization_new_basic_info WHERE area_flag = 1 UNION ALL " \
                  "SELECT 0 as countpro,COUNT(*) as fundcount,round(SUM(reg_capital_number)/10000,1) as fundamount " \
                  "FROM dws_fund_mj_specialization_new_basic_info WHERE area_flag = 1 and is_fund = 1 )a"
        logger.info("执行sql：%s" % sql)
        data_list = db.select_db(sql)
        return data_list

    def professional_getlist_sql(self, tag):
        if tag == '全国':
            sql = "SELECT * FROM dws_fund_mj_specialization_new_basic_info WHERE area_flag = 0 " \
                  "ORDER BY is_fund DESC,specialization_batch"
        else:
            sql = "SELECT * FROM dws_fund_mj_specialization_new_basic_info WHERE area_flag = 1 " \
                  "ORDER BY is_fund DESC,specialization_batch"
        logger.info("执行sql：%s" % sql)
        data_list = db.select_db(sql)
        return data_list

    def professional_publishTimes_sql(self):  # 专精特新发布批次企业分布
        sql = "SELECT SUM(conprocount) as conprocount,SUM(fundprocount) as fundprocount,specialization_batch FROM(" \
              "SELECT COUNT(*) conprocount, 0 as fundprocount,specialization_batch FROM " \
              "dws_fund_mj_specialization_new_basic_info WHERE area_flag = 0 GROUP BY specialization_batch UNION ALL " \
              "SELECT 0 as conprocount,COUNT(*) as fundprocount,specialization_batch FROM " \
              "dws_fund_mj_specialization_new_basic_info WHERE area_flag = 0 and is_fund = 1 " \
              "GROUP BY specialization_batch)as a GROUP BY specialization_batch"
        logger.info("执行sql：%s" % sql)
        data_list = db.select_db(sql)
        return data_list

    def professional_getProvincesTimes_sql(self):  # 专精特新省域分布
        sql = "SELECT * FROM(SELECT COUNT(*) totalCount,specialization_batch,project_province FROM dws_fund_mj_specialization_" \
              "new_basic_info WHERE area_flag = 0 GROUP BY project_province,specialization_batch) as a"
        logger.info("执行sql：%s" % sql)
        data_list = db.select_db(sql)
        return data_list

    def professional_getMapOfCountry_sql(self):  # 专精特新地图
        sql = "SELECT COUNT(*) procount,project_province FROM dws_fund_mj_specialization_new_basic_info " \
              "WHERE area_flag = 0 GROUP BY project_province ORDER BY project_province"
        logger.info("执行sql：%s" % sql)
        data_list = db.select_db(sql)
        return data_list

    def professional_ipoTimes_sql(self):  # 专精特新融资轮次
        sql = "SELECT COUNT(*) procount,financing_rounds FROM dws_fund_mj_specialization_new_basic_info WHERE " \
              "area_flag = 1 and financing_rounds is not null GROUP BY financing_rounds"
        logger.info("执行sql：%s" % sql)
        data_list = db.select_db(sql)
        return data_list

    def professional_getPieChart_sql(self, charttype):  # 专精特新领域分布
        sql = "SELECT field_type,field_count,CASE WHEN domanial_type = 1 THEN '先进制造' WHEN domanial_type = 2 " \
              "THEN '三大科创' WHEN domanial_type = 3 THEN '十大标志性产业' END as domanial_type,field_proportion FROM " \
              "dws_fund_mj_cast_pro_field_basic_info WHERE type_flag = 1 and domanial_type = %d" % charttype
        logger.info("执行sql：%s" % sql)
        data_list = db.select_db(sql)
        return data_list

    def honour_ipoTimes_sql(self):  # 光荣榜融资轮次
        sql = "SELECT COUNT(*) countpro,financing_rounds FROM dws_fund_mj_high_quality_basic_info WHERE " \
              "financing_rounds is not null and financing_rounds != '其他'  GROUP BY financing_rounds"
        logger.info("执行sql：%s" % sql)
        data_list = db.select_db(sql)
        return data_list

    def honour_rank_sql(self, ranktype):  # 光荣榜榜单分布
        if ranktype == 1:
            sql = "SELECT (SUM(count1) + SUM(count2)) as '总数',SUM(count1) as '产业基金已投',SUM(count2) as" \
                  " '产业基金未投',list FROM( SELECT COUNT(*) as count1,0 as count2,listtype.high_type_list as list" \
                  " FROM dim_list_type as listtype LEFT JOIN dws_fund_mj_high_quality_basic_info as info on " \
                  "listtype.id = info.list_type  WHERE info.is_fund = 1 and type_flag = 1 GROUP BY info.list_type" \
                  " UNION ALL SELECT 0 as count1,COUNT(*) as count2,listtype.high_type_list as list FROM dim_list_type" \
                  " as listtype LEFT JOIN dws_fund_mj_high_quality_basic_info as info on listtype.id = info.list_type" \
                  "  WHERE (info.is_fund != 1 or info.is_fund is null) and type_flag = 1 GROUP BY info.list_type " \
                  ")as a GROUP BY list"
        else:
            sql = "SELECT (SUM(count1) + SUM(count2)) as '总数',SUM(count1) as '产业基金已投'," \
                  "SUM(count2) as '产业基金未投',list FROM( SELECT COUNT(*) as count1,0 as count2," \
                  "listtype.high_type_list as list FROM dim_list_type as listtype LEFT JOIN " \
                  "dws_fund_mj_high_quality_basic_info as info on listtype.id = info.list_type  WHERE " \
                  "info.is_fund = 1 and type_flag = 2 GROUP BY info.list_type UNION ALL SELECT 0 as count1" \
                  ",COUNT(*) as count2,listtype.high_type_list as list FROM dim_list_type as listtype LEFT JOIN" \
                  " dws_fund_mj_high_quality_basic_info as info on listtype.id = info.list_type  WHERE " \
                  "(info.is_fund != 1 or info.is_fund is null) and type_flag = 2 GROUP BY info.list_type " \
                  ")as a GROUP BY list"
        logger.info("执行sql：%s" % sql)
        data_list = db.select_db(sql)
        return data_list

    def honour_getlist_sql(self):  # 光荣榜融资轮次
        sql = "SELECT * FROM dws_fund_mj_high_quality_basic_info"
        logger.info("执行sql：%s" % sql)
        data_list = db.select_db(sql)
        return data_list

    def honour_getSixStatistic_sql(self):  # 光荣榜融资轮次
        sql = "SELECT SUM(make_count) make_count,SUM(make_fund_count) make_fund_count,SUM(digital_count) " \
              "digital_count,SUM(digital_fund_count) digital_fund_count FROM(SELECT count(*) make_count, " \
              "0 make_fund_count,0 digital_count,0 digital_fund_count FROM dws_fund_mj_high_quality_basic_info" \
              " WHERE type_flag = 1 UNION ALL SELECT 0 make_count,count(*) make_fund_count,0 digital_count," \
              "0 digital_fund_count FROM dws_fund_mj_high_quality_basic_info WHERE type_flag = 1 and is_fund = 1" \
              " UNION ALL SELECT 0 make_count, 0 make_fund_count,count(*) digital_count,0 digital_fund_count FROM" \
              " dws_fund_mj_high_quality_basic_info WHERE type_flag = 2 UNION ALL SELECT 0 make_count, 0 " \
              "make_fund_count,0 digital_count,count(*) digital_fund_count FROM dws_fund_mj_high_quality_basic_info" \
              " WHERE type_flag = 2 and is_fund = 1)a"
        logger.info("执行sql：%s" % sql)
        data_list = db.select_db(sql)
        return data_list
# print(round((float(FundMj_Sql().field_list_sql(1)[0]['field_proportion']))*100,2))
# print(type(FundMj_Sql().fund_mj_list()[0]['total_scala_two']))
print((FundMj_Sql().honour_getSixStatistic_sql()))
