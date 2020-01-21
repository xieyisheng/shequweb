import logging
import logging.config
import sys

#sys.setrecursionlimit(1000000)
logconfpath='../config/log.conf'
logging.config.fileConfig(logconfpath)
logger=logging.getLogger()

def debug(message):
    logger.debug(message)

def info(message):
    logger.info(message)

def warning(message):
    logger.warning(message)

def error(message):
    logger.error(message)

if __name__=='__main__':

    info("zheshi一条debug")
    warning('这是一条警告')
    error('zheshi一个错误')

