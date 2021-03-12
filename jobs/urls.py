#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File Name： urls
# Author : zengyi
# Date： 2021/2/6 15:36
from django.conf import settings
from django.conf.urls import url
from django.urls import path

from jobs import views

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    # 职位列表
    url(r'^joblist/', views.joblist, name='joblist'),

    # 职位详情
    url(r'^job/(?P<job_id>\d+)/$', views.detail, name='detail'),

    # 提交简历
    path('resume/add/', views.ResumeCreateView.as_view(), name='resume-add'),
    path('resume/<int:pk>/', views.ResumeDetailView.as_view(), name='resume-detail'),

    path('sentry-debug/', trigger_error),

    # 管理员创建 HR 账户的页面
    path('create_hr_user/', views.create_hr_user, name='create_hr_user'),

    # 首页自动跳转到 职位列表
    url(r'^$', views.joblist, name='name'),
]

if settings.DEBUG:
    # 有 XSS 漏洞的视图页面，
    urlpatterns += [url(r'^detail_resume/(?P<resume_id>\d+)/$', views.detail_resume, name='detail_resume'),]