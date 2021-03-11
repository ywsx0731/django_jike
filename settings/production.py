from .base import *

DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1"]

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

print(sentry_sdk.init(
    dsn="http://ef1e23388d2d4c0380de950c5d952748@100.95.173.161:9000/2",
    integrations=[DjangoIntegration()],

    traces_sample_rate=1.0,
    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
).__dict__['_client'].__dict__)
