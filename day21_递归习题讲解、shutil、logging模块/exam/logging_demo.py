# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/27 06:59
# 文件名称: logging_demo.py

import logging
import time
from logging import handlers

# 屏幕输出
sh = logging.StreamHandler()
# 按文件大小切割
rfh = handlers.RotatingFileHandler(filename=r'./logs/rf.log', maxBytes=1024, backupCount=5, encoding='utf-8')
rfh.setLevel(logging.ERROR) # 优先级高于basicConfig
# 按时间切割
time_rfh = handlers.TimedRotatingFileHandler(filename='./logs/trfh.log', when='S', interval=5, backupCount=5, encoding='utf-8')

# logging配置日志格式
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s[line: %(lineno)d]-%(module)s: %(message)s',
    datefmt = '%Y-%m-%s %H:%M:%S',
    level = logging.DEBUG,
    handlers=[sh, rfh, time_rfh]

)

if __name__ == '__main__':
    for i in range(1, 100):
        time.sleep(1)
        logging.debug('测试日志屏幕输出及文件切割(按大小切割、按时间切割) %s' % (str(i)))


