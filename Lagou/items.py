# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field
from scrapy.loader.processors import TakeFirst, Join, MapCompose
from Lagou.utils.common import get_avg_salary


class LagouItem(Item):
    table = 'position'
    id = Field(input_processor=Join())
    positiondetailurl = Field(input_processor=Join())
    positionname = Field(input_processor=Join())
    publishtime = Field(input_processor=Join())
    salary = Field(input_processor=Join())
    avg_salary = Field(input_processor=MapCompose(get_avg_salary))
    workyear = Field(input_processor=Join())
    education = Field(input_processor=Join())
    jobnature = Field(input_processor=Join())
    positionadvantage = Field(input_processor=Join())
    city = Field(input_processor=Join())
    companyfullName = Field(input_processor=Join())
    companyurl = Field(input_processor=Join())