from djongo import models


class TargetModel(models.Model):
    _id = models.ObjectIdField()
    slug = models.SlugField(unique=True)

    class Meta:
        db_table = "targets"
        ordering = ['slug']
    pass


class StoreModel(models.Model):
    _id = models.ObjectIdField()
    slug = models.SlugField(unique=True)
    address = models.CharField(max_length=100)   # 한글 주소
    coord = models.JSONField(null=False)
    name = models.CharField(max_length=100)      # Ex. 서귀포 호텔
    # Ex. 숙박 시설 | 식당 | 기타...
    storeTypes = (
        ('accommodation', '숙박 시설'),
        ('food', '식당'),
        ('culture', '문화시설'),
        ('etc', '기타')
    )
    storeType = models.CharField(max_length=20, choices=storeTypes)
    imageSrc = models.ImageField(upload_to='store', null=True)  # 예시 이미지 주소
    # 할인 대상 Ex. 군인(병사, 부사관, 장교)
    TARGET_CHOICES = (
        ('ALL', '장병 및 군무원'),  # ALL
        ('ADS', '현역 용사 만'),  # Active Duty Solider
        ('OS', '장병 만'),  # Only Soldier
        ('PS', '직업군인 만'),  # professional soldier
        ('MC', '군무원 만'))  # Military Civilian
    target = models.CharField(max_length=3, choices=TARGET_CHOICES)
    # target = models.TextField()
    promotion = models.TextField(null=True)      # 할인 정보, Optional
    tel = models.TextField(null=True)            # 전화 번호, Optional
    facilities = models.TextField(null=True)     # 부대 시설, Optional
    homepage = models.TextField(null=True)       # 홈페이지, Optional
    # 할인 종료 날짜, Optional undefined: 기한 없음
    endDate = models.DateTimeField(null=True)
    objects = models.DjongoManager()

    class Meta:
        db_table = "stores"
        ordering = ['slug']

    def __str__(self):
        return self.slug
