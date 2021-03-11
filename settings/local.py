from .base import *

DEBUG = True

ALLOWED_HOSTS = ["recruit.ihopeit.com", "127.0.0.1"]

## 务必修改以下值，确保运行时系统安全:
SECRET_KEY = "w$46bks+b3-7f(13#i%v@jwejrnxc$^^#@#@^t@fofizy1^mo9r8(-939243423300"

## 如果仅使用数据库中的账号，以下 LDAP 配置可忽略
## 替换这里的配置为正确的域服务器配置，同时可能需要修改 base.py 中的 LDAP 服务器相关配置:
LDAP_AUTH_URL = "ldap://localhost:389"
LDAP_AUTH_CONNECTION_USERNAME = "admin"
LDAP_AUTH_CONNECTION_PASSWORD = "admin_passwd_4_ldap"

INSTALLED_APPS += (
    # other apps for production site
)


## 钉钉群的 WEB_HOOK， 用于发送钉钉消息
DINGTALK_WEB_HOOK = "https://oapi.dingtalk.com/robot/send?access_token=dec6c67036c259bea4fe5df5786801811ac7c126a192db95831f902ff4aa9b6c"

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration


print(sentry_sdk.init(
    # dsn='http://ef1e23388d2d4c0380de950c5d952748@100.95.173.161:9000/2',
    dsn='https://dd6a4752ee724b74b4ea56e7bcea2170@o547160.ingest.sentry.io/5669768',
    integrations=[DjangoIntegration()],
    # http_proxy=proxies,

    traces_sample_rate=1.0,
    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
).__dict__['_client'].__dict__)



