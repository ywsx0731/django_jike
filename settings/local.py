from .base import *

DEBUG = True

STATIC_URL = '/static/'

ALLOWED_HOSTS = ["recruit.ihopeit.com", "127.0.0.1", '*']

## 务必修改以下值，确保运行时系统安全:
SECRET_KEY = "w$46bks+b3-7f(13#i%v@jwejrnxc$^^#@#@^t@fofizy1^mo9r8(-939243423300"

## 如果仅使用数据库中的账号，以下 LDAP 配置可忽略
## 替换这里的配置为正确的域服务器配置，同时可能需要修改 base.py 中的 LDAP 服务器相关配置:
LDAP_AUTH_URL = "ldap://localhost:389"
LDAP_AUTH_CONNECTION_USERNAME = "admin"
LDAP_AUTH_CONNECTION_PASSWORD = "admin_passwd_4_ldap"

INSTALLED_APPS += (
    'debug_toolbar',    # other apps for production site
)

CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/1'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERYD_MAX_TASKS_PER_CHILD = 10
CELERYD_LOG_FILE = os.path.join(BASE_DIR, "logs", "celery_work.log")
CELERYBEAT_LOG_FILE = os.path.join(BASE_DIR, "logs", "celery_beat.log")

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        'TIMEOUT': 300, # default expire time per api call
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            # "PASSWORD": "mysecret",
            "SOCKET_CONNECT_TIMEOUT": 5,  # in seconds
            "SOCKET_TIMEOUT": 5,  # r/w timeout in seconds
        }
    }
}

# 阿里云 CDN 存储静态资源文件 & 阿里云存储上传的图片/文件
# STATICFILES_STORAGE = 'django_oss_storage.backends.OssStaticStorage'

# DEFAULT_FILE_STORAGE = 'django_oss_storage.backends.OssMediaStorage'

# AliCloud access key ID
# OSS_ACCESS_KEY_ID = ''
# # AliCloud access key secret
# OSS_ACCESS_KEY_SECRET = ''
# # The name of the bucket to store files in
# OSS_BUCKET_NAME = 'django-recruitment-zy'
#
# # The URL of AliCloud OSS endpoint
# # Refer https://www.alibabacloud.com/help/zh/doc-detail/31837.htm for OSS Region & Endpoint
# OSS_ENDPOINT = 'oss-cn-beijing.aliyuncs.com'

## 钉钉群的 WEB_HOOK， 用于发送钉钉消息
DINGTALK_WEB_HOOK = "https://oapi.dingtalk.com/robot/send?access_token=dec6c67036c259bea4fe5df5786801811ac7c126a192db95831f902ff4aa9b6c"

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration


sentry_sdk.init(
    # dsn='http://ef1e23388d2d4c0380de950c5d952748@100.95.173.161:9000/2',
    dsn='https://dd6a4752ee724b74b4ea56e7bcea2170@o547160.ingest.sentry.io/5669768',
    integrations=[DjangoIntegration()],
    # http_proxy=proxies,

    traces_sample_rate=1.0,
    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)



# set DJANGO_SETTINGS_MODULE=settings.local
# celery -A recruitment worker -l info -P eventlet
# celery -A recruitment flower
# celery -A recruitment beat --scheduler django_celery_beat.schedulers:DatabaseScheduler

# python manage.py runserver 0.0.0.0:8000 --settings=settings.local
# gunicorn -w 3 -b 127.0.0.1:8000 recruitment.wsgi:application
# export DJANGO_SETTINGS_MODULE=settings.local;/antenv/bin/gunicorn -w 3 -b 0.0.0.0:3000 recruitment.wsgi:application
# gunicorn -w 3 -b 10.0.1.4:8000 recruitment.wsgi:application
# gunicorn -w 3 -b 137.117.67.120:8000 recruitment.wsgi:application
# uvicorn recruitment.asgi:application --workers 3
# python manage.py check --deploy   部署前的安全检查
# curl 127.0.0.1:3000/admin