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

# 군 장병 AI · SW 역량강화 by 카오엔터프라이즈 3팀 - MiliDeal
API 개발 담당 저장소입니다.
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
