# -*- coding: utf-8 -*-

from environs import Env

env = Env()
env.read_env()

WATCHED_ADS = []
IS_RUN = True

BOT_TOKEN = env.str("BOT_TOKEN")
OLX_URL = "https://www.olx.ua/nedvizhimost/lvov/?search%5Bfilter_float_price%3Afrom%5D=2000&search%5Bfilter_float_price%3Ato%5D=10000"