import bs4
import time
import pandas as pd
from selenium import webdriver

# 참고 https://brunch.co.kr/@jk-lab/18

chromedriver_dir = 'D:\Heechul\Python_Crawling/chromedriver.exe'
driver = webdriver.Chrome(chromedriver_dir)
driver.get('https://www.bskorea.or.kr/bible/korbibReadpage.php?version=GAE&book=gen&chap=1&sec=1&cVersion=&fontSize=15px&fontWeight=normal')

Bible_content = []
Chapter = []
Part = []

for i in range(50):

    page_num = i + 1
    driver.get('https://www.bskorea.or.kr/bible/korbibReadpage.php?version=GAE&book=gen&chap='+str(page_num)+'&sec=1&cVersion=&fontSize=15px&fontWeight=normal')
    time.sleep(3)

    source = driver.page_source
    bs = bs4.BeautifulSoup(source, 'lxml')
    entire = bs.find('div', class_='bible_read')
    content = entire.find_all('span')

    for k in range(0, len(content), 2):

        Chapter.append(i + 1)
        Bible_content.append(' '.join(content[k].get_text().split()[1:]))

    for j in range(0, len(content) // 2):
        Part.append(j + 1)

    print(i)

len(Chapter)
len(Part)
Bible_content[-1]
len(Bible_content)


Bible = pd.DataFrame({'장': Chapter,
                      '절': Part,
                      '말씀': Bible_content})
len(Bible)
Bible.columns


Bible.to_csv('Bible/Data/Bible_Raw.csv',
             encoding = 'euc-kr',
             sep = ',')

data = pd.read_csv('Bible/Data/Bible_Raw.csv',
                 encoding = 'euc-kr')

