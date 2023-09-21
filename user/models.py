from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from rest_framework import status
from rest_framework.response import Response
from pymongo import MongoClient


def isDuplicate(user_email: str) -> bool:
    client = MongoClient('mongodb://localhost:27017/')
    db = client['test']
    collection = db['account_emailaddress']
    existing_user = collection.find_one({'email': user_email})

    # 이미 같을 이메일을 사용하는 유저가 있을 경우 중복 처리
    if existing_user:
        print("중복된 이메일입니다.")
        return True
    else:
        return False


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password, **kwargs):
        print("================= Create User =================")
        if not email:
            raise ValueError('Users must have an email address')

        if isDuplicate(user_email=email):
            print(f"중복된 키 오류")
            return Response({"error": "이미 존재하는 데이터입니다."}, status=status.HTTP_400_BAD_REQUEST)

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
        # try:
        #     user.save(using=self._db)
        #     return user
        # except BulkWriteError as bwe:
        #     for error in bwe.details['writeErrors']:
        #         if error['code'] == 11000:  # 중복 키 오류 코드 (E11000)
        #             duplicate_key = error['keyValue']
        #             print(f"중복된 키 오류: {duplicate_key}")
        #             return Response({"error": "이미 존재하는 데이터입니다."}, status=status.HTTP_400_BAD_REQUEST)
        # except Exception as e:
        #     # 다른 예외 처리
        #     print(f"다른 예외 발생: {str(e)}")
        #     return Response({"error": "데이터 처리 중 오류가 발생했습니다."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create_superuser(self, email=None, password=None, **extra_fields):

        if isDuplicate(user_email=email):
            print(f"중복된 키 오류")
            return Response({"error": "이미 존재하는 데이터입니다."}, status=status.HTTP_400_BAD_REQUEST)

        superuser = self.create_user(
            email=email,
            password=password,
        )
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.is_active = True
        superuser.save(using=self._db)
        return superuser


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    # username = models.TextField(max_length=30, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    class Meta:
        app_label = 'user'
        db_table = "users"
        # ordering = ['slug']
