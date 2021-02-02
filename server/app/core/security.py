#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/25 17:50
# @Author  : CoderCharm
# @File    : security.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""

"""

"""
token password 验证
pip install python-jose
pip install passlib
"""

from typing import Any, Union, Optional
from datetime import datetime, timedelta

from jose import jwt
from pydantic import ValidationError
from passlib.context import CryptContext
from fastapi import Header

from app.common import custom_exc
from core import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(
        subject: Union[str, Any], expires_delta: timedelta = None
) -> str:
    """
    生成token
    :param subject:
    :param expires_delta:
    :return:
    """
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    return encoded_jwt


def check_jwt_token(
        token: Optional[str] = Header(None)
) -> Union[str, Any]:
    """
    只解析验证token
    :param token:
    :return:
    """

    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY, algorithms=settings.JWT_ALGORITHM
        )
        return payload
    except (jwt.JWTError, ValidationError, AttributeError):
        raise custom_exc.UserTokenError(err_desc="access token fail")
    except (jwt.ExpiredSignatureError,):
        raise custom_exc.UserTokenError(err_desc="access token expired")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)
