import os

from aiogram import F, Router, types
from aiogram.filters.command import Command
from dotenv import load_dotenv

from utils.logging import log

load_dotenv()
router = Router()


@router.message(Command("report"))
async def report(message: types.Message):
    member = await message.chat.get_member(message.from_user.id)
    if not isinstance(member, (types.ChatMember)):
        return

    reply = message.reply_to_message
    if not reply:
        await message.reply("Пожалуйста, напишите команду ответом на сообщение.")
        return

    await log(
        group_id=os.getenv("LOGS_CHANNEL"),
        text=f"""
<b>❗ Новый репорт!</b>\n\n
<b>От кого:</b> @{message.from_user.username}\n
<b>На кого:</b> @{reply.from_user.username}\n
<b>Сообщение:</b> {reply.text}\n\n
<b><a href='https://t.me/c/{str(message.chat.id)[4:]}/{reply.message_id}'>Ссылка на сообщение</a></b>
""",
    )

    await message.reply("✅ Репорт успешно отправлен! Спасибо за помощь!")
