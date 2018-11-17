

# from peewee import *
#
# psql_db = PostgresqlDatabase('my_database',  # Required by Peewee.
#     user='postgres',  # Will be passed directly to psycopg2.
#     password='share',  # Ditto.
#     host='localhost')
#
# class Old_building(Model):
#     STRCT_CD_NM = CharField(null = True)
#     HHLD_CNT = IntegerField(null = True)
#     BLD_NM = CharField(null = True)
#     ETC_PURPS = CharField(null = True)
#     TOTAREA = FloatField(null = True)
#     BC_RAT = FloatField(null = True)
#     SIGUNGU_CD = IntegerField(null = True)
#     MAIN_PURPS_CD_NM = CharField(null = True)
#     UGRND_FLR_CNT = IntegerField(null = True)
#     VL_RAT_ESTM_TOTAREA = FloatField(null = True)
#     BJDONG_CD = IntegerField(null = True)
#     NEW_PLAT_PLC = CharField(null = True)
#     ARCH_AREA = FloatField(null = True)
#     PLAT_PLC = CharField(null = True)
#     GRND_FLR_CNT = IntegerField(null = True)
#     USEAPR_DAY = CharField(null = True)
#     VL_RAT = FloatField(null = True)
#     PLAT_AREA = FloatField(null = True)
#     FMLY_CNT = IntegerField(null = True)
#
#
#
#     class Meta:
#         database = psql_db  # This model uses the "people.db" database.
#
#
#
#
# class User(Old_building):
#     username = CharField()
#
#
# psql_db.connect()
#
# psql_db.create_tables([Old_building])
#
# Old_building = Old_building()
#
#



import json
import pathlib
from pprint import pprint

# encoding = 'UTF8'
# ,encoding='latin-1'

with open("C:\\seoul_bigdata\\강남구.json") as data_file:
    tmp_data =json.load(data_file)
    # tmp_data = json.load(data_file)
    # tmp_data2 = tmp_data["Data"]

# with open("C:\\Users\\CHS\\Desktop\\노후건축2\\강동구.json") as data_file:
#     tmp_data = json.load(data_file)




### 데이터 컬럼갯수가 동일한지 확인

# cnt=0
# for j in range(len(tmp_data['Data'])):
#     list=[i for i in tmp_data['Data'][j]]
#     if len(list) == 19:
#         pprint(j)
#         pprint(len(list))
#         cnt=cnt+1
#         print(cnt)





### json파일 중복데이터가 있는지 확인하기

# liss=[]
# for i in range(len(tmp_data['Data'])):
#
#     liss.append(tmp_data['Data'][i].values())
#
# print(len(set(liss)))




### 점검
pprint(tmp_data['Description'])

# pprint(tmp_data[0]["rooms"])
# print(tmp_data["location"])
# print(tmp_data["rooms"])

# ls1 = [i for i in tmp_data['Data'][0]]

# print(ls1)
# print(len(ls1))





#강남구 데이터 DB저장
#
# list=[i for i in tmp_data['Description'].keys()]
#
# for j in range(len(tmp_data['Data'])):
#
#     ls1 = [i for i in tmp_data['Data'][j].keys()]
#     # ls1 = [i for i in tmp_data['Data'][j]]
#
#     for k in list:
#
#
#         if k in ls1:
#
#             pass
#
#
#         else:
#
#             tmp_data['Data'][j][str(k)] = None
#
#
#
#     Old_building.create(STRCT_CD_NM=tmp_data['Data'][j].get('STRCT_CD_NM'),
#                     HHLD_CNT=tmp_data['Data'][j].get('HHLD_CNT'),
#                     BLD_NM=tmp_data['Data'][j].get('BLD_NM'),
#                     ETC_PURPS=tmp_data['Data'][j].get('ETC_PURPS'),
#                     TOTAREA=tmp_data['Data'][j].get('TOTAREA'),
#                     BC_RAT=tmp_data['Data'][j].get('BC_RAT'),
#                     SIGUNGU_CD=tmp_data['Data'][j].get('SIGUNGU_CD'),
#                     MAIN_PURPS_CD_NM=tmp_data['Data'][j].get('MAIN_PURPS_CD_NM'),
#                     UGRND_FLR_CNT=tmp_data['Data'][j].get('UGRND_FLR_CNT'),
#                     VL_RAT_ESTM_TOTAREA=tmp_data['Data'][j].get('VL_RAT_ESTM_TOTAREA'),
#                     BJDONG_CD=tmp_data['Data'][j].get('BJDONG_CD'),
#                     NEW_PLAT_PLC=tmp_data['Data'][j].get('NEW_PLAT_PLC'),
#                     ARCH_AREA=tmp_data['Data'][j].get('ARCH_AREA'),
#                     PLAT_PLC=tmp_data['Data'][j].get('PLAT_PLC'),
#                     GRND_FLR_CNT=tmp_data['Data'][j].get('GRND_FLR_CNT'),
#                     USEAPR_DAY=tmp_data['Data'][j].get('USEAPR_DAY'),
#                     VL_RAT=tmp_data['Data'][j].get('VL_RAT'),
#                     PLAT_AREA=tmp_data['Data'][j].get('PLAT_AREA'),
#                     FMLY_CNT=tmp_data['Data'][j].get('FMLY_CNT'))
#
