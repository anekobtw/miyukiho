from aiogram import Bot
from dotenv import load_dotenv
import os
from aiogram.client.default import DefaultBotProperties

load_dotenv()

bot = Bot(token=os.getenv("TOKEN"), default=DefaultBotProperties(parse_mode="HTML"))


async def log(group_id: int, text: str):
    if group_id and text:
        await bot.send_message(chat_id=group_id, text=text)
