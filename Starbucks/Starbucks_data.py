### 스타벅스 매장 크롤링한 데이터 전처리

# 모듈 준비하기
import pandas as pd
import numpy as np

# 데이터 불러오기
raw_data = pd.read_csv('Starbucks/Starbucks.csv',
                       index_col = 0)
raw_data

data = raw_data.copy()
data.head()

data['City'] = []

for i in range(len(data)):
    data['City'][i].append(' '.join(data['Address'][i].split()[:2]))



