# -*- coding: utf-8 -*-

import aiohttp
import asyncio

from data import config
from bs4 import BeautifulSoup
from logzero import logger


async def is_have_new_ads() -> str | bool:
    async with aiohttp.ClientSession() as session:
        response = await session.get(config.OLX_URL)
        html_document = BeautifulSoup(await response.text(), "html.parser")

        ads_table = html_document.find("table", {"id" : "offers_table"})
        ads = ads_table.find("tr", {"class" : "wrap"})
        ads_link = ads.find("a", {"class" : "link"}).get("href")
        
        if ads_link not in config.WATCHED_ADS:
            config.WATCHED_ADS.append(ads_link)
            return ads_link
        
        else: 
            return False


async def start_worker_loop(bot, chat_id):
    while config.IS_RUN:
        exist_new_ads_link = await is_have_new_ads()
        
        if exist_new_ads_link:
            logger.info("Exist new ads")
            await bot.send_message(
                text=exist_new_ads_link,
                chat_id=chat_id,
            )
        else:
            logger.info("Not exist new ads")

        await asyncio.sleep(60)


async def stop_worker_loop():
    config.IS_RUN = False