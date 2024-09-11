import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command



logging.basicConfig(level=logging.INFO)

api = '123'
bot = Bot(token=api)
dp = Dispatcher()

@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')

@dp.message()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
