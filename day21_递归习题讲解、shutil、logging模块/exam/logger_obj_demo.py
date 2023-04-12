# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/27 07:33
# 文件名称: logger_obj_demo.py

import logging

logger = logging.getLogger()

# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('test.log',encoding='utf-8')
# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
# 日志格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# 日志记录登记
fh.setLevel(logging.DEBUG)
# 设置handler格式
fh.setFormatter(formatter)
ch.setFormatter(formatter)
#logger对象可以添加多个fh和ch对象
logger.addHandler(fh)
logger.addHandler(ch)

if __name__ == '__main__':
    logger.debug('logger debug message')
    logger.info('logger info message')
    logger.warning('logger warning message')
    logger.error('logger error message')
    logger.critical('logger critical message')