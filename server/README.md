# Chat Server

![FastAPI](https://img.shields.io/badge/FastAPI-0.61.0-brightgreen)
![Python](https://img.shields.io/badge/Python-3.6+-blue)

## Intro

This is a simple chat server program demo, 
more details on the FastApi project directory, please refer to [my other project](https://github.com/CoderCharm/fastapi-mysql-generator)

## Run

#### Install Dependency package

```
pip install -r requirements.txt
```

#### Start

```
python main.py
```

or

```
uvicorn main:app --host=127.0.0.1 --port=8010 --workers=4
```



## Custom ws interaction protocol

Interaction using JSON format.

send to ws server

```json5
{
    "token": "xxxx",
    "messageType": 1000 ,  // 1000 send to friend; 2000 send to group;  3000 other 
    "toTargetId": "userId",  // userId or groupId
    "message": "xxxx",
    "timestamp": "timestamp"
}
```

send to ws client
```json5
{ 
  "userId": "xx",
  "messageType": 1000 ,  // 1000 send to friend; 2000 send to group;  3000 other 
  "toTargetId": "xxx",
  "message": "xx",
  "timestamp": "timestamp"
}
```
