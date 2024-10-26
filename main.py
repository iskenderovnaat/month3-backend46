import asyncio
import logging

from handlers.start import start_router
from handlers.other_msgs import other_messages
from handlers.review_dialog import review_router
from handlers.adminadding_food import admin_Food_router
from handlers.dishes import catalog_router
from bot_config import bot, dp, database
from aiogram import Bot


async def on_startup():
    print("База данных создалась.")
    database.create_table()


async def main():
    dp.include_router(start_router)
    dp.include_router(review_router)

    dp.include_router(other_messages)

    dp.startup.register(on_startup)
    dp.include_router(admin_Food_router)
    dp.include_router(catalog_router)


    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())