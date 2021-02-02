#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/19 13:38
# @Author  : CoderCharm
# @File    : test_main.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""

这是一个最简单的demo WebSocket 核心实现逻辑。

https://stackoverflow.com/questions/15219858/how-to-store-a-complex-object-in-redis-using-redis-py

obj = ExampleObject()
pickled_object = pickle.dumps(obj)
r.set('some_key', pickled_object)
unpacked_object = pickle.loads(r.get('some_key'))
obj == unpacked_object



typing.Dict[key_type, value_type]

"""

from typing import List, Dict

from websockets.exceptions import ConnectionClosedOK
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()


class ConnectionManager:
    def __init__(self):
        # 存放激活的链接
        self.active_connections: List[Dict[str, WebSocket]] = []

    async def connect(self, user: str, ws: WebSocket):
        # 连接ws
        await ws.accept()
        self.active_connections.append({"user": user, "ws": ws})

    def disconnect(self,user: str, ws: WebSocket):
        # 关闭时 移除ws对象
        self.active_connections.remove({"user": user, "ws": ws})

    @staticmethod
    async def send_personal_message(message: dict, ws: WebSocket):
        # 发送个人消息
        await ws.send_json(message)

    async def send_other_message(self, message: dict, user: str):
        # 发送个人消息
        for connection in self.active_connections:
            if connection["user"] == user:
                await connection['ws'].send_json(message)

    async def broadcast(self, data: dict):
        # 广播消息
        for connection in self.active_connections:
            await connection['ws'].send_json(data)


manager = ConnectionManager()


@app.websocket("/ws/{user}")
async def websocket_endpoint(ws: WebSocket, user: str):

    await manager.connect(user, ws)

    await manager.broadcast({"user": user, "message": "进入聊天"})

    try:
        while True:
            data = await ws.receive_json()
            print(data, type(data))

            send_user = data.get("send_user")

            if send_user:
                await manager.send_personal_message(data, ws)
                await manager.send_other_message(data, send_user)
            else:
                await manager.broadcast({"user": user, "message": data['message']})

    except WebSocketDisconnect:
        print(f"{user}-离开")
        manager.disconnect(user, ws)
        await manager.broadcast({"user": user, "message": "离开"})
    except ConnectionClosedOK:
        manager.disconnect(user, ws)
        print(f"{user}-页面关闭离开")


if __name__ == "__main__":
    import uvicorn
    # 官方推荐是用命令后启动 uvicorn main:app --host=127.0.0.1 --port=8010 --reload
    uvicorn.run(app='test_main:app', host="127.0.0.1", port=8020, reload=True, debug=True)
