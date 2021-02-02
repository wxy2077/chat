#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/25 14:24
# @Author  : CoderCharm
# @File    : setting.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""

"""

import os
from typing import List, Union

from pydantic import BaseSettings, AnyHttpUrl, IPvAnyAddress


class Settings(BaseSettings):

    DEBUG: bool = True

    PROJECT_TITLE: str = "聊天服务端"
    PROJECT_DESC: str = "这是使用FastAPI WebSocket的服务端"

    API_V1_STR: str = "/api/chat/v1"
    # SECRET_KEY 记得保密生产环境 不要直接写在代码里面
    SECRET_KEY: str = "(-ASp+_nvVG-iqKyJSD&*&^-H312(*^$YRzRE"

    # jwt加密算法
    JWT_ALGORITHM: str = "HS256"

    # jwt token过期时间 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    # 根路径
    BASE_DIR: str = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))

    # 跨域
    BACKEND_CORS_ORIGINS: List[str] = ['*']

    # 配置你的Mysql环境
    MYSQL_USERNAME: str = 'root'
    MYSQL_PASSWORD: str = "Admin12345-"
    MYSQL_HOST: Union[AnyHttpUrl, IPvAnyAddress] = "172.16.137.129"
    MYSQL_DATABASE: str = 'Chat'

    # Mysql地址
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@" \
                              f"{MYSQL_HOST}/{MYSQL_DATABASE}?charset=utf8mb4"

    # redis配置
    # REDIS_HOST: str = "172.16.137.129"
    # REDIS_PASSWORD: str = "root12345"
    # REDIS_DB: int = 10
    # REDIS_PORT: int = 6379
    # REDIS_URL: str = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}?encoding=utf-8"

    class Config:
        case_sensitive = True


settings = Settings()

