import os
from datetime import timedelta

import environ

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# envirion Key Management Module

env_keys = environ.Env()

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = env_keys('SECRET_KEY')
DEBUG = True
ALLOWED_HOSTS = [".run.goorm.io", '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'mainAPI',
    'store',
    'user',

    # djangorestframework
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'dj_rest_auth',
    'dj_rest_auth.registration',

    # allauth
    'allauth',
    'allauth.account',

    # django-rest-swagger
    'rest_framework_swagger',

    # Django Basic Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'MiliDeal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'MiliDeal.wsgi.application'

SITE_ID = 1                               # Site 의 ID, UID 와 비슷한 개념

AUTH_USER_MODEL = 'user.User'             # Auth 모델로 user app 의 User 를 사용 o
REST_USE_JWT = True                       # JsonWebToken 사용 o
ACCOUNT_USER_MODEL_USERNAME_FIELD = None  # username 필드 사용 x, 대신 nickname 필드 생성
ACCOUNT_EMAIL_REQUIRED = True             # email 필드 사용 o
ACCOUNT_USERNAME_REQUIRED = False         # username 필드 사용 x
ACCOUNT_AUTHENTICATION_METHOD = 'email'   # 로그인 인증 방법 (username, email, username_email 중 email)
ACCOUNT_UNIQUE_EMAIL = True               # Email 중복 불허
ACCOUNT_EMAIL_VERIFICATION = 'none'       # 회원가입 과정에서 이메일 인증 사용 X

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'ENFORCE_SCHEMA': True,
        'LOGGING': {
            'version': 1,
            'loggers': {
                'djongo': {
                    'level': 'DEBUG',
                    'propagate': False,
                }
            },
        }, 'NAME': env_keys('mongo_collection'),
        'CLIENT': {
            'host': env_keys('mongo_host'),
            'port': int(env_keys('mongo_port')),
            'username': env_keys('mongo_username'),
            'password': env_keys('mongo_password'),
            'authSource': env_keys('mongo_authSource'),
            'authMechanism': env_keys('mongo_authMechanism')
        }
    },
    # 'user_db': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # },
}

# DATABASE_ROUTERS = [
#     'Util.db_Router.UserRouter',
# ]

from djongo.operations import DatabaseOperations

DatabaseOperations.conditional_expression_supported_in_where_clause = (
    lambda *args, **kwargs: False
)
 

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

# Django REST Framework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.IsAdminUser',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

# JWT (JSON Web Token) 설정.
# https://dj-rest-auth.readthedocs.io/en/latest/installation.html
REST_AUTH = {
    # 'SESSION_LOGIN': False,
    'USE_JWT': True,
    'JWT_AUTH_COOKIE': 'user-auth',
    'JWT_AUTH_REFRESH_COOKIE': 'user-refresh-token',
}

REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'user.serializers.CustomRegisterSerializer',
}

JWT_AUTH_COOKIE = 'jwt-auth'

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    
    # Token 지속 시간 설정
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),         # access
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),    # refresh
}
