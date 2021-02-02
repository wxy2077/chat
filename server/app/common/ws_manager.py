#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/25 15:56
# @Author  : CoderCharm
# @File    : ws_manager.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""
管理 WebSocket 客户端
"""


from typing import List, Dict

from fastapi import WebSocket


class ConnectionManager:
    def __init__(self):
        # 存放激活的链接
        self.active_connections: List[Dict[str, WebSocket]] = []

    async def connect(self, user: str, ws: WebSocket):
        # 连接ws
        await ws.accept()
        self.active_connections.append({"user": user, "ws": ws})

    def disconnect(self, user: str, ws: WebSocket):
        # 关闭时 移除ws对象
        self.active_connections.remove({"user": user, "ws": ws})

    @staticmethod
    async def send_personal_message(message: dict, ws: WebSocket):
        # 发送个人消息
        await ws.send_json(message)

    @staticmethod
    async def send_heart_pong(ws: WebSocket):
        await ws.send_text("pong")

    async def send_other_message(self, message: dict, user: str):
        # 发送个人消息
        for connection in self.active_connections:
            if connection["user"] == user:
                await connection['ws'].send_json(message)

    async def broadcast(self, data: dict):
        # 广播消息
        for connection in self.active_connections:
            await connection['ws'].send_json(data)


ws_manager = ConnectionManager()
