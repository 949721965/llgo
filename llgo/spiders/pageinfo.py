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
      for cookie in config.COOKIE:
        self._driver.add_cookie(cookie)

    def _request(self, start_url):
      url = start_url % self._current_item
      self._driver.get(url)
      response = scrapy.http.HtmlResponse(
                url, body=driver.page_source.encode('UTF-8'))
      self._parse_homepage(response)
      self._current_item = self._current_item + 1
      print('解析完成：%s\n' % url)
      self._request(start_url)


    def _parse_homepage(self, response):
      """ 解析招聘信息主页地址，并将主页地址存储到文件中。"""
      homepages = response.xpath(config.XPATH_HOMEPAGE).extract()
      if not len(homepages):
        self._task_completed()
      with open(self._storage_dir + str(self._current_item), 'w') as f:
        json.dump(homepages, f)

    def _task_completed(self):
      """ 任务结束后做一些清理工作，并退出程序。"""
      self._driver.quit()
      sys.exit(0)


if __name__ == "__main__":
    pageinfo = PageInfo('技术','后端开发','Java')
    pageinfo.start_crawl()
