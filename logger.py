import logging

FORMAT = "%(asctime)s|%(levelname)s|%(filename)s:%(lineno)s|%(message)s"
logging.basicConfig(level=logging.INFO, format=FORMAT)
logger = logging.getLogger('d2-helper')
