```
┌────────────────────────────────────────┐
 ___  ___ _  _  _ ______               _
 |  \/  |(_)| |(_)|  _  \             | |
 | .  . | _ | | _ | | | |  ___   __ _ | |
 | |\/| || || || || | | | / _ \ / _` || |
 | |  | || || || || |/ / |  __/| (_| || |
 \_|  |_/|_||_||_||___/   \___| \__,_||_|
	             🤑 𝙔𝙤𝙪 𝙘𝙖𝙣 𝙜𝙚𝙩 𝙖 𝙙𝙞𝙨𝙘𝙤𝙪𝙣𝙩!
└────────────────────────────────────────┘
```

# ![Static Badge](https://img.shields.io/badge/Kakao_Enterprise-FFCD00?style=flat-square&logo=kakao&logoColor=white&labelColor=%23FFCD00) × ![Static Badge](https://img.shields.io/badge/Goorm-%23000000?style=flat-square&logo=Goorm&logoColor=%23FFFFFF) 군 장병 AI · SW 역량강화

SW 3팀 **MiliDeal**  
API 개발 저장소입니다.

# Environments

![Static Badge](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![Static Badge](https://img.shields.io/badge/Python-%233776AB?style=for-the-badge&logo=Python&logoColor=%23FFFFFF)
![Static Badge](https://img.shields.io/badge/Django-%23092E20?style=for-the-badge&logo=Django)
![Static Badge](https://img.shields.io/badge/MongoDB-%2347A248?style=for-the-badge&logo=MongoDB&logoColor=%23FFFFFF)

| Contribute | version |
| ---------- | ------- |
| Ubuntu     | 18.04   |
| Python     | 3.9     |
| Django	 | 4.1.10  |
| MongoDB    | 4.4.24  |

## For Contributers

### Commit Message

기본적으로 https://gitmoji.dev/ 의 아이콘을 사용하여 다음과 같이 작성합니다.

```md
:sparkles: Add Search API
:bug: Fix Djongo Manager Error
```

주로 사용하는 아이콘은 다음과 같습니다.

- :sparkles: - 새 기능 추가
- :zap: - 성능 개선
- :fire: - 코드 삭제
- :bug: - 버그 수정
- :adhesive_bandage: - 그렇게 엄청 심각하지 않은 문제 수정
- :rotating_light: 컴파일러 / 린터 경고 수정
- :ambulance: - 핫픽스
- :bulb: - 주석 수정
- :card_file_box: - 데이터베이스 관련 수정
- :memo: - 문서 추가 또는 수정
- :pencil2: - 오타 수정
- :package: 패키지 추가 / 삭제
- :twisted_rightwards_arrows: 브랜치 머지
- :poop: - 응가 코드

## DataBase

### Entity Relationship Diagram

```mermaid
---
title: MiliDeal DB Schema
---
%%{
	init: {
		"theme": "forest",
		"themeCSS": [
			"[id*=entity-Store] .er.entityBox { fill: orange;}",
			"[id*=entity-User] .er.entityBox { fill: #CC6692;}"
		]}
}%%
erDiagram
	Store||--o{ Review : ""
	User ||--o{ Review : ""
	Store {
    ObjectId _id PK
		Slug slug PK, FK
		Char(100) address
		Float coordx
		Float coordy
		Char(100) name
		Char(20) storeType
		Image imageSrc
		Char(3) target
		Text promotion
		Text tel
		Text facilities
		Text homepage
		DateTime endDate
	}

	Review {
		ObjectId _id PK
		Objectid reviewOf FK
		Embedding author_id FK
		Text review
		Float score
	}

	User {
		ObjectId _id PK
		Char name
		Integer age
		Boolean isMilitary
		Char military_rank "계급 + 군무원"

		Char troop
	}
```

## Contributers

<table>
  <tbody>
    <tr>
      <td align="center"><a href="https://github.com/woohyun212"><img src="https://avatars.githubusercontent.com/u/43837268?v=4" 
	  style="border-radius:50%" width="100px;" alt="woohyun212"/><br /><sub><b>woohyun</b></sub></a></td>
      <td align="center"><a href="https://github.com/callendev20"><img src="https://avatars.githubusercontent.com/u/63829204?v=4" style="border-radius:50%" width="100px;" alt="callendev20"/><br /><sub><b>Jeon Somyeong</b></sub></a></td>
	  <td align="center"><a href="https://github.com/yeonjunky"><img src="https://avatars.githubusercontent.com/u/57308980?v=4" style="border-radius:50%" width="100px;" alt="yeonjunky"/><br /><sub><b>yeonjunkim</b></sub></a></td>
    </tr>
  </tbody>
</table>
