import environ
import json
from Util.kakao_api import KakaoAPI

env_keys = environ.Env()
environ.Env.read_env('.env')
API_KEY = env_keys('KAKAO_RESTAPI_KEY')
k = KakaoAPI(API_KEY)

with open("./DATA/vips.json", 'r', encoding='utf-8') as data:
    data = json.load(data)
    result = []
    failed_list = []
    for location in list(data):
        title = location["JUMNAME"]
        keyword = f"빕스 {title}"
        print(keyword)
        docs = k.get_search_result_by_keyword(
            keyword=keyword,
            # params={
            #     "category_group_code": "CT1"
            #     }
            )
        if docs is None:
            failed_list.append(location)
            continue
        result.append(docs)

with open(f'vips_output.json', 'w',  encoding='utf-8') as f:
    json.dump(result, f, indent=2, ensure_ascii=False)

with open('vips_failed.json', 'w',  encoding='utf-8') as f:
    json.dump(failed_list, f, indent=2, ensure_ascii=False)
