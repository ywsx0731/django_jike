#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dingtalkchatbot.chatbot import DingtalkChatbot

from django.conf import settings

def send(message, at_mobiles=[]):
    webhook = settings.DINGTALK_WEB_HOOK

    xiaoding = DingtalkChatbot(webhook)

    xiaoding.send_text(msg=('面试通知： %s' % message), at_mobiles=['17388951098'])
