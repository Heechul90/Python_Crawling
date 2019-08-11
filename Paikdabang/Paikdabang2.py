### 빽다방 커피지수

import pandas as pd
import numpy as np


# 데이터 불러오기
raw_data = pd.read_csv('Paikdabang/Data/Paikdabang_Raw.csv',
                       encoding = 'euc-kr')
data = raw_data.copy()
data.rename(columns = {'상호명': 'Name',
                       '시도명': 'City1',
                       '시군구명': 'City2',
                       '주소': 'Address',
                       'Unnamed: 4': '입점수'},
            inplace = True)
data.head()

# 주소 분리하기
City3 = []
City4 = []

for i in range(len(data['City2'])):
    if len(data['City2'][i].split()) == 2:
        City3.append(data['Address'][i].split()[0])
        City4.append(data['City2'][i].split()[1])
    else:
        City3.append(data['Address'][i].split()[0])
        City4.append(data['City2'][i].split()[0])

data['광역시도'] = City3
data['시도'] = City4
del data['City1']
del data['City2']
data.head()

# 광역시도 값 확인하고 수정하기
data['광역시도'].unique()

# 시도 값 확인하고 수정하기
data['시도'].unique()


data[data['시도'].isin(['부천시'])]
data['시도'][0] = '원미구'
data['시도'][1] = '원미구'
data['시도'][5] = '원미구'
data['시도'][8] = '원미구'
data['시도'][14] = '원미구'
data['시도'][31] = '원미구'
data['시도'][32] = '소사구'
data['시도'][34] = '소사구'
data['시도'][56] = '소사구'
data['시도'][63] = '소사구'
data['시도'][66] = '오정구'
data['시도'][69] = '오정구'
data['시도'][82] = '오정구'
data['시도'][153] = '오정구'

data['시도'].unique()

# 입점수 컬럼 추가

data.to_csv("Paikdabang/Data/Paikdabang1.csv",
                  encoding='euc-kr',
                  sep=',')

# 피봇테이블 만들기
Paikdabang = pd.pivot_table(data,
                            values = '입점수',
                            index = ['광역시도', '시도'],
                            aggfunc = 'sum')
Paikdabang.reset_index(inplace = True)
Paikdabang.head()
Paikdabang
Paikdabang.to_csv('Paikdabang/Data/Paikdabang2.csv',
                  encoding = 'euc-kr',
                  sep = ',')

Paikdabang = pd.read_csv('Paikdabang/Data/Paikdabang2.csv',
                  encoding = 'euc-kr')

## 몇몇 구를 가진 시를 구별로 나누고 ID추가하기
si_name = [None] * len(Paikdabang)

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

for n in Paikdabang.index:
    if Paikdabang['광역시도'][n][-3:] not in ['광역시', '특별시', '자치시']:
        if Paikdabang['시도'][n][:-1] == '고성' and Paikdabang['광역시도'][n] == '강원도':
            si_name[n] = '고성(강원)'
        elif Paikdabang['시도'][n][:-1] == '고성' and Paikdabang['광역시도'][n] == '경상남도':
            si_name[n] = '고성(경남)'
        else:
            si_name[n] = Paikdabang['시도'][n][:-1]

        for keys, values in tmp_gu_dict.items():
            if Paikdabang['시도'][n] in values:
                if len(Paikdabang['시도'][n]) == 2:
                    si_name[n] = keys + ' ' + Paikdabang['시도'][n]
                elif Paikdabang['시도'][n] in ['마산합포구', '마산회원구']:
                    si_name[n] = keys + ' ' + Paikdabang['시도'][n][2:-1]
                else:
                    si_name[n] = keys + ' ' + Paikdabang['시도'][n][:-1]

    elif Paikdabang['광역시도'][n] == '세종특별자치시':
        si_name[n] = '세종'

    else:
        if len(Paikdabang['시도'][n]) == 2:
            si_name[n] = Paikdabang['광역시도'][n][:2] + ' ' + Paikdabang['시도'][n]
        else:
            si_name[n] = Paikdabang['광역시도'][n][:2] + ' ' + Paikdabang['시도'][n][:-1]

Paikdabang['ID'] = si_name
Paikdabang
Paikdabang.to_csv("Paikdabang/Data/Paikdabang3.csv",
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

set(draw_korea['ID'].unique()) - set(Paikdabang['ID'].unique())
set(Paikdabang['ID'].unique()) - set(draw_korea['ID'].unique())

# CoffeeBean과 draw_korea 합치기
Paikdabang = pd.merge(Paikdabang, draw_korea, how='right', on=['ID'])
Paikdabang = Paikdabang.fillna(0)
Paikdabang.head()

Paikdabang.to_csv("Paikdabang/Data/Paikdabang4.csv",
                  encoding='euc-kr',
                  sep=',')

mapdata = Paikdabang.pivot_table(index='y', columns='x', values='입점수')
masked_mapdata = np.ma.masked_where(np.isnan(mapdata), mapdata)
mapdata

# 그래프 그리기
# 함수 준비
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

drawKorea('입점수', Paikdabang, 'Blues')