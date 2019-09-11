"""
"""

import scrapy
from llgo import config

class PageInfo(scrapy.Spider):
    name = 'EmployInfo'
    domain = config.DOMAIN

    def __init__(self):
      pass

    