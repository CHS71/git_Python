



# # 노후주택 데이터 json 형태로 불러오기



###################################


from peewee import *

psql_db = PostgresqlDatabase('my_database',  # Required by Peewee.
                             user='postgres',  # Will be passed directly to psycopg2.
                             password='share',  # Ditto.
                             host='localhost')


class Buildings(Model):
    STRCT_CD_NM = CharField(null=True)
    HHLD_CNT = IntegerField(null=True)
    BLD_NM = CharField(null=True)
    ETC_PURPS = CharField(null=True)
    TOTAREA = FloatField(null=True)
    BC_RAT = FloatField(null=True)
    SIGUNGU_CD = IntegerField(null=True)
    MAIN_PURPS_CD_NM = CharField(null=True)
    UGRND_FLR_CNT = IntegerField(null=True)
    VL_RAT_ESTM_TOTAREA = FloatField(null=True)
    BJDONG_CD = IntegerField(null=True)
    NEW_PLAT_PLC = CharField(null=True)
    ARCH_AREA = FloatField(null=True)
    PLAT_PLC = CharField(null=True)
    GRND_FLR_CNT = IntegerField(null=True)
    USEAPR_DAY = CharField(null=True)
    VL_RAT = FloatField(null=True)
    PLAT_AREA = FloatField(null=True)
    FMLY_CNT = IntegerField(null=True)

    class Meta:
        database = psql_db  # This model uses the "people.db" database.


class User(Buildings):
    username = CharField()


psql_db.connect()

psql_db.create_tables([Buildings])





######
import os
import json

## json파일만 파일명 불러오기
path = 'C:\\yang\\buildings'
gu_lst = []
for file_or_dir in os.listdir(path):  # 입력한 경로의 파일과 폴더 목록 리스트를 loop문 돌림
    #print('$',file_or_dir)

    abs_path = os.path.abspath(file_or_dir)
    s = os.path.splitext(abs_path)

    if '.json' in os.path.split(s[1]):
        s=  os.path.split(s[0])
        gu_lst.append((s[1]))

# print(gu_lst)
# print(len(gu_lst))
# print(len(set(gu_lst)))



## 경로내 모든 json파일 불러와서 db에 저장
# GU = []
for i in  gu_lst:

    with open("C:\\yang\\buildings\\"+ i +".json") as data_file:
        tmp_data = json.load(data_file)


    # print(len(tmp_data['Data']))
print(tmp_data["Description"])

    # ls1 = [i for i in tmp_data['Data'][0]]
    #
    # print(ls1)
    # print(len(ls1))

    #
    # list = [i for i in tmp_data['Description'].keys()]
    #
    # for j in range(len(tmp_data['Data'])):
    #
    #     # ls1 = [i for i in tmp_data['Data'][j]]
    #     ls1 = [i for i in tmp_data['Data'][j].keys()]
    #
    #     for k in list:
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
    #             Buildings.create(STRCT_CD_NM=tmp_data['Data'][j].get('STRCT_CD_NM'),
    #                         HHLD_CNT=tmp_data['Data'][j].get('HHLD_CNT'),
    #                         BLD_NM=tmp_data['Data'][j].get('BLD_NM'),
    #                         ETC_PURPS=tmp_data['Data'][j].get('ETC_PURPS'),
    #                         TOTAREA=tmp_data['Data'][j].get('TOTAREA'),
    #                         BC_RAT=tmp_data['Data'][j].get('BC_RAT'),
    #                         SIGUNGU_CD=tmp_data['Data'][j].get('SIGUNGU_CD'),
    #                         MAIN_PURPS_CD_NM=tmp_data['Data'][j].get('MAIN_PURPS_CD_NM'),
    #                         UGRND_FLR_CNT=tmp_data['Data'][j].get('UGRND_FLR_CNT'),
    #                         VL_RAT_ESTM_TOTAREA=tmp_data['Data'][j].get('VL_RAT_ESTM_TOTAREA'),
    #                         BJDONG_CD=tmp_data['Data'][j].get('BJDONG_CD'),
    #                         NEW_PLAT_PLC=tmp_data['Data'][j].get('NEW_PLAT_PLC'),
    #                         ARCH_AREA=tmp_data['Data'][j].get('ARCH_AREA'),
    #                         PLAT_PLC=tmp_data['Data'][j].get('PLAT_PLC'),
    #                         GRND_FLR_CNT=tmp_data['Data'][j].get('GRND_FLR_CNT'),
    #                         USEAPR_DAY=tmp_data['Data'][j].get('USEAPR_DAY'),
    #                         VL_RAT=tmp_data['Data'][j].get('VL_RAT'),
    #                         PLAT_AREA=tmp_data['Data'][j].get('PLAT_AREA'),
    #                         FMLY_CNT=tmp_data['Data'][j].get('FMLY_CNT'))






# print(len(GU))

#pprint(tmp_data)

#for h in tmp_data['Data']:
 #   print(h['ARCH_AREA'])
# print(result_df) '''







