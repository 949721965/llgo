""" 浏览器驱动程序
"""

from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('blink-settings=imagesEnabled=false')

driver = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=options)
