#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/25 14:29
# @Author  : CoderCharm
# @File    : logger.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""

"""

import os
import time
from loguru import logger

from app.core import settings

# 定位到log日志文件
log_path = os.path.join(settings.BASE_DIR, 'logs')

if not os.path.exists(log_path):
    os.mkdir(log_path)

log_path_error = os.path.join(log_path, f'{time.strftime("%Y-%m-%d")}_error.log')


# 日志简单配置
# 具体其他配置 可自行参考 https://github.com/Delgan/loguru
logger.add(log_path_error, rotation="12:00", retention="5 days", enqueue=True)


# 只导出 logger
__all__ = ["logger"]
