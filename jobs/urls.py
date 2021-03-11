#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File Name： urls
# Author : zengyi
# Date： 2021/2/6 15:36
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

    # 首页自动跳转到 职位列表
    url(r'^$', views.joblist, name='name'),
]