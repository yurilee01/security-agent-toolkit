import logging

logging.basicConfig(filename="my.log", level=logging.INFO, encoding="utf-8")
logging.info("시작")
logging.warning("주의")
logging.error("오류")
