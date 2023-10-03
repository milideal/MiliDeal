if __name__ == "__main__":
    import os, sys
    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
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

# 위치 좌표 기준 N meter 이내(원) slugs를 가져옴
# def get_slugs_with_geoWithin_search(coordinates:tuple, distance:int):
#     return list(mongo_client[env_keys('mongo_database')].stores.find({
#         "coord": {
#             "$geoWithin": {
#             "$centerSphere": [coordinates, distance / 6378160]
#                 }
#             }
#         }, {"_id": 0, "slug":1 })
#     )


def get_slugs_with_geoWithin_search(coordinates:list, distance:int):
    pipeline = []
    pipeline.append({"$match": {"coord": {
        "$geoWithin":{"$centerSphere": [coordinates, distance / 6378160]}}}})
    pipeline.append({"$group": {"_id" : "slugs","slugs": { "$push": "$slug" }}})
    pipeline.append({"$project": { "_id":0} })
    # 검색 결과가 없으면 list index out of range 가 나옴
    results = list(mongo_client[env_keys('mongo_database')].stores.aggregate(pipeline))
    if results:
        return results[0]["slugs"]
    return []

if __name__ == "__main__":
    searched_slugs = get_slugs_with_geoWithin_search([127.02927482937886, 37.5243205724172], 120)
    pprint(searched_slugs)