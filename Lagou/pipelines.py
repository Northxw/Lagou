# -*- coding: utf-8 -*-

import logging
import pymysql
from twisted.enterprise import adbapi
from openpyxl import Workbook
import codecs
import json

class MysqlTwistedPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_crawler(cls,crawler):
        params = dict(
            host=crawler.settings.get('MYSQL_HOST'),
            database=crawler.settings.get('MYSQL_DB'),
            user=crawler.settings.get('MYSQL_USER'),
            password=crawler.settings.get('MYSQL_PASSWORD'),
            port=crawler.settings.get('MYSQL_PORT'),
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=True
        )
        dbpool = adbapi.ConnectionPool("pymysql", **params)
        return cls(dbpool)

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self.do_insert, item, spider)
        query.addErrback(self.handle_error, spider)

    def handle_error(self, failure, spider):
        spider.crawler.stats.inc_value('Failed_Insert_DB')
        logging.error("Failed Insert DB: %s" % failure)

    def do_insert(self, cursor, item, spider):
        data = dict(item)
        keys = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        sql = "INSERT INTO {table} ({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE".format(
            table=item.table, keys=keys, values=values)
        update = ', '.join([" {key} = %s".format(key=key) for key in data])
        sql += update
        cursor.execute(sql, tuple(data.values())*2)
        spider.crawler.stats.inc_value('Success_Inserted_DB')

class ExcelPipeline(object):
    def __init__(self):
        # 实例化
        self.wb = Workbook()
        # 激活工作表
        self.ws = self.wb.active
        self.ws.append(['ID', 'PositionURL', 'PositionName', 'Salary', 'Avg_Salary', 'PublishTime', 'WorkYear', 'Education', 'JobNature',
                        'Advantage', 'City', 'CompanyFullName', 'CompanyURL'])

    def process_item(self, item, spider):
        datas = dict(item)
        line_datas = [''.join(value) for value in datas.values()]
        self.ws.append(line_datas)
        self.wb.save('./utils/Lagou_Position.xlsx')
        spider.crawler.stats.inc_value('Success_Append_Excel')
        return item

class JsonPipeline(object):
    def open_spider(self, spider):
        self.file = codecs.open('houseinfo.json', 'w', encoding='utf-8')
        self.file.write(b'[\n')

    def process_item(self, item, spider):
        # 序列化
        lines = '{}\n'.format(json.dumps(dict(item), indent=2, ensure_ascii=False))
        self.file.write(lines)
        return item

    def close_spider(self, spider):
        self.file.write(b']')
        self.file.close()