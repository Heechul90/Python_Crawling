import pandas as pd
import numpy as np


data_raw = pd.read_excel('Ediya/Data/이디야_원본.xlsx')

data = data_raw.copy()
del data['시도명']
del data['시군구명']
data.columns

data['Unnamed: 3']
data = data['Unnamed: 2']
data

len(data[1].split('///'))
len(data)
type(data)
data.notnull()
data = data.fillna('')



Address = []

for i in range(1, 241):

    len_data = len(data[i].split('///'))
    sep_data = data[i].split('///')

    for k in range(len_data):
        Address.append(sep_data[k])
        # City1.append(sep_data[k].split()[0])

len(Address)
Ediya = pd.DataFrame(Address,
                     columns = ['Address'])

Ediya[Ediya['Address'].isin(['x'])]
len(Ediya)

Ediya = Ediya.drop([905])
Ediya = Ediya.drop([1120])
Ediya = Ediya.drop([1981])
Ediya = Ediya.drop([2126])
Ediya = Ediya.drop([2133])
Ediya = Ediya.drop([2285])
Ediya = Ediya.drop([2288])
Ediya = Ediya.drop([2296])
Ediya = Ediya.drop([2301])
Ediya = Ediya.drop([2379])
Ediya = Ediya.drop([2381])
Ediya = Ediya.drop([2396])
Ediya = Ediya.drop([2525])
Ediya = Ediya.drop([2532])
len(Ediya)

Ediya[Ediya['Address'].isin([''])]

Ediya = Ediya.drop([673])
Ediya = Ediya.drop([888])
Ediya = Ediya.drop([942])
Ediya = Ediya.drop([1121])
Ediya = Ediya.drop([1175])
Ediya = Ediya.drop([1255])
Ediya = Ediya.drop([1270])
Ediya = Ediya.drop([1280])
Ediya = Ediya.drop([1923])
Ediya = Ediya.drop([2010])
Ediya = Ediya.drop([2076])
Ediya = Ediya.drop([2146])
Ediya = Ediya.drop([2239])
Ediya = Ediya.drop([2302])
Ediya = Ediya.drop([2397])
Ediya = Ediya.drop([2538])
len(Ediya)
Ediya

Ediya.to_csv('Ediya/Data/Ediya_Raw.csv',
             encoding = 'euc-kr',
             sep = ',')
Ediya = pd.read_csv('Ediya/Data/Ediya_Raw.csv',
                    encoding = 'euc-kr')
del Ediya['Unnamed: 0']
Ediya.to_csv('Ediya/Data/Ediya_Raw.csv',
             encoding = 'euc-kr',
             sep = ',')
Ediya = pd.read_csv('Ediya/Data/Ediya_Raw.csv',
                    encoding = 'euc-kr',
                    index_col = 0)