# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 11:28:02 2018

@author: Administrator
"""

import logging
import sys

# 获取logger的实例
logger = logging.getLogger('testLogger')

# 指定当前日志格式
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

# 创建日志对象的Handler
# 文件日志
file_handler = logging.FileHandler("testLogger3.log")
file_handler.setFormatter(formatter)

# 设置一个默认的级别，低于这个级别的信息将不会被写入日志系统
logger.setLevel(logging.INFO)

# 终端日志
#console_handler = logging.StreamHandler(sys.stdout)
#console_handler.setFormatter(formatter)

# 把文件日志，终端日志handlers 添加到日志处理系统中
logger.addHandler(file_handler)
#logger.addHandler(console_handler)

logger.critical("test critical in log")
logger.error("test error in log")
logger.debug("test debug in log")


# 不用这个日志handlers时，需要移除
logger.removeHandler(file_handler)
#logger.removeHandler(console_handler)













