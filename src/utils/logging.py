import os

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv("BOT_TOKEN"), default=DefaultBotProperties(parse_mode="HTML"))


async def log(text: str, disable_notification: bool = False):
    if text:
        await bot.send_message(chat_id=os.getenv("LOGS_CHANNEL"), text=text, disable_notification=disable_notification)
