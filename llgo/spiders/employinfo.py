"""
"""

import scrapy
from llgo import config

class EmployInfo(scrapy.Spider):
    name = 'EmployInfo'
    domain = config.DOMAIN

    def __init__(self):
      pass
    
    def start_requests(self):
      pass
    
    def parse(self, response):
      pass

    def extract_id(self, response):
      pass
    
    def extract_category(self, response):
      pass
    
    def extract_branch(self, response):
      pass
    
    def extract_position(self, response):
      pass
    
    def extract_jobname(self, response):
      pass
    
    def extract_salarylower(self, response):
      pass
    
    def extract_salaryupper(self, response):
      pass
    
    def extract_location(self, response):
      pass
    
    def extract_experience(self, response):
      pass
    
    def extract_education(self, response):
      pass
    
    def extract_advantage(self, response):
      pass
    
    def extract_duties(self, response):
      pass
    
    def extract_claim(self, response):
      pass
    
    def extract_companyname(self, response):
      pass
    
    def extract_companyfield(self, response):
      pass
    
    def extract_financing(self, response):
      pass
    
    def extract_scalelower(self, response):
      pass
    
    def extract_scaleupper(self, response):
      pass
