### 이디야 커피 크롤링하기

# 모듈 준비하기
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from urllib.request import urlopen
import time


from selenium import webdriver
chromedriver_dir = 'D:\Heechul\Python_Crawling/chromedriver.exe'
driver = webdriver.Chrome(chromedriver_dir)

driver.get('')
loca = driver.find_element_by_class_name('region_srh')
loca.click()
time.sleep(5)

sido = driver.find_element_by_class_name('sido_arae_box')
li = sido.find_elements_by_tag_name('li')
li[i].click()
time.sleep(5)

gugun = driver.find_element_by_class_name('gugun_arae_box')
guli = gugun.find_element_by_tag_name('li')
guli.click()
time.sleep(5)

source = driver.page_source
bs = bs4.BeautifulSoup(source,'lxml')
entire = bs.find('ul', class_ = 'quickSearchResultBoxSidoGugun')
li_list = entire.find_all('li')


for info in li_list:
    name.append(info['data-name'])

    tmp_address = info.find('p').get_text().split()[:-1]
    tmp_address = ' '.join(tmp_address)
    address.append(tmp_address)

    lat.append(info['data-lat'])

    log.append(info['data-long'])
