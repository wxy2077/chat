#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/7 10:00
# @Author  : CoderCharm
# @File    : init_user.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""

初始化用户信息

"""

import uuid
from loguru import logger

from app.core.security import get_password_hash
from app.common.database import SessionLocal


def init() -> None:
    db = SessionLocal()
    # 初始化用户信息
    user_info = [
        {
            "username": "alvin",
            "password": "12345",
            "nickname": "艾尔文",
            "avatar": "/img/alvin.jpeg"
        },
        {
            "username": "wukong",
            "password": "12345",
            "nickname": "卡卡洛特",
            "avatar": "/img/wukong.jpeg"
        },
        {
            "username": "xiaomao",
            "password": "12345",
            "nickname": "小猫🐱",
            "avatar": "/img/xiaomao.jpg"
        }
    ]
    for item in user_info:
        hashed_password = get_password_hash(password=item["password"])

        sql = f"""INSERT INTO chat_user (user_id, username, hashed_password, nickname, avatar)VALUES(
        "{str(uuid.uuid4()).replace("-",'')}", "{item["username"]}", "{hashed_password}", "{item["nickname"]}", "{item["avatar"]}");"""
        db.execute(sql)
        db.commit()


def main() -> None:
    logger.info("Creating initial data")
    init()
    logger.info("Initial data created")


if __name__ == "__main__":
    main()
