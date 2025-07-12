from datetime import datetime

from aiogram import F, Router, types
from aiogram.filters import Command, CommandObject

from utils.admin import ban, mute, parse_time
from utils.logging import log

router = Router()


@router.message(F.reply_to_message, F.chat.type.in_({"group", "supergroup"}), Command("mute"))
async def mute_cmd(message: types.Message, command: CommandObject):
    admin = message.from_user
    user = message.reply_to_message.from_user

    # Is admin?
    if await message.chat.get_member(admin.id) not in await message.chat.get_administrators():
        await message.answer("⚠️ У тебя нет прав на использование этой команды.")
        return

    # Is there enough arguments?
    try:
        duration, *reason = command.args.split(" ")
        until = (datetime.now() + parse_time(duration)).strftime("%d %B %Y %H:%M:%S")
    except ValueError:
        await message.reply("⚠️ Недостаточно аргументов или в них есть ошибка.")
        return

    # Mute and log
    await mute(chat=message.chat, user_id=user.id, duration=duration)

    text = f"""
<b>🚫 Новый мут!</b>

<b>Админ:</b> @{admin.username}
<b>Пользователь:</b> @{user.username}
<b>До:</b> {until}
<b>Причина:</b> {' '.join(reason)}

<b>#mute #id{admin.id} #id{user.id}</b>
"""

    await log(text=text)
    await message.reply(f"✅ Пользователь @{user.username} успешно замучен до {until}!")


@router.message(F.reply_to_message, F.chat.type.in_({"group", "supergroup"}), Command("ban"))
async def mute_cmd(message: types.Message, command: CommandObject):
    admin = message.from_user
    user = message.reply_to_message.from_user

    # Is admin?
    if await message.chat.get_member(admin.id) not in await message.chat.get_administrators():
        await message.answer("⚠️ У тебя нет прав на использование этой команды.")
        return

    # Ban and log
    await ban(chat=message.chat, user_id=user.id)

    text = f"""
<b>🚫 Новый бан!</b>

<b>Админ:</b> @{admin.username}
<b>Пользователь:</b> @{user.username}
<b>Причина:</b> {command.args}

<b>#ban #id{admin.id} #id{user.id}</b>
"""

    await log(text=text)
    await message.reply(f"✅ Пользователь @{user.username} успешно забанен!")
