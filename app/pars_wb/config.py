import logging
from logging.handlers import RotatingFileHandler


logging.basicConfig(
    level=logging.INFO,
    filename="app.log",
    filemode="w",
    format="%(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = RotatingFileHandler("app.log", maxBytes=50000000, backupCount=5)
logger.addHandler(handler)