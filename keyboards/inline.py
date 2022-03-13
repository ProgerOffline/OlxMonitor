# -*- coding: utf-8 -*-

from aiogram import types
from loader import dp

from . import ctypes


def main():
    return types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(
            text="Начать парсинг",
            callback_data=ctypes.start.new(),
        )
    ).add(
        types.InlineKeyboardButton(
            text="Остановить парсинг",
            callback_data=ctypes.stop.new()
        ),
    )