#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/25 13:43
# @Author  : CoderCharm
# @File    : main.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""

"""

from api import create_app

app = create_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app='main:app', host="127.0.0.1", port=8010, reload=True, debug=True)
