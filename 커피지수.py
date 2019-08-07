


# 모듈 준비하기
import requests
import json
import pandas as pd
from pandas.io.json import json_normalize
import folium


## 스타벅스 매장 크롤링하기
# 참고 https://brunch.co.kr/@jk-lab/18

한라산_좌표 = (33.361666, 126.529166)

data = {
    'ins_lat': '33.4996213',  # 제주 시청의 좌표
    'ins_lng': '126.5311884',
    'p_sido_cd': '16',  # 01=서울시, 08=경기 ... 16=제주
    'p_gugun_cd': '',  # 세부지역 (지정하지 않으면 시/도 전체)
    'in_biz_cd': '',
    'set_date': '',
    'iend': '1000',
}


url = 'https://www.istarbucks.co.kr/store/getStore.do'
r = requests.post(url, data=data)
df = json_normalize(json.loads(r.text), 'list')

map_osm = folium.Map(location=한라산_좌표, zoom_start=10)
for ix, row in df.iterrows():
    location = (row['lat'], row['lot'])
    folium.Marker(location, popup=row['s_name']).add_to(map_osm)