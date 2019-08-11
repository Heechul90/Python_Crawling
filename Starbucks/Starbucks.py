### 스타벅스 매장 크롤링하기

# 모듈 준비하기
import bs4
import time
import pandas as pd
from selenium import webdriver

# 참고 https://brunch.co.kr/@jk-lab/18

chromedriver_dir = 'D:\Heechul\Python_Crawling/chromedriver.exe'
driver = webdriver.Chrome(chromedriver_dir)

name = []
address = []
lat = []
log = []


for i in range(17):
    driver.get('https://www.istarbucks.co.kr/store/store_map.do')
    loca = driver.find_element_by_class_name('loca_search')
    time.sleep(3)

    loca.click()
    time.sleep(3)

    sido = driver.find_element_by_class_name('sido_arae_box')
    li = sido.find_elements_by_tag_name('li')

    if i == 16:
        li[16].click()
        time.sleep(3)

        source = driver.page_source
        bs = bs4.BeautifulSoup(source, 'lxml')
        entire = bs.find('ul', class_='quickSearchResultBoxSidoGugun')
        li_list = entire.find_all('li')

        for info in li_list:
            name.append(info['data-name'])

            tmp_address = info.find('p').get_text().split()[:-1]
            tmp_address = ' '.join(tmp_address)
            address.append(tmp_address)

            lat.append(info['data-lat'])

            log.append(info['data-long'])
    else:
        li[i].click()
        time.sleep(3)

        gugun = driver.find_element_by_class_name('gugun_arae_box')
        guli = gugun.find_element_by_tag_name('li')
        guli.click()
        time.sleep(3)

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
len(address)
lat
log

starbucks = pd.DataFrame({'Name': name,
                          'Address': address,
                          'Lat': lat,
                          'Log': log})
len(starbucks)
starbucks.to_csv('Starbucks/Data/Starbucks_Raw.csv',
                 encoding = 'euc-kr',
                 sep = ',')

data = pd.read_csv('Starbucks/Data/Starbucks_Raw.csv',
                 encoding = 'euc-kr')