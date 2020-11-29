import logging
import time
import os
def log_func():
    timestap = time.strftime("%Y-%m-%d",time.localtime())
    logdir = "/var/log/python-" +timestap 
    if not os.path.exists(logdir):
        os.mkdir(logdir)
    logging.basicConfig(filename=logdir+os.sep+"first-test.log",
                        level=logging.DEBUG,
                        datefmt="%Y-%m-%d %H:%M:%S",
                        format="%(asctime)s %(name)-8s %(levelname)-10s [line: %(lineno)d] %(message)s")
    logging.debug("this is a debug log....")
    logging.info("this is a info log....")
    logging.warning("this is a warning log....")
    logging.error("this is a error log....")
    logging.critical("this is a critical log....")

if __name__=='__main__':
    log_func()