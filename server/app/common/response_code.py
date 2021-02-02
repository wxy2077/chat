#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/25 14:36
# @Author  : CoderCharm
# @File    : response_code.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""

"""

from fastapi import status
from fastapi.responses import JSONResponse, Response

from typing import Union


def resp_200(*, data: Union[list, dict, str]=None, message: str="Success"):

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            'code': 200,
            'message': message,
            'data': data,
        }
    )


def resp_400(*, data: str = None, message: str="BAD REQUEST") -> Response:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            'code': 400,
            'message': message,
            'data': data,
        }
    )


def resp_403(*, data: str = None, message: str="Forbidden") -> Response:
    return JSONResponse(
        status_code=status.HTTP_403_FORBIDDEN,
        content={
            'code': 403,
            'message': message,
            'data': data,
        }
    )


def resp_404(*, data: str = None, message: str="Page Not Found") -> Response:
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            'code': 404,
            'message': message,
            'data': data,
        }
    )


def resp_422(*, data: str = None, message: Union[list, dict, str]="UNPROCESSABLE_ENTITY") -> Response:
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            'code': 422,
            'message': message,
            'data': data,
        }
    )


def resp_500(*, data: str = None, message: Union[list, dict, str]="Server Internal Error") -> Response:
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            'code': "500",
            'message': message,
            'data': data,
        }
    )


# 自定义 重新登录 Token 过期 前端强制重新登录
def resp_5000(*, data: Union[list, dict, str]=None, message: str="Token failure") -> Response:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            'code': 5000,
            'message': message,
            'data': data,
        }
    )


# 没有此用户
def resp_5001(*, data: Union[list, dict, str]=None, message: str="User Not Found") -> Response:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            'code': 5001,
            'message': message,
            'data': data,
        }
    )
