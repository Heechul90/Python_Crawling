### 빽다방 매장 크롤링하기

# 모듈 준비하기
from selenium import webdriver
import bs4
import time


# 참고 https://brunch.co.kr/@jk-lab/18


chromedriver_dir = 'D:\Heechul\Python_Crawling/chromedriver.exe'
driver = webdriver.Chrome(chromedriver_dir)
time.sleep(3)

driver.get('http://www.theborn.co.kr/store/domestic-store/')
time.sleep(3)

select = driver.find_element_by_xpath("//*[@id='select_brand']/option[8]")
select.click()
time.sleep(3)

name = []
address = []

for i in range(61):

    x1 = '//*[@id="pagination"]/li['
    x2 = str(i+1)
    x3 = ']'

    page = driver.find_element_by_xpath(x1 + x2 + x3)
    page.click()
    time.sleep(3)



    source = driver.page_source
    bs = bs4.BeautifulSoup(source, 'lxml')
    entire = bs.find('div', id='store_list')
    ul_list = entire.findAll('ul')
    ul_list[0].find_all('li')[2]

    for k in range(len(ul_list)):

        name.append(ul_list[k].find_all('li')[2])

        address.append(ul_list[k].find_all('li')[3])


