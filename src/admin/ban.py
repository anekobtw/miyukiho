import os

from aiogram import F, Router, types
from aiogram.filters.command import Command
from dotenv import load_dotenv

from utils.admin import mute
from utils.logging import log

load_dotenv()
router = Router()


@router.message(Command("ban"))
async def mute_cmd(message: types.Message):
    # Is admin?
    member = await message.chat.get_member(message.from_user.id)
    if not isinstance(member, (types.ChatMemberOwner, types.ChatMemberAdministrator)):
        return

    # Is the message a reply?
    reply = message.reply_to_message
    if not reply:
        await message.reply("Пожалуйста, напишите команду ответом на сообщение.")
        return

    # Is there enough arguments?
    try:
        _, duration, *reason = message.text.split(" ")
    except ValueError:
        await message.reply("Недостаточно аргументов или в них есть ошибка.")
        return

    # Mute and log
    await mute(chat=message.chat, user_id=reply.from_user.id, duration=duration)
    
    await log(
        group_id=os.getenv("LOGS_CHANNEL"),
        text=f"<b>🚫 Новый мут!</b>\n\n<b>Админ:</b> @{message.from_user.username}\n<b>Пользователь:</b> @{reply.from_user.username}\n<b>До:</b> {until.strftime("%d %B %Y %H:%M:%S")}\n<b>Причина:</b> {' '.join(reason)}",
    )
    
    await message.reply(f"✅ Пользователь @{reply.from_user.username} успешно замучен!")

