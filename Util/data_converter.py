import json
# store model 에 맞도록 원본 json 을 변환 시키는 코드.

# DATA 폴더 내에 있는 점포 들의 종류
# store_name = ["blue", "cgv", "lotte", "megabox", "vips"]
stores = {"blue": "etc", "cgv": "theater", "lotte": "theater", "megabox": "theater", "vips": "restau"}

for s in stores.keys():
    with open(f'../DATA/{s}_output.json', 'r', encoding='utf-8') as data:
        data = json.load(data)
        converted_data = []
        for item in list(data):
            converted_item = {
                "address": item["road_address_name"],
                "coordx": item["x"],
                "coordy": item["y"],
                "tel": item["phone"],
                "name": item["place_name"],
                "storeType": stores[s]
            }
            converted_data.append(converted_item)
        with open(f'../DATA/converted/{s}_converted.json', "w", encoding="utf-8") as output_file:
            json.dump(converted_data, output_file, ensure_ascii=False, indent=2)

"""
  {
    "address_name": "제주특별자치도 제주시 노형동 2511-5",
    "category_group_code": "",
    "category_group_name": "",
    "category_name": "가정,생활 > 미용 > 미용실 > 블루클럽",
    "distance": "",
    "id": "1890966269",
    "phone": "064-745-7675",
    "place_name": "블루클럽 노형점",
    "place_url": "http://place.map.kakao.com/1890966269",
    "road_address_name": "제주특별자치도 제주시 수덕로 75",
    "x": "126.470196310714",
    "y": "33.4840678734097"
  }
===> 원본 data 


<field>                     <Key>
address         <==         "road_adress_name"
coordx          <==         "x"
coordy          <==         "y"
tel             <==         "phone"
name            <==         "place_name"
===> store model 에 맞게 메칭
"""
