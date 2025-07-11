from datetime import datetime

from aiogram import F, Router, types
from aiogram.filters.command import Command

from utils.admin import mute, parse_time, ban
from utils.logging import log

router = Router()


@router.message(F.reply_to_message, F.chat.type.in_({"group", "supergroup"}), Command("mute"))
async def mute_cmd(message: types.Message):
    # Is admin?
    member = await message.chat.get_member(message.from_user.id)
    if not isinstance(member, (types.ChatMemberAdministrator, types.ChatMemberOwner)):
        return

    # Is there enough arguments?
    try:
        _, duration, *reason = message.text.split(" ")
    except ValueError:
        await message.reply("⚠️ Недостаточно аргументов или в них есть ошибка.")
        return

    # Mute and log
    until = (datetime.now() + parse_time(duration)).strftime("%d %B %Y %H:%M:%S")
    await mute(chat=message.chat, user_id=message.reply_to_message.from_user.id, duration=duration)

    text = f"""
<b>🚫 Новый мут!</b>

<b>Админ:</b> @{message.from_user.username}
<b>Пользователь:</b> @{message.reply_to_message.from_user.username}
<b>До:</b> {until}
<b>Причина:</b> {' '.join(reason)}
"""

    await log(text=text)

    await message.reply(f"✅ Пользователь @{message.reply_to_message.from_user.username} успешно замучен до {until}!")


@router.message(F.reply_to_message, F.chat.type.in_({"group", "supergroup"}), Command("ban"))
async def mute_cmd(message: types.Message):
    # Is admin?
    member = await message.chat.get_member(message.from_user.id)
    if not isinstance(member, (types.ChatMemberAdministrator, types.ChatMemberOwner)):
        return

    # Is there enough arguments?
    try:
        _, *reason = message.text.split(" ")
    except ValueError:
        await message.reply("⚠️ Недостаточно аргументов или в них есть ошибка.")
        return

    # Ban and log
    await ban(chat=message.chat, user_id=message.reply_to_message.from_user.id)

    text = f"""
<b>🚫 Новый бан!</b>

<b>Админ:</b> @{message.from_user.username}
<b>Пользователь:</b> @{reply.from_user.username}
<b>Причина:</b> {' '.join(reason)}
"""

    await log(text=text)

    await message.reply(f"✅ Пользователь @{message.reply_to_message.from_user.username} успешно забанен!")
