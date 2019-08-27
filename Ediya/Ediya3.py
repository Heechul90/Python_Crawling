### 이디야 커피지수

import pandas as pd
import numpy as np

# 데이터 불러오기
raw_data = pd.read_csv('Ediya/Data/Ediya_Raw.csv',
                       encoding = 'euc-kr',
                       index_col = 0)

data = raw_data.copy()
data.head()

# 주소 분리하기
data['Address'][0].split()[0]
data['Address'][0].split()[1]

City1 = []
City2 = []

for i in range(len(data['Address'])):

    City1.append(data['Address'][i].split()[0])
    City2.append(data['Address'][i].split()[1])

data['City1'] = City1
data['City2'] = City2

City3 = []
City4 = []

for i in range(len(data)):
    if data['City2'][i] == '수원시':
        City3.append(data['Address'][i].split()[0])
        City4.append(data['Address'][i].split()[2])
    elif data['City2'][i] == '성남시':
        City3.append(data['Address'][i].split()[0])
        City4.append(data['Address'][i].split()[2])
    elif data['City2'][i] == '안양시':
        City3.append(data['Address'][i].split()[0])
        City4.append(data['Address'][i].split()[2])
    elif data['City2'][i] == '안산시':
        City3.append(data['Address'][i].split()[0])
        City4.append(data['Address'][i].split()[2])
    elif data['City2'][i] == '고양시':
        City3.append(data['Address'][i].split()[0])
        City4.append(data['Address'][i].split()[2])
    elif data['City2'][i] == '용인시':
        City3.append(data['Address'][i].split()[0])
        City4.append(data['Address'][i].split()[2])
    elif data['City2'][i] == '청주시':
        City3.append(data['Address'][i].split()[0])
        City4.append(data['Address'][i].split()[2])
    elif data['City2'][i] == '천안시':
        City3.append(data['Address'][i].split()[0])
        City4.append(data['Address'][i].split()[2])
    elif data['City2'][i] == '전주시':
        City3.append(data['Address'][i].split()[0])
        City4.append(data['Address'][i].split()[2])
    elif data['City2'][i] == '포항시':
        City3.append(data['Address'][i].split()[0])
        City4.append(data['Address'][i].split()[2])
    elif data['City2'][i] == '창원시':
        City3.append(data['Address'][i].split()[0])
        City4.append(data['Address'][i].split()[2])
    elif data['City2'][i] == '부천시':
        City3.append(data['Address'][i].split()[0])
        City4.append(data['Address'][i].split()[2])
    else:
        City3.append(data['Address'][i].split()[0])
        City4.append(data['Address'][i].split()[1])

data['광역시도'] = City3
data['시도'] = City4
del data['City1']
del data['City2']
data.head()

# 광역시도 값 확인하고 수정하기
data['광역시도'].unique()

data[data['광역시도'].isin(['/충남'])]
data['광역시도'][2084] = '충청남도'

data[data['광역시도'].isin(['북'])]
data['광역시도'][2361] = '경상북도'

for i in range(len(data['광역시도'])):
    if data['광역시도'][i] == '서울':
        data['광역시도'][i] = '서울특별시'

    if data['광역시도'][i] == '부산':
        data['광역시도'][i] = '부산광역시'

    if data['광역시도'][i] == '대구':
        data['광역시도'][i] = '대구광역시'

    if data['광역시도'][i] == '인천':
        data['광역시도'][i] = '인천광역시'

    if data['광역시도'][i] == '광주':
        data['광역시도'][i] = '광주광역시'

    if data['광역시도'][i] == '대전':
        data['광역시도'][i] = '대전광역시'

    if data['광역시도'][i] == '울산':
        data['광역시도'][i] = '울산광역시'

    if data['광역시도'][i] == '경기':
        data['광역시도'][i] = '경기도'

    if data['광역시도'][i] == '강원':
        data['광역시도'][i] = '강원도'

    if data['광역시도'][i] == '경남':
        data['광역시도'][i] = '경상남도'

    if data['광역시도'][i] == '충북':
        data['광역시도'][i] = '충청북도'

    if data['광역시도'][i] == '충남':
        data['광역시도'][i] = '충청남도'

    if data['광역시도'][i] == '전북':
        data['광역시도'][i] = '전라북도'

    if data['광역시도'][i] == '전남':
        data['광역시도'][i] = '전라남도'

    if data['광역시도'][i] == '경북':
        data['광역시도'][i] = '경상북도'

    if data['광역시도'][i] == '전남':
        data['광역시도'][i] = '전라남도'

