xpaths = ['/html[1]/body[1]/div[5]/div[1]/div[1]/div[1]/h2[1]/text()',
 '/html[1]/body[1]/div[5]/div[1]/div[1]/dd[1]/h3[1]/span[1]/text()',
 '/html[1]/body[1]/div[5]/div[1]/div[1]/dd[1]/h3[1]/span[2]/text()',
 '/html[1]/body[1]/div[5]/div[1]/div[1]/dd[1]/h3[1]/span[3]/text()',
 '/html[1]/body[1]/div[5]/div[1]/div[1]/dd[1]/h3[1]/span[4]/text()',
 '/html[1]/body[1]/div[7]/div[1]/dl[1]/dd[1]/p[1]/text()',
 '/html[1]/body[1]/div[7]/div[1]/dl[1]/dd[2]/div[1]/p/text()',
 '/html[1]/body[1]/div[7]/div[2]/dl[1]/dt[1]/a[1]/div[1]/h3[1]/em[1]/text()',
 '/html[1]/body[1]/div[7]/div[2]/dl[1]/dd[1]/ul[1]/li[1]/h4[1]/text()',
 '/html[1]/body[1]/div[7]/div[2]/dl[1]/dd[1]/ul[1]/li[2]/h4[1]/text()',
 '/html[1]/body[1]/div[7]/div[2]/dl[1]/dd[1]/ul[1]/li[3]/h4[1]/text()']

import scrapy
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('blink-settings=imagesEnabled=false')
driver = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=options)


driver.get('')
res = scrapy.http.HtmlResponse('xx', body=driver.page_source.encode('UTF-8'))

for xpa in xpaths:
  print(res.xpath(xpa).extract())




