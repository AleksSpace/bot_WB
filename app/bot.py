import os
import logging

from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
from app.pars_wb.pars import get_product

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

logger = logging.getLogger(__name__)


@dp.message_handler()
async def first_message(message: types.Message):
    """Обработчик команды /start"""
    message_text = message.text.split()[::-1]
    articul = message_text.pop()
    product = " ".join(message_text[::-1])
    await bot.send_message(
        chat_id=message.from_user.id,
        text=get_product(articul, product),
    )


if __name__ == "__main__":
    executor.start_polling(dp)
