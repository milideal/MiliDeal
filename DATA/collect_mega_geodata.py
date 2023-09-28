import environ
import json
import os, sys
from Util.kakao_api import KakaoAPI

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
env_keys = environ.Env()
environ.Env.read_env('.env')
API_KEY = env_keys('KAKAO_RESTAPI_KEY')
k = KakaoAPI(API_KEY)

with open("./DATA/mega.json", 'r', encoding='utf-8') as data:
    data = json.load(data)
    result = []
    failed_list = []
    for location in list(data):
        title = location["name"]
        keyword = f"메가박스 {title}"
        print(keyword)
        docs = k.get_search_result_by_keyword(
            keyword=keyword,
            params={
                "category_group_code": "CT1"
                }
            )
        if docs is None:
            failed_list.append(location)
            continue
        result.append(docs)

with open(f'megabox_output.json', 'w',  encoding='utf-8') as f:
    json.dump(result, f, indent=2, ensure_ascii=False)

with open('megabox_failed.json', 'w',  encoding='utf-8') as f:
    json.dump(failed_list, f, indent=2, ensure_ascii=False)
