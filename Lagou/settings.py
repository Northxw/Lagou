# -*- coding: utf-8 -*-

import random

BOT_NAME = 'Lagou'

SPIDER_MODULES = ['Lagou.spiders']
NEWSPIDER_MODULE = 'Lagou.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 100

DOWNLOAD_DELAY = eval('%.1f'%random.random())

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'Lagou.middlewares.RandomUAMiddleware': 543,
    'Lagou.middlewares.ProxyMiddleware': 544,
    'Lagou.middlewares.DownloadRetryMiddleware': 545,
}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'Lagou.pipelines.ExcelPipeline': 290,
    'Lagou.pipelines.MysqlTwistedPipeline': 300,
    # 'Lagou.pipelines.JsonPipeline': 302
}

# SETITNG DOWNLOAD TIMEOUT
DOWNLOAD_TIMEOUT = 10

# MAX PAGE
MAX_PAGES = 50

# MYSQL SEETINGS
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '123456'
MYSQL_DB = 'lagou'
MYSQL_PORT = 3306

# SMTP SETTINGS
SMTP_HOST = 'smtp.163.com'
SMTP_USER = 'northxw@163.com'
SMTP_AUTHCODE = '123456'
SMTP_PORT = '465'
SENDER = 'northxw@163.com'
SUBJECT = 'Crawler Status Report'
RECEIVE_LIST = ['northxw@qq.com', 'northxw@sina.com']

# Abuyun_Proxy
PROXY_SERVER = "http://http-dyn.abuyun.com:9020"
PROXY_USER = "H8686H93Q18O3M3D"
PROXY_PASS = "E868F2FAFC2B93BA"