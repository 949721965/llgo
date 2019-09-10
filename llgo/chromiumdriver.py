import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('blink-settings=imagesEnabled=false')
driver = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=options)
