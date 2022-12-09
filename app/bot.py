import os
import logging
from logging.handlers import RotatingFileHandler

from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
from app.pars_wb.constants import START_MESSAGE, LOG_DEBAG_START_MESSAGE, LOG_DEBAG_START_PARSER
from app.pars_wb.pars import get_product

load_dotenv()


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

try:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
except KeyError as error:
    logger.critical(f"Отсутствует обязательная переменная окружения: {error}!")
    quit()


bot = Bot(BOT_TOKEN)

dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    logger.info(LOG_DEBAG_START_MESSAGE)
    await message.answer(text=START_MESSAGE)


@dp.message_handler()
async def first_message(message: types.Message):
    """Обработчик команды /start"""
    logger.info(LOG_DEBAG_START_PARSER)
    message_text = message.text.split()[::-1]
    articul = message_text.pop()
    product = " ".join(message_text[::-1])
    await bot.send_message(
        chat_id=message.from_user.id,
        text=get_product(articul, product),
    )


if __name__ == "__main__":
    executor.start_polling(dp)
