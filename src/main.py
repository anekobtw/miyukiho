import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

import admin
import database


async def run_bot() -> None:
    load_dotenv()
    logging.basicConfig(
        force=True,
        level=logging.INFO,
        format="%(levelname)s | %(message)s",
        datefmt="%H:%M:%S",
    )

    database.create_table()
    bot = Bot(token=os.getenv("TOKEN"), default=DefaultBotProperties(parse_mode="HTML"))
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    dp.include_router(admin.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(run_bot())
