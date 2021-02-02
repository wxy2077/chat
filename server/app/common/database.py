#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/5 17:40
# @Author  : CoderCharm
# @File    : database.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""

"""

from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core import settings

engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URI
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
