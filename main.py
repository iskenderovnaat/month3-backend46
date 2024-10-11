import asyncio
import logging
from bot_config import bot, dp
from handlers.start import start_router
from handlers.other_msgs import other_messages

async def main():
    dp.include_router(start_router)
    dp.include_router(other_messages)
    # запуск ботаp
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())