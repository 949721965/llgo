""" 抓取招聘信息主页的地址 
"""

import os
import sys
import json
import time
import scrapy
sys.path.append('/home/mxsyx/desktop/llgo')

from llgo import config
from llgo.chrome import driver


class PageInfo():
    def __init__(self, category, branch, position):
      self._driver = driver
      self._current_item = 1
      self._start_url = config.START_URLS[category][branch][position]
      self._storage_dir = 'urls/%s/%s/%s/' % (category, branch, position)

    def start_crawl(self):
      self._driver.get(config.DOMAIN)
      self._add_cookie()
      self._request(self._start_url)

    def _add_cookie(self):
      """ 增加与登录有关的Cookie """
      for cookie in config.COOKIES:
        self._driver.add_cookie(cookie)

    def _request(self, start_url):
      """ 调用浏览器驱动程序请求网页  将请求到的网页
      封装为Scrapy的response对象并传递给主页地址解
      析函数进行解析，这是一个递归函数。
      """
      url = start_url % self._current_item
      self._driver.get(url)
      response = scrapy.http.HtmlResponse(
                url, body=driver.page_source.encode('UTF-8'))
      self._parse_homepage(response)
      self._current_item = self._current_item + 1
      print('解析完成：%s\r' % url, end='')
      self._request(start_url)

    def _parse_homepage(self, response):
      """ 解析招聘信息主页地址，并将主页地址存储到文件中。"""
      homepages = response.xpath(config.XPATH_HOMEPAGE).extract()
      if not len(homepages): # 到达链接末尾
        self._end_task()
      with open(self._storage_dir + str(self._current_item), 'w') as f:
        json.dump(homepages, f)

    def _end_task(self):
      """ 任务结束后做一些清理工作，并退出程序。"""
      self._driver.quit()
      print('\n任务结束！最后的条目值： %s' % self._current_item)
      sys.exit(0)


if __name__ == "__main__":
    pageinfo = PageInfo('技术','后端开发','搜索算法')
    pageinfo.start_crawl()
