#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/25 14:35
# @Author  : CoderCharm
# @File    : custom_exc.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""
自定义异常
"""


class UserTokenError(Exception):
    def __init__(self, err_desc: str = "user auth error"):
        self.err_desc = err_desc


class TokenExpired(Exception):
    def __init__(self, err_desc: str = "token expired"):
        self.err_desc = err_desc
