#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @description : description
# @file    : example_http_requests.py.py
# @author  : xingpeidong
# @email   : xpd1437@126.com
# @time    : 2024/3/15 11:03
"""
import json
import os
import time

from insta_python_api import http_requests

if __name__ == "__main__":
    try:
        # 获取配置文件路径
        # 获取配置文件数据
        config = http_requests.get_config()
        # 生成接口地址和URI
        host = config["instafogging"]["host"]
        uri = config['instafogging']['uri']['get_logfile']
        request_url = host + uri
        # 获取请求headers
        headers = http_requests.get_headers(config)
        data = {
            "format_type": "5min",
            "start_time": time.strftime('%Y-%m-%d 00:00:00'),
            "end_time": time.strftime('%Y-%m-%d %H:%M:%S')
        }
        request_data = json.dumps(data)
        print("POST", request_url, headers, request_data)
        response = http_requests.send_request("POST", request_url, headers, request_data)
        print(response)
    except ValueError as ve:
        print("Exception %s\n" % ve)

