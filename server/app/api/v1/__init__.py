#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/25 15:44
# @Author  : CoderCharm
# @File    : __init__.py.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""

"""

from fastapi import APIRouter
from app.api.v1 import chat
from app.api.v1 import user

api_v1_router = APIRouter()


api_v1_router.include_router(chat.router, tags=["聊天"])
api_v1_router.include_router(user.router, tags=["用户"])
