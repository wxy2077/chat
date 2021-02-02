#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/25 13:47
# @Author  : CoderCharm
# @File    : __init__.py.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""

"""

import traceback

from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError, ValidationError
from aioredis import create_redis_pool

from app.core import settings
from app.common import logger
from app.common import response_code
from app.common import custom_exc

from app.api.v1 import api_v1_router


def create_app():
    """
    生成FatAPI对象
    :return:
    """
    app = FastAPI(
        title=settings.PROJECT_TITLE,
        description=settings.PROJECT_DESC,
    )

    # 其余的一些全局配置可以写在这里 多了可以考虑拆分到其他文件夹

    # 跨域设置
    register_cors(app)

    # 注册路由
    register_router(app)

    # 注册捕获全局异常
    register_exception(app)

    # 请求拦截
    register_middleware(app)

    # 挂载redis
    # register_redis(app)

    return app


def register_router(app: FastAPI):
    """
    注册路由
    这里暂时把两个API服务写到一起，后面在拆分
    :param app:
    :return:
    """
    # 项目API
    app.include_router(
        api_v1_router,
        prefix=settings.API_V1_STR  # 前缀
    )


def register_cors(app: FastAPI):
    """
    支持跨域
    :param app:
    :return:
    """
    app.add_middleware(
        CORSMiddleware,
        # allow_origins=["http://192.168.101.123:8080"],
        allow_origin_regex='https?://.*',  # 改成用正则就行了
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def register_exception(app: FastAPI):
    """
    捕获全局异常
    :param app:
    :return:
    """

    @app.exception_handler(custom_exc.UserTokenError)
    async def inner_validation_exception_handler(request: Request, exc: custom_exc.UserTokenError):
        """
        内部参数验证异常
        :param request:
        :param exc:
        :return:
        """
        logger.error(
            f"Token错误\nURL:{request.method}{request.url}\nHeaders:{request.headers}\n{traceback.format_exc()}")
        return response_code.resp_5000(message=exc.err_desc)

    @app.exception_handler(custom_exc.TokenExpired)
    async def inner_validation_exception_handler(request: Request, exc: custom_exc.TokenExpired):
        """
        内部参数验证异常
        :param request:
        :param exc:
        :return:
        """
        logger.error(
            f"Token过期\nURL:{request.method}{request.url}\nHeaders:{request.headers}\n{traceback.format_exc()}")
        return response_code.resp_5000(message=exc.err_desc)

    @app.exception_handler(ValidationError)
    async def inner_validation_exception_handler(request: Request, exc: ValidationError):
        """
        内部参数验证异常
        :param request:
        :param exc:
        :return:
        """
        logger.error(
            f"内部参数验证错误\nURL:{request.method}{request.url}\nHeaders:{request.headers}\n{traceback.format_exc()}")
        return response_code.resp_500(message=exc.errors())

    @app.exception_handler(RequestValidationError)
    async def request_validation_exception_handler(request: Request, exc: RequestValidationError):
        """
        请求参数验证异常
        :param request:
        :param exc:
        :return:
        """
        logger.error(
            f"请求参数格式错误\nURL:{request.method}{request.url}\nHeaders:{request.headers}\n{traceback.format_exc()}")
        return response_code.resp_422(message=exc.errors())

    # 捕获全部异常
    @app.exception_handler(Exception)
    async def all_exception_handler(request: Request, exc: Exception):
        """
        全局所有异常
        :param request:
        :param exc:
        :return:
        """
        logger.error(f"全局异常\n{request.method}URL:{request.url}\nHeaders:{request.headers}\n{traceback.format_exc()}")
        return response_code.resp_500(message="服务器内部错误")


def register_middleware(app: FastAPI):
    """
    请求响应拦截 hook
    https://fastapi.tiangolo.com/tutorial/middleware/
    :param app:
    :return:
    """

    @app.middleware("http")
    async def logger_request(request: Request, call_next):
        # https://stackoverflow.com/questions/60098005/fastapi-starlette-get-client-real-ip
        # logger.info(f"访问记录:{request.method} url:{request.url}\nheaders:{request.headers}\nIP:{request.client.host}")

        response = await call_next(request)

        return response


def register_redis(app: FastAPI) -> None:
    """
    把redis挂载到app对象上面
    :param app:
    :return:
    """

    @app.on_event('startup')
    async def startup_event():
        """
        获取链接
        :return:
        """
        app.state.redis = await create_redis_pool(settings.REDIS_URL)

    @app.on_event('shutdown')
    async def shutdown_event():
        """
        关闭
        :return:
        """
        app.state.redis.close()
        await app.state.redis.wait_closed()
