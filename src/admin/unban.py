import os

from aiogram import F, Router, types
from aiogram.filters.command import Command
from dotenv import load_dotenv

import database
from utils.admin import unban
from utils.logging import log

load_dotenv()
router = Router()


@router.message(Command("unban"))
async def unban_cmd(message: types.Message):
    # Is admin?
    member = await message.chat.get_member(message.from_user.id)
    if not isinstance(member, (types.ChatMemberAdministrator, types.ChatMemberOwner)):
        return

    # Is the message a reply?
    reply = message.reply_to_message
    if not reply:
        await message.reply("Пожалуйста, напишите команду ответом на сообщение.")
        return

    # Ban and log
    await unban(chat=message.chat, user_id=reply.from_user.id)

    database.insert_log(
        admin_id=message.from_user.id,
        user_id=reply.from_user.id,
        action="unban",
        reason="",
    )

    await log(
        group_id=os.getenv("LOGS_CHANNEL"),
        text=f"<b>✅ Разбан!</b>\n\n<b>Админ:</b> @{message.from_user.username}\n<b>Пользователь:</b> @{reply.from_user.username}",
    )

    await message.reply(f"✅ Пользователь @{reply.from_user.username} успешно разбанен!")
