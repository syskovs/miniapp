import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import TOKEN

def main_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text="Main Page", web_app=WebAppInfo(url='https://docs.medsync.botfather.dev/backend/'))
    return builder.as_markup()

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.reply('Привет', reply_markup=main_menu())

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')