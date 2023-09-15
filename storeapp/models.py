from django.db import models
from datetime import datetime


class Store(models.Model):
    address = models.CharField(max_length=100)   # 한글 주소
    coordx = models.IntegerField()               # x좌표
    coordy = models.IntegerField()               # y좌표
    name = models.CharField(max_length=100)      # Ex. 서귀포 호텔
    storeType = models.CharField(max_length=20)  # Ex. 숙박 시설 | 식당 | 기타...
    # detail = models.CharField(max_length=100)  # AccomDetail | RestauDetail | EtcDetail 추후 변경 가능
    imageSrc = models.ImageField(upload_to='store/', null=True) # 예시 이미지 주소
    target = models.TextField()                  # 할인 대상 Ex. 군인(병사, 부사관, 장교)
    promotion = models.TextField(null=True)      # 할인 정보, Optional
    tel = models.TextField(null=True)            # 전화 번호, Optional
    facilities = models.TextField(null=True)     # 부대 시설, Optional
    homepage = models.TextField(null=True)       # 홈페이지, Optional
    endDate = models.DateTimeField(null=True)    # 할인 종료 날짜, Optional undefined: 기한 없음
