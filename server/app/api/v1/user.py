#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/25 17:36
# @Author  : CoderCharm
# @File    : user.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""

"""

from typing import Union, Any
from datetime import timedelta

from sqlalchemy.orm import Session
from fastapi import APIRouter, Body, Depends

from app.common.database import get_db
from app.core.security import verify_password, create_access_token, check_jwt_token
from app.common import response_code
from app.common import logger
from app.core import settings


router = APIRouter()


@router.post("/auth/login")
async def user_auth(*, db: Session = Depends(get_db), username: str = Body(...), password: str = Body(...)):
    """
    简单模拟登录
    :param db;
    :param username:
    :param password:
    :return:
    """
    sql_query_user = f"SELECT user_id, hashed_password from chat_user WHERE username='{username}'"
    query_user = db.execute(sql_query_user)

    user_res = query_user.fetchone()
    if not user_res:
        return response_code.resp_5000(message="用户名或者密码错误")

    verify_res = verify_password(password, user_res.hashed_password)
    if not verify_res:
        return response_code.resp_5000(message="用户名或者密码错误")

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    return response_code.resp_200(data={
        "token": create_access_token(user_res.user_id, expires_delta=access_token_expires),
    })


@router.get("/user/info", summary="获取用户信息")
async def get_user_info(
    *,
    db: Session = Depends(get_db),
    token_data: Union[str, Any] = Depends(check_jwt_token)
):
    sql_query_user = f"""SELECT nickname, avatar from chat_user WHERE user_id='{token_data.get("sub")}'"""
    query_user = db.execute(sql_query_user)

    user_info = query_user.fetchone()

    return response_code.resp_200(data={
        "authInfo": {
            "userId": token_data.get("sub"),
            "nickname": user_info.nickname,
            "avatar": user_info.avatar
        }
    })


@router.get("/friends/list", summary="好友列表")
async def get_dialog_list(
        *,
        db: Session = Depends(get_db),
        token_data: Union[str, Any] = Depends(check_jwt_token)
):
    sql_query_friends = f"""SELECT * from chat_user_relation WHERE user_id='{token_data.get("sub")}' or friend_id='{token_data.get("sub")}'"""
    query_user = db.execute(sql_query_friends)

    # 查询所有的好友
    user_friends = query_user.fetchall()

    # 添加user_id 或者 friend_id
    friends_list = []
    for i in user_friends:
        friends_list.append(i[1])
        friends_list.append(i[2])

    # 去掉重复的id
    friends_list = list(set(friends_list))
    friends_list.remove(token_data.get("sub"))

    # 查询所有的好友信息
    friends_info_list = []
    for user_id in friends_list:
        # 后续可以考虑 redis缓存 好友信息避免好友多的时候 查询慢
        # 查询用户信息
        sql_user_info = f"""SELECT user_id,nickname,avatar from chat_user WHERE user_id='{user_id}'"""
        query_user_info = db.execute(sql_user_info)
        user_info_res = query_user_info.fetchone()
        friends_info_list.append({
            "userId": user_info_res.user_id,
            "nickname": user_info_res.nickname,
            "avatar": user_info_res.avatar
        })

    return response_code.resp_200(data={
        "friendsInfoList": friends_info_list
    })
