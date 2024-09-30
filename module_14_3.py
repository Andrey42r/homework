import logging
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
import asyncio
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

logging.basicConfig(level=logging.INFO)

api = '7525137638:AAGNCa4raWBBcMe46slncTZ4BqzsDo8tKFk'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb1 = ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = KeyboardButton(text='Рассчитать')
button_2 = KeyboardButton(text='Информация')
button_3 = KeyboardButton(text='Купить')
kb1.add(button_1)
kb1.add(button_2)
kb1.add(button_3)

kb2 = InlineKeyboardMarkup()
button_3 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_4 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb2.add(button_3)
kb2.add(button_4)

kb3 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Продукт 1', callback_data='product_buying',),
            InlineKeyboardButton(text='Продукт 2', callback_data='product_buying'),
            InlineKeyboardButton(text='Продукт 3', callback_data='product_buying'),
            InlineKeyboardButton(text='Продукт 4', callback_data='product_buying')
        ]
    ]
)


class UserState(StatesGroup):
    age = State()  #возраст
    growth = State()  #рост
    weight = State()  #вес


@dp.message_handler(commands=['start'])
async def cmd_start(message):
    await message.answer('Добро пожаловать!', reply_markup=kb1)


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb2)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;'
                              '\nдля женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161.')
    await call.answer


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()
    await call.answer


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    result = 10 * int(data['weight']) + 6.25 * int(data['growth']) + 4.92 * int(data['age']) - 161
    await message.answer(f"Ваша норма калорий: {result}")

    await state.finish()


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    number_1 = 1
    await message.answer(f'Название: Продукт {number_1} | Описание: {number_1} | Цена: {number_1 * 100}')
    with open('files/Брокколи.jpg', "rb") as img:
        await message.answer_photo(img)
    number_2 = 2
    await message.answer(f'Название: Продукт {number_2} | Описание: {number_2} | Цена: {number_2 * 100}')
    with open('files/гречка.jpg', "rb") as img:
        await message.answer_photo(img)
    number_3 = 3
    await message.answer(f'Название: Продукт {number_3} | Описание: <{number_3} | Цена: {number_3 * 100}')
    with open('files/грудка.jpg', "rb") as img:
        await message.answer_photo(img)
    number_4 = 5
    await message.answer(f'Название: Продук {number_4} | Описание: {number_4} | Цена: {number_4 * 100}')
    with open('files/шпинат.jpg', "rb") as img:
        await message.answer_photo(img)
    await message.answer("Выберите продукт для покупки:", reply_markup=kb3)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
