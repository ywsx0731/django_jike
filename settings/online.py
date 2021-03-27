from .base import *

DEBUG = True

ALLOWED_HOSTS = ['137.117.67.120', "recruit.ihopeit.com", "127.0.0.1", 'zhaoping.ihopeit.com', 'qing0628.top', '10.0.1.4', 'qing.eastus.cloudapp.azure.com']

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'w$46iie+a8-7f(13#i%v@pa@+fbm^t@fofizy1^m69r8(-h16o3s882')

DEBUG = False
INSTALLED_APPS += (
    'debug_toolbar', # and other apps for local development
)

INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]

CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/1'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERYD_MAX_TASKS_PER_CHILD = 10
CELERYD_LOG_FILE = os.path.join(BASE_DIR, "logs", "celery_work.log")
CELERYBEAT_LOG_FILE = os.path.join(BASE_DIR, "logs", "celery_beat.log")

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

'''
sentry_sdk.init(
    dsn="http://xxx@recruit.ihopeit.com:9000/2",
    integrations=[DjangoIntegration()],
    # performance tracing sample rate, 采样率, 生产环境访问量过大时，建议调小（不用每一个URL请求都记录性能）
    traces_sample_rate=1.0, # 

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)
'''

## 如果仅使用数据库中的账号，以下 LDAP 配置可忽略
## 替换这里的配置为正确的域服务器配置，同时可能需要修改 base.py 中的 LDAP 服务器相关配置:
LDAP_AUTH_URL = os.environ.get('LDAP_AUTH_URL', 'ldap://localhost:389')
LDAP_AUTH_CONNECTION_USERNAME = os.environ.get('LDAP_AUTH_CONNECTION_USERNAME')
LDAP_AUTH_CONNECTION_PASSWORD = os.environ.get('LDAP_AUTH_CONNECTION_PASSWORD')

# STATIC_URL = 'http://icdn.ihopeit.com/static/'
STATIC_URL = '/static/'

# 阿里云 CDN 存储静态资源文件 & 阿里云存储上传的图片/文件
# STATICFILES_STORAGE = 'django_oss_storage.backends.OssStaticStorage'

DEFAULT_FILE_STORAGE = 'django_oss_storage.backends.OssMediaStorage'

# AliCloud access key ID
OSS_ACCESS_KEY_ID = os.environ.get('OSS_ACCESS_KEY_ID', '')
# AliCloud access key secret
OSS_ACCESS_KEY_SECRET = os.environ.get('OSS_ACCESS_KEY_SECRET', '')
# The name of the bucket to store files in
OSS_BUCKET_NAME = 'django-recruitment-zy'

# The URL of AliCloud OSS endpoint
# Refer https://www.alibabacloud.com/help/zh/doc-detail/31837.htm for OSS Region & Endpoint
OSS_ENDPOINT = 'oss-cn-beijing.aliyuncs.com'

DINGTALK_WEB_HOOK_TOKEN = os.environ.get('DINGTALK_WEB_HOOK_TOKEN', '')
DINGTALK_WEB_HOOK = "https://oapi.dingtalk.com/robot/send?access_token=%s" % DINGTALK_WEB_HOOK_TOKEN


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