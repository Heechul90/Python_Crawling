### 커피빈 매장 크롤링하기

# 모듈 준비하기
import bs4
import time
import pandas as pd
import numpy as np
from selenium import webdriver

from bs4 import BeautifulSoup
from urllib.request import urlopen

# 참고 https://brunch.co.kr/@jk-lab/18

from selenium import webdriver
chromedriver_dir = 'D:\Heechul\Python_Crawling/chromedriver.exe'
driver = webdriver.Chrome(chromedriver_dir)

name = []
address = []
lat = []
log = []

for i in range(17):
    driver.get('https://www.istarbucks.co.kr/store/store_map.do')
    loca = driver.find_element_by_class_name('loca_search')
    time.sleep(5)

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
    print(i)

name
address
lat
log

starbucks = pd.DataFrame({'Name': name,
                          'Address': address,
                          'Lat': lat,
                          'Log': log})
len(starbucks)
starbucks.to_csv('Starbucks/Starbucks.csv')

data = pd.read_csv('Starbucks/Starbucks.csv')



# url 가져오기
url_base = 'http://www.chicagomag.com'
url_sub = '/Chicago-Magazine/November-2012/Best-Sandwiches-Chicago/'
url = 'https://www.coffeebeankorea.com/store/store_data2.asp?lat=&lng=&chk1=0&chk2=0&chk3=0&chk4=0&chk5=0&chk6=0&chk7=0&chk8=0&chk9=0&keyword=&StoreLocal=%EC%84%9C%EC%9A%B8&StoreLocal2=&storeNo='
url
# html 열기
html = urlopen(url)
soup = BeautifulSoup(html, "html.parser")
soup.get_text()

# find_all 명령어를 통해 div의 sammy태그를 찾아 확인
# 내가 찾고자 하는것이 맞는지 확인
print(soup.find_all('div', 'sammy'))
len(soup.find_all('div', 'sammy'))
print(soup.find_all('div', 'sammy')[0])
