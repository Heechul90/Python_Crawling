import pandas as pd
import numpy as np

raw_data = pd.read_csv('Starbucks/Data/Starbucks_Raw.csv',
                       index_col= 0)
data = raw_data.copy()

data.head()

City1 = []
City2 = []

for i in range(len(data['Address'])):
    City1.append(data['Address'][i].split()[0])
    City2.append(data['Address'][i].split()[1])
len(City1)
data['City1'] = City1
data['City2'] = City2

del data['Name']
del data['Lat']
del data['Log']

data['City2'].unique()
data.head()

City3 = []
City4 = []

for i in range(len(data)):
    if data['City2'][i] == '수원시':
        City3.append(data['Address'][i].split()[0])
        City4.append(' '.join(data['Address'][i].split()[1:3]))
    elif data['City2'][i] == '성남시':
        City3.append(data['Address'][i].split()[0])
        City4.append(' '.join(data['Address'][i].split()[1:3]))
    elif data['City2'][i] == '안양시':
        City3.append(data['Address'][i].split()[0])
        City4.append(' '.join(data['Address'][i].split()[1:3]))
    elif data['City2'][i] == '안산시':
        City3.append(data['Address'][i].split()[0])
        City4.append(' '.join(data['Address'][i].split()[1:3]))
    elif data['City2'][i] == '고양시':
        City3.append(data['Address'][i].split()[0])
        City4.append(' '.join(data['Address'][i].split()[1:3]))
    elif data['City2'][i] == '용인시':
        City3.append(data['Address'][i].split()[0])
        City4.append(' '.join(data['Address'][i].split()[1:3]))
    elif data['City2'][i] == '청주시':
        City3.append(data['Address'][i].split()[0])
        City4.append(' '.join(data['Address'][i].split()[1:3]))
    elif data['City2'][i] == '천안시':
        City3.append(data['Address'][i].split()[0])
        City4.append(' '.join(data['Address'][i].split()[1:3]))
    elif data['City2'][i] == '전주시':
        City3.append(data['Address'][i].split()[0])
        City4.append(' '.join(data['Address'][i].split()[1:3]))
    elif data['City2'][i] == '포항시':
        City3.append(data['Address'][i].split()[0])
        City4.append(' '.join(data['Address'][i].split()[1:3]))
    elif data['City2'][i] == '창원시':
        City3.append(data['Address'][i].split()[0])
        City4.append(' '.join(data['Address'][i].split()[1:3]))
    elif data['City2'][i] == '부천시':
        City3.append(data['Address'][i].split()[0])
        City4.append(' '.join(data['Address'][i].split()[1:3]))
    else:
        City3.append(data['Address'][i].split()[0])
        City4.append(data['Address'][i].split()[1])

data['광역시도'] = City3
data['시도'] = City4


data.head()
del data['City1']
del data['City2']