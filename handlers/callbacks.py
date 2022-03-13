# -*- coding: utf-8 -*-

from aiogram import types
from loader import dp, bot
from keyboards import ctypes

from utils import parser


@dp.callback_query_handler(ctypes.start.filter())
async def start_parsing(call: types.CallbackQuery):
    await call.answer()
    await parser.start_worker_loop(bot, call.message.chat.id)


@dp.callback_query_handler(ctypes.stop.filter())
async def stop_parsing(call: types.CallbackQuery):
    await call.answer()
    await parser.stop_worker_loop()