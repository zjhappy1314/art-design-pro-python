import os
import logging
from logging.handlers import TimedRotatingFileHandler
from config import LOG_CONFIG


formatter = logging.Formatter(LOG_CONFIG.format)

LOG_DIR = 'logs'
os.makedirs(LOG_DIR, exist_ok=True)
log_path = os.path.join(LOG_DIR, LOG_CONFIG.file)
file_handler = TimedRotatingFileHandler(
    log_path, encoding='utf-8',
    # 每一天午夜保存一份新日志 
    when='midnight', interval=1
)
file_handler.suffix = '%Y-%m-%d'
file_handler.setLevel(LOG_CONFIG.level)
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setLevel(LOG_CONFIG.level)
console_handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.addHandler(file_handler)
logger.addHandler(console_handler)
logger.setLevel(LOG_CONFIG.level)
