#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File Name： performance
# Author : zengyi
# Date： 2021/3/7 17:41
import time
import logging

logger = logging.getLogger(__name__)

def performance_logger_middleware(get_response):
    def middleware(request):
        start_time = time.time()
        response = get_response(request)
        duration = time.time() - start_time
        response['X-Page-Duration-ms'] = int(duration * 1000)
        logger.info('%s %s %s', duration, request.path, request.GET.dict())
        return response
    return middleware