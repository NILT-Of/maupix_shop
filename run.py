import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from config import TOKEN

from dotenv import  load_dotenv

load_dotenv()

from user import handlers
from admin import handlers_admin



bot = Bot(os.getenv("TG_TOKEN"))
dp = Dispatcher()

async def main():
    dp.include_routers(handlers.router, handlers_admin.router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')