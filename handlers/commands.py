# -*- coding: utf-8 -*-

from aiogram import types
from loader import dp

from keyboards import inline


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        text="Привет, я готов к работе",
        reply_markup=inline.main(),
    )