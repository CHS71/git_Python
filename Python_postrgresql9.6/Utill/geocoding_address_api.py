# -*- coding: utf-8 -*-
import requests
import json
import pandas as pd


df_origin = pd.DataFrame(columns=['address', 'lat', 'lng'])
new_candidates = ["서울특별시 서초구 신반포로 190", "서울특별시 서초구 동광로43길 51-13"]
apikey = 'bd081f3ec46252d2335952946cd5c2e8'  # 예시입니다. 본인의 apikey를 string 내부에 넣어아 합니다.

for address in new_candidates:
    resp = requests.get('https://apis.daum.net/local/geo/addr2coord?apikey={apikey}&q={address}&output=json'.format(
        apikey=apikey,
        address=address))
    print(json.loads(resp.text))
    lat = json.loads(resp.text)['channel']['item'][0]['lat']
    lng = json.loads(resp.text)['channel']['item'][0]['lng']
    # print(lat)
    # df_origin.loc[len(df_origin)] = [address, lng, lat]

# json.loads(resp.text)