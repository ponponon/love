from loguru import logger
from mark import BASE_DIR

logger.add(BASE_DIR/'logs'/'run.log', serialize='json',
           rotation='100 MB', retention=1)
