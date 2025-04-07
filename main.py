import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from config import TOKEN
from handlers import register_handlers

async def main():
    bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    register_handlers(dp)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())