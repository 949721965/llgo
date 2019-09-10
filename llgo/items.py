""" 存储条目
  id            索引值
  category      职位分类
  branch        职位分支
  position      职位名称
  jobname       工作名称
  salarylower   薪资最低（单位k)
  salaryupper   薪资最高（单位k)    
  location      工作地点
  experience    工作经验
  education     学历要求
  advantage     工作诱惑
  duties        工作职责
  claim         技能要求
  companyname   公司名称
  companyfield  公司领域
  financing     融资情况
  scalelower    公司规模（不小于）
  scaleupper    公司规模（不大于）
"""

import scrapy


class LlgoItem(scrapy.Item):
    id_ = scrapy.Field()  索引值
    category = scrapy.Field()
    branch = scrapy.Field()
    position = scrapy.Field()
    jobname = scrapy.Field()
    salarylower = scrapy.Field()
    salaryupper = scrapy.Field()
    location = scrapy.Field()
    experience = scrapy.Field()
    education = scrapy.Field()
    advantage = scrapy.Field()
    duties = scrapy.Field()
    claim = scrapy.Field()
    companyname = scrapy.Field()
    companyfield = scrapy.Field()
    financing = scrapy.Field()
    scalelower = scrapy.Field()
    scaleupper = scrapy.Field()
