# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LlgoItem(scrapy.Item):
    mark = scrapy.Field()
    category = scrapy.Field()
    branch = scrapy.Field()
    job = scrapy.Field()
    job_name = scrapy.Field()
    salary_lower = scrapy.Field()
    salary_upper = scrapy.Field()
    area = scrapy.Field()
    experience = scrapy.Field()
    education = scrapy.Field()
    labels = scrapy.Field()
    advantage = scrapy.Field()
    requirement = scrapy.Field()
