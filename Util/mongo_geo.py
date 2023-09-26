if __name__ == "__main__":
    import os, sys
    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
    from pprint import pprint

from MiliDeal.settings import env_keys 
from pymongo import MongoClient

# Django 실행하면 mongoDB Database Connect
mongo_client = MongoClient(
    host=env_keys('mongo_host'), 
    port=int(env_keys('mongo_port')), 
    username=env_keys('mongo_username'), 
    password=env_keys('mongo_password')
)

# 위치 좌표 기준 N meter 이내(원) 정보 가져옴
def get_stores_geoWithin_search(coordinates:list, meter:int):
    return list(mongo_client[env_keys('mongo_database')].stores.find({
        "coord": {
            "$geoWithin": {
            "$centerSphere": [coordinates, meter / 6378160]
                }
            }
        })
    )