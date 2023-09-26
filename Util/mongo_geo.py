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
        "$geoWithin":{"$centerSphere": [coordinates, 96 / 6378160]}}}})
    pipeline.append({"$group": {"_id" : "slugs","slugs": { "$push": "$slug" }}})
    pipeline.append({"$project": { "_id":0} })
    return list(mongo_client[env_keys('mongo_database')].stores.aggregate(pipeline))[0]["slugs"]

if __name__ == "__main__":
    searched_slugs = get_slugs([127.7816977, 37.9296045], 120)
    pprint(searched_slugs)