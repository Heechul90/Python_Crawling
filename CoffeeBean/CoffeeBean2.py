### 커피빈 커피지수

# 모듈, 함수 준비하기
import pandas as pd
import numpy as np

# 데이터 불러오기
raw_data = pd.read_csv('CoffeeBean/CoffeeBean.csv',
                       index_col = 0)
data = raw_data.copy()
data.head()

# 필요없는 컬럼 지우기
del data['Name']
del data['Lat']
del data['Log']
data.head()

# 주소 나누기
City1 = []
City2 = []

for i in range(len(data)):

    City1.append(data['Address'][i].split()[0])
    City2.append(data['Address'][i].split()[1])

City1 = []
City2 = []

Starbucks = pd.DataFrame({'City1': City1,
                          'City2': City2})