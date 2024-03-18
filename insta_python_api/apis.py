#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @description : description
# @file    : apis.py
# @author  : xingpeidong
# @email   : xpd1437@126.com
# @time    : 2024/3/14 12:22
"""
import json

from insta_python_api import http_requests


def get_logfile(data):
    try:
        # 获取配置文件数据
        config = http_requests.get_config()
        # 生成接口地址和URI
        host = config["instafogging"]["host"]
        uri = config['instafogging']['uri']['get_logfile']
        request_url = host + uri
        # 获取请求headers
        headers = http_requests.get_headers(config)
        request_data = json.dumps(data)
        return http_requests.send_request("POST", request_url, headers, request_data)
    except ValueError as ve:
        return str(ve)