data['광역시도'].unique()

# 시도 값 확인하고 수정하기
data['시도'].unique()

for i in range(len(data['광역시도'])):
    if data['광역시도'][i] == '세종특별자치시':
        data['시도'][i] = '세종특별자치시'

data['시도'].unique()

data[data['시도'].isin(['범안로'])]
data['시도'][1436] = '소사구'
data['시도'][1464] = '소사구'

data[data['시도'].isin(['성주로'])]
data['시도'][1437] = '소사구'

data[data['시도'].isin(['송내대로'])]
data['시도'][1438] = '원미구'
data['시도'][1476] = '소사구'

data[data['시도'].isin(['옥산로'])]
data['시도'][1439] = '원미구'

data[data['시도'].isin(['소사로'])]
data['시도'][1440] = '오정구'
data['시도'][1455] = '소사구'
data['시도'][1456] = '소사구'

data[data['시도'].isin(['양지로67번길'])]
data['시도'][1441] = '소사구'

data[data['시도'].isin(['부흥로'])]
data['시도'][1443] = '원미구'
data['시도'][1452] = '원미구'

data[data['시도'].isin(['부일로'])]
data['시도'][1444] = '원미구'
data['시도'][1480] = '원미구'

data[data['시도'].isin(['상동로117번길'])]
data['시도'][1446] = '오정구'

data[data['시도'].isin(['경인로'])]
data['시도'][1453] = '소사구'
data['시도'][1479] = '소사구'

data[data['시도'].isin(['소사동로'])]
data['시도'][1454] = '소사구'

data[data['시도'].isin(['상일로94번길'])]
data['시도'][1457] = '원미구'

data[data['시도'].isin(['부천로'])]
data['시도'][1459] = '원미구'
data['시도'][1465] = '원미구'

data[data['시도'].isin(['수도로'])]
data['시도'][1460] = '오정구'

data[data['시도'].isin(['양지로184번길'])]
data['시도'][1463] = '소사구'

data[data['시도'].isin(['원미로124번길'])]
data['시도'][1466] = '원미구'

data[data['시도'].isin(['원종로'])]
data['시도'][1467] = '오정구'

data[data['시도'].isin(['중동로'])]
data['시도'][1470] = '소사구'

data[data['시도'].isin(['장말로'])]
data['시도'][1473] = '원미구'

data[data['시도'].isin(['호현로489번길'])]
data['시도'][1475] = '소사구'

data[data['시도'].isin(['상일로122번길'])]
data['시도'][1477] = '원미구'

data[data['시도'].isin(['지봉로'])]
data['시도'][1433] = '원미구'

data['시도'].unique()

# 입점수 컬럼 추가
data['입점수'] = 1
data.head()

data.to_csv("Ediya/Data/Ediya1.csv",
            encoding = 'euc-kr',
            sep = ',')

# 피봇테이블 만들기
Ediya = pd.pivot_table(data,
                       values = '입점수',
                       index = ['광역시도', '시도'],
                       aggfunc = 'sum')

Ediya.reset_index(inplace = True)
Ediya.head()
Ediya
Ediya.to_csv("Ediya/Data/Ediya2.csv",
             encoding='euc-kr',
             sep=',')

# 몇몇 구를 가진 시를 구별로 나누고 ID 추가하기
si_name = [None] * len(Ediya)

tmp_gu_dict = {'수원':['장안구', '권선구', '팔달구', '영통구'],
                       '성남':['수정구', '중원구', '분당구'],
                       '안양':['만안구', '동안구'],
                       '안산':['상록구', '단원구'],
                       '고양':['덕양구', '일산동구', '일산서구'],
                       '용인':['처인구', '기흥구', '수지구'],
                       '청주':['상당구', '서원구', '흥덕구', '청원구'],
                       '천안':['동남구', '서북구'],
                       '전주':['완산구', '덕진구'],
                       '포항':['남구', '북구'],
                       '창원':['의창구', '성산구', '진해구', '마산합포구', '마산회원구'],
                       '부천':['오정구', '원미구', '소사구']}

for n in Ediya.index:
    if Ediya['광역시도'][n][-3:] not in ['광역시', '특별시', '자치시']:
        if Ediya['시도'][n][:-1] == '고성' and Ediya['광역시도'][n] == '강원도':
            si_name[n] = '고성(강원)'
        elif Ediya['시도'][n][:-1] == '고성' and Ediya['광역시도'][n] == '경상남도':
            si_name[n] = '고성(경남)'
        else:
            si_name[n] = Ediya['시도'][n][:-1]

        for keys, values in tmp_gu_dict.items():
            if Ediya['시도'][n] in values:
                if len(Ediya['시도'][n]) == 2:
                    si_name[n] = keys + ' ' + Ediya['시도'][n]
                elif Ediya['시도'][n] in ['마산합포구', '마산회원구']:
                    si_name[n] = keys + ' ' + Ediya['시도'][n][2:-1]
                else:
                    si_name[n] = keys + ' ' + Ediya['시도'][n][:-1]

    elif Ediya['광역시도'][n] == '세종특별자치시':
        si_name[n] = '세종'

    else:
        if len(Ediya['시도'][n]) == 2:
            si_name[n] = Ediya['광역시도'][n][:2] + ' ' + Ediya['시도'][n]
        else:
            si_name[n] = Ediya['광역시도'][n][:2] + ' ' + Ediya['시도'][n][:-1]

Ediya['ID'] = si_name
Ediya
Ediya.to_csv("Ediya/Data/Ediya3.csv",
             encoding='euc-kr',
             sep=',')

# 엑셀로된 지도 파일 불러오기
draw_korea_raw = pd.read_excel('05. draw_korea_raw.xlsx', encoding = 'euc-kr')
draw_korea_raw

# stack으로 풀고 index로 재설정
draw_korea_raw_stacked = pd.DataFrame(draw_korea_raw.stack())
draw_korea_raw_stacked.reset_index(inplace = True)
draw_korea_raw_stacked.rename(columns = {'level_0': 'y',
                                         'level_1': 'x',
                                         0: 'ID'},
                              inplace = True)
draw_korea_raw_stacked
draw_korea = draw_korea_raw_stacked
draw_korea

# 경계선 설정하기
BORDER_LINES = [
    [(5, 1), (5,2), (7,2), (7,3), (11,3), (11,0)],                      # 인천
    [(5,4), (5,5), (2,5), (2,7), (4,7), (4,9), (7,9),
     (7,7), (9,7), (9,5), (10,5), (10,4), (5,4)],                       # 서울
    [(1,7), (1,8), (3,8), (3,10), (10,10), (10,7),
     (12,7), (12,6), (11,6), (11,5), (12, 5), (12,4),
     (11,4), (11,3)],                                                    # 경기도
    [(8,10), (8,11), (6,11), (6,12)],                                    # 강원도
    [(12,5), (13,5), (13,4), (14,4), (14,5), (15,5),
     (15,4), (16,4), (16,2)],                                            # 충청북도
    [(16,4), (17,4), (17,5), (16,5), (16,6), (19,6),
     (19,5), (20,5), (20,4), (21,4), (21,3), (19,3), (19,1)],            # 전라북도
    [(13,5), (13,6), (16,6)],                                            # 대전시
    [(13,5), (14,5)],                                                    # 세종시
    [(21,2), (21,3), (22,3), (22,4), (24,4), (24,2), (21,2)],            # 광주
    [(20,5), (21,5), (21,6), (23,6)],                                    # 전라남도
    [(10,8), (12,8), (12,9), (14,9), (14,8), (16,8), (16,6)],            # 충청북도
    [(14,9), (14,11), (14,12), (13,12), (13,13)],                        # 경상북도
    [(15,8), (17,8), (17,10), (16,10), (16,11), (14,11)],                # 대구
    [(17,9), (18,9), (18,8), (19,8), (19,9), (20,9), (20,10), (21,10)],  # 부산
    [(16,11), (16,13)],                                                  # 울산
#     [(9,14), (9,15)],
    [(27,5), (27,6), (25,6)],
]

set(draw_korea['ID'].unique()) - set(Ediya['ID'].unique())
set(Ediya['ID'].unique()) - set(draw_korea['ID'].unique())

# CoffeeBean과 draw_korea 합치기
Ediya = pd.merge(Ediya, draw_korea, how='right', on=['ID'])
Ediya = Ediya.fillna(0)
Ediya.head()

Ediya.to_csv("Ediya/Data/Ediya4.csv",
             encoding = 'euc-kr',
             sep = ',')

mapdata = Ediya.pivot_table(index='y', columns='x', values='입점수')
masked_mapdata = np.ma.masked_where(np.isnan(mapdata), mapdata)
mapdata

# 그래프 그리기
# 함수 준비
import pandas as pd
import numpy as np

import platform
import matplotlib.pyplot as plt

# 한글 사용하기
path = "c:/Windows/Fonts/malgun.ttf"
from matplotlib import font_manager, rc

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~')

plt.rcParams['axes.unicode_minus'] = False


# 지도 함수 만들기
def drawKorea(targetData, blockedMap, cmapname):
    gamma = 0.75

    whitelabelmin = (max(blockedMap[targetData]) -
                     min(blockedMap[targetData])) * 0.25 + \
                     min(blockedMap[targetData])

    datalabel = targetData

    vmin = min(blockedMap[targetData])
    vmax = max(blockedMap[targetData])

    mapdata = blockedMap.pivot_table(index='y', columns='x', values=targetData)
    masked_mapdata = np.ma.masked_where(np.isnan(mapdata), mapdata)

    plt.figure(figsize=(9, 11))
    plt.pcolor(masked_mapdata, vmin=vmin, vmax=vmax, cmap=cmapname,
               edgecolor='#aaaaaa', linewidth=0.5)

    # 지역 이름 표시
    for idx, row in blockedMap.iterrows():
        # 광역시는 구 이름이 겹치는 경우가 많아서 시단위 이름도 같이 표시한다.
        # (중구, 서구)
        if len(row['ID'].split()) == 2:
            dispname = '{}\n{}'.format(row['ID'].split()[0], row['ID'].split()[1])
        elif row['ID'][:2] == '고성':
            dispname = '고성'
        else:
            dispname = row['ID']

        # 서대문구, 서귀포시 같이 이름이 3자 이상인 경우에 작은 글자로 표시한다.
        if len(dispname.splitlines()[-1]) >= 3:
            fontsize, linespacing = 10.0, 1.1
        else:
            fontsize, linespacing = 11, 1.

        annocolor = 'white' if row[targetData] > whitelabelmin else 'black'
        plt.annotate(dispname, (row['x'] + 0.5, row['y'] + 0.5), weight='bold',
                     fontsize=fontsize, ha='center', va='center', color=annocolor,
                     linespacing=linespacing)

    # 시도 경계를 그린다.
    for path in BORDER_LINES:
        ys, xs = zip(*path)
        plt.plot(xs, ys, c='black', lw=2)

    plt.gca().invert_yaxis()

    plt.axis('off')

    cb = plt.colorbar(shrink=.1, aspect=10)
    cb.set_label(datalabel)

    plt.tight_layout()
    plt.show()

# 지도 그리기

drawKorea('입점수', Ediya, 'Blues')