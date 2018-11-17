
##노후주택 데이터에 위도,경도컬럼을 생성한 후 geocoding으로 위도,경도를 채우는 작업
##위도,경도값이 나오지않는 비정상 데이터는 0으로 채운 후 계속 진행.

from Db_Server import db_server
from Model import *
# from pprint import pprint
from Utill import geocoding_address
from time import sleep
import re

db_server.db_connect()

end= len(Old_Building.Old_building().select().tuples())

for j in range(1, 2770, 1):


    for i in Old_Building.Old_building.select().order_by(Old_Building.Old_building.id).paginate(j,100):


        if i.LONG == 0 and i.LAT==0:

            print(re.sub('번지','',i.LAND_LOC))

            geogeo = geocoding_address.reverse_geocoding(re.sub('번지','',i.LAND_LOC))
            print(geogeo)
            try:
                long = float(geogeo["documents"][0]['address']['x'])
                lat = float(geogeo["documents"][0]['address']['y'])
                # sleep(random.uniform(0, 1))

                q = Old_Building.Old_building.update(LONG= long , LAT= lat).where(Old_Building.Old_building.id == i)
                q.execute()

            except:
                q = Old_Building.Old_building.update(LONG=0, LAT=0).where(Old_Building.Old_building.id == i)
                q.execute()
                print('$$$$$$$$$$$$$$ abnormal data occured!!$$$$$$$$$$$$$$$$')




        else:
            pass

    # j = j + 1




# for i in Old_Building.Old_building.select().order_by(Old_Building.Old_building.id).paginate(1,10):
#
# print(i.LAND_LOC)

