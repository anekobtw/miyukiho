from aiogram import F, Router, types
from aiogram.filters.command import Command

import database
from utils.admin import ban
from utils.logging import log

router = Router()


@router.message(Command("ban"))
async def ban_cmd(message: types.Message):
    # Is admin?
    member = await message.chat.get_member(message.from_user.id)
    if not isinstance(member, (types.ChatMemberAdministrator, types.ChatMemberOwner)):
        return

    # Is the message a reply?
    reply = message.reply_to_message
    if not reply:
        await message.reply("❗ Пожалуйста, используйте команду в ответ на сообщение пользователя.")
        return

    # Is there enough arguments?
    try:
        _, *reason = message.text.split(" ")
    except ValueError:
        await message.reply("Недостаточно аргументов или в них есть ошибка.")
        return

    # Ban and log
    await ban(chat=message.chat, user_id=reply.from_user.id)

    database.insert_log(
        admin_id=message.from_user.id,
        user_id=reply.from_user.id,
        action="ban",
        reason=" ".join(reason),
    )

    text = f"""
<b>🚫 Новый бан!</b>

<b>Админ:</b> @{message.from_user.username}
<b>Пользователь:</b> @{reply.from_user.username}
<b>Причина:</b> {' '.join(reason)}
"""

    await log(text=text)

    await message.reply(f"✅ Пользователь @{reply.from_user.username} успешно забанен!")
