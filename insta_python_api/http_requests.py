#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @description : description
# @file    : http_requests.py
# @author  : xingpeidong
# @email   : xpd1437@126.com
# @time    : 2024/3/14 17:00
"""
import hashlib
import os
import requests
import time
import yaml


# 获取配置文件内容
def get_config():
    # 获取配置文件路径
    path = "../config/config.yaml"
    if not os.path.exists(path):
        path = '../config/example_config.yaml'
        with open(path, "r", encoding="utf-8") as f:
            try:
                value = f.read()
                return yaml.safe_load(value)
            except:
                return {}
    else:
        with open(path, "r", encoding="utf-8") as f:
            try:
                value = f.read()
                return yaml.safe_load(value)
            except:
                return {}


# 获取header和加密
def get_headers(config):
    # timestamp
    timestamp = int(time.time())
    # appid 和 secret
    app_id = config["instafogging"]["appid"]
    secret_key = config["instafogging"]["secret_key"]
    # 获取加密signature
    str_for_md5 = str(timestamp) + str(app_id) + str(secret_key)
    # make signature
    md5 = hashlib.md5()
    md5.update(str_for_md5.encode(encoding='utf-8'))
    signature = md5.hexdigest()
    # 组织请求header参数
    headers = {
        'appid': app_id,
        'timestamp': str(timestamp),
        'signature': signature,
        'Content-Type': 'application/json'
    }
    return headers


# 请求数据
def send_request(method, url, headers, payload):
    res = requests.request(method, url, headers=headers, data=payload)
    response = res.json()
    if response["code"] == 0 and response['result'] is not None:
        return response['result']
    else:
        return []
