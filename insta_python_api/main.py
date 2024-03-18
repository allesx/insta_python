#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @description : description
# @file    : main.py
# @author  : xingpeidong
# @email   : xpd1437@126.com
# @time    : 2024/3/14 16:56
"""
import sys
import time

from insta_python_api import apis


def main():
    try:
        data = {
            "format_type": "5min",
            "start_time": time.strftime('%Y-%m-%d 00:00:00'),
            "end_time": time.strftime('%Y-%m-%d %H:%M:%S'),
            # "domain": "example.domain"
        }
        print("POST", data)

        response = apis.get_logfile(data)
        print(response)

    except ValueError as ve:
        return str(ve)


if __name__ == "__main__":
    sys.exit(main())
