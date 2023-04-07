from common.logger import logger
from common.mysql_operate import db


class ProJect_Sql():
    # 查询项目库国民行业标签
    def industry_code(self):
        sql = "select code,`name` FROM zjjk_fund_industry"
        logger.info("执行sql：%s" % sql)
        data_list = db.select_db(sql)
        codelist = []
        for i in range(len(data_list)):
            print(len(data_list[i]['code']))
            if len(data_list[i]['code']) > 3:
                codelist.append([data_list[i]['code'], data_list[i]['name'], True, 200, '操作成功'])
        return codelist

    # 查询项目库国民行业标签
    def industry_code_2(self):
        sql = "select label_code,label_name FROM zjjk_fund_label"
        logger.info("执行sql：%s" % sql)
        data_list = db.select_db(sql)
        codelist = []
        for i in range(len(data_list)):
            print(len(data_list[i]['label_code']))
            if len(data_list[i]['label_code']) > 3:
                codelist.append([data_list[i]['label_code'], data_list[i]['label_name'], True, 200, '操作成功'])
        return codelist

    # 查询项目库产业链标签
    def industry_code_3(self):
        sql = "select code,name FROM zjjk_fund_chain"
        logger.info("执行sql：%s" % sql)
        data_list = db.select_db(sql)
        codelist = []
        for i in range(len(data_list)):
            if len(data_list[i]['code']) > 3:
                codelist.append([data_list[i]['code'], data_list[i]['name'], True, 200, '操作成功'])
        return codelist

    def project_list_sql_1(self, label):  # 国民行业
        # sql = "SELECT details.pro_name,details.com_name,details.is_industry_investment,incode.`name`," \
        #       "details.com_province,details.com_city,details.com_district,details.credit_code FROM " \
        #       "dwd_fund_project_details_info details LEFT JOIN (zjjk_fund_industry as incode LEFT JOIN " \
        #       "zjjk_fund_project_label_info as prolabel on incode.code = prolabel.label_code) ON " \
        #       "details.credit_code = prolabel.comp_code WHERE incode.code in('%s') and details.credit_code is not null " \
        #       "GROUP BY details.credit_code ORDER BY details.is_industry_investment DESC" % (str(label))

        sql = "select t.id,t.project_id,t.pro_name,t.credit_code,t.com_name,t.com_province,t.com_city,t.com_district," \
              "t.is_industry_investment,t.pro_province,t.pro_city,t.pro_district,t.com_industry from ( select *, " \
              "row_number() over(partition by " \
              "credit_code order by project_id desc) as rn from dwd_fund_project_details_info ) t LEFT JOIN " \
              "(zjjk_fund_industry i LEFT JOIN zjjk_fund_project_label_info l ON i.code = l.label_code)" \
              " on t.credit_code = l.comp_code where t.rn = 1 and i.`code` in('%s') and " \
              "t.credit_code is not null order by t.is_industry_investment desc" % (str(label))
        logger.info("执行sql：%s" % sql)
        data_list = db.select_db(sql)
        return data_list

    def project_list_sql_2(self, label):  # 新兴行业

        sql = "select t.id,t.project_id,t.pro_name,t.credit_code,t.com_name,t.com_province,t.com_city,t.com_district," \
              "t.is_industry_investment,t.pro_province,t.pro_city,t.pro_district,t.com_industry from ( select *, " \
              "row_number() over(partition by " \
              "credit_code order by project_id desc) as rn from dwd_fund_project_details_info ) t LEFT JOIN " \
              "(zjjk_fund_label i LEFT JOIN zjjk_fund_project_label_info l ON i.label_code = l.label_code)" \
              " on t.credit_code = l.comp_code where t.rn = 1 and i.label_code in('%s') and " \
              "t.credit_code is not null order by t.is_industry_investment desc" % (str(label))
        logger.info("执行sql：%s" % sql)
        data_list = db.select_db(sql)
        return data_list

    def project_list_sql_3(self, label):  # 产业链

        sql = "select t.id,t.project_id,t.pro_name,t.credit_code,t.com_name,t.com_province,t.com_city,t.com_district," \
              "t.is_industry_investment,t.pro_province,t.pro_city,t.pro_district,t.com_industry from ( select *, " \
              "row_number() over(partition by " \
              "credit_code order by project_id desc) as rn from dwd_fund_project_details_info ) t LEFT JOIN " \
              "(zjjk_fund_chain i LEFT JOIN zjjk_fund_project_label_info l ON i.code = l.label_code)" \
              " on t.credit_code = l.comp_code where t.rn = 1 and i.code in('%s') and " \
              "t.credit_code is not null order by t.is_industry_investment desc" % (str(label))
        logger.info("执行sql：%s" % sql)
        data_list = db.select_db(sql)
        return data_list

    def project_list_sql_4(self, label):  # 是否产业基金投资

        sql = "select t.id,t.project_id,t.pro_name,t.credit_code,t.com_name,t.com_province,t.com_city,t.com_district," \
              "t.is_industry_investment,t.pro_province,t.pro_city,t.pro_district,t.com_industry from ( select *, " \
              "row_number() over(partition by " \
              "credit_code order by project_id desc) as rn from dwd_fund_project_details_info ) t LEFT JOIN " \
              "(zjjk_fund_industry i LEFT JOIN zjjk_fund_project_label_info l ON i.code = l.label_code)" \
              " on t.credit_code = l.comp_code where t.rn = 1 and t.is_industry_investment %s and " \
              "t.credit_code is not null order by t.is_industry_investment desc" % (str(label))
        logger.info("执行sql：%s" % sql)
        data_list = db.select_db(sql)
        return data_list
# print(ProJect_Sql().project_list_sql('D441'))
# print(ProJect_Sql().industry_code())
# print(ProJect_Sql().industry_code_3())
print((ProJect_Sql().industry_code_3()))