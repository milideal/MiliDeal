import requests
import environ
import os
import json


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_keys = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

HOST = "https://openapi.mnd.go.kr/"
KEY = env_keys('OPENAPI_KEY')
TYPE = "/json"

# 국방부_군 휴양시설 운영 정보 목록
vacation_facility = HOST + KEY + TYPE + "/DS_WHLAM_WLFR_VCTNINSTLT/1/14/"

# 국방부_병사 할인 혜택 정보
discount_info = HOST + KEY + TYPE + "/DS_MND_ENLSTMN_DCNT_BEF_INF/1/81/"

vacation_json = json.loads(requests.get(vacation_facility).content)
discount_json = json.loads(requests.get(discount_info).content)

with open("stores.json", 'w', encoding='utf-8') as f:
    f.write(
        json.dumps(
            vacation_json['DS_WHLAM_WLFR_VCTNINSTLT']['row'] +
            discount_json['DS_MND_ENLSTMN_DCNT_BEF_INF']['row'],
            indent=2, ensure_ascii=False
        ).replace("'", '"')
    )
