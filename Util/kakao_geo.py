import requests
import json
import environ
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_keys = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

HOST = "https://dapi.kakao.com"
URL = "/v2/local/search/address"
API_KEY = env_keys('KAKAO_RESTAPI_KEY')
headers = {"Authorization": f"KakaoAK {API_KEY}"}
params = {"query": "제주도 서귀포시 상예로 319",
          "analyze_type": "exact"}

r = requests.get(HOST+URL, headers=headers, params=params)

print(r.url)
print(r.status_code)

j = json.loads(r.text)
d = j['documents'][0]
print(d['x'], d['y'])
