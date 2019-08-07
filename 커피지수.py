


# 모듈 준비하기
import requests
import json
import pandas as pd
from pandas.io.json import json_normalize
import folium


## 스타벅스 매장 크롤링하기
# 참고 https://brunch.co.kr/@jk-lab/18

from selenium import webdriver
chromedriver_dir = 'D:\Heechul\Python_Crawling/chromedriver.exe'
driver = webdriver.Chrome(chromedriver_dir)
driver.get('https://www.istarbucks.co.kr/store/store_map.do')
loca = driver.find_element_by_class_name('loca_search')
loca.click()
sido = driver.find_element_by_class_name('sido_area_box')
li = sido.find_element_by_tag_name('li')


