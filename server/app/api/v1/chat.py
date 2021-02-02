#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/25 15:45
# @Author  : CoderCharm
# @File    : chat.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""

"""
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from websockets.exceptions import ConnectionClosedOK

from app.common.ws_manager import ws_manager
from app.common import logger
from app.core.security import check_jwt_token

router = APIRouter()


@router.websocket("/ws/{token}")
async def websocket_endpoint(ws: WebSocket, token: str):
    """
    :param ws:
    :param token:
    :return:
    """
    user_sub = check_jwt_token(token)
    user_id = user_sub.get("sub")

    await ws_manager.connect(user_id, ws)
    logger.info(f"{user_id}-连接WebSocket")

    # 广播
    # await ws_manager.broadcast({"username": user, "message": "enter chat room"})

    try:
        while True:
            data = await ws.receive_json()
            logger.info(f"接收数据{data}, {type(data)}")

            message_type = data.get("messageType")
            to_target_id = data.get("toTargetId")  # 用户id 或者 组id

            # 发送给自己
            # await ws_manager.send_personal_message(data, ws)

            if message_type == 1000:
                # 发送给客户端格式
                # {
                #   "userId": "xx",
                #   "toTargetId": "xxx",
                #   "message": "xx"
                # }
                send_json = {
                    "userId": user_id,
                    "messageType": message_type,
                    "toTargetId": to_target_id,
                    "message": data["message"],
                    "timestamp": data["timestamp"]
                }
                logger.info(f"发送给他人{message_type}-{send_json}")
                # await ws_manager.send_personal_message(send_json, ws)
                await ws_manager.send_other_message(send_json, to_target_id)
            # else:
            #     # 群发
            #     logger.info(f"群发数据-{data}")
            #     await ws_manager.broadcast({"username": user, "message": data['message']})

    except WebSocketDisconnect:
        logger.info(f"{user_id}-离开")
        # 关闭连接
        ws_manager.disconnect(user_id, ws)
        # await ws_manager.broadcast({"user": user, "message": "离开"})
    except ConnectionClosedOK:
        # 关闭连接
        ws_manager.disconnect(user_id, ws)
        logger.info(f"{user_id}-页面关闭离开")
