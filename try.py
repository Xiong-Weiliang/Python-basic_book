import logging
import logging.config
logging.config.fileConfig("logger.conf")   #声明读取配置文件的位置
logger=logging.getLogger('logger1')        # 从文件中读取数据的格式信息
logger.debug("这是debug信息")
logger.info("这是info信息")
logger.warning("这是Warning信息")
logger.error("这是ERROR信息")
logger.critical("这是Critical信息")
def funlog():
    logger.info('进入了funlog函数')         # TODO 运行错误？
logger.info('调用funlog函数')
funlog()
