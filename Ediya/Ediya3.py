# 데이터 수정하기

# 함수준비
import pandas as pd
import numpy as np

# 데이터 불러오기
raw_data = pd.read_excel('Ediya/Data/이디야 2.xlsx',
                         encoding = 'euc-kr')
raw_data.head()
raw_data.loc[0]