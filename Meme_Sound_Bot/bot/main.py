import asyncio
import  logging
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from bot.handler import router
import os

load_dotenv()
tok = os.getenv('token')
bot = Bot(token=tok)
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("exit")