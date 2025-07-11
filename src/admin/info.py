from aiogram import F, Router, types
from aiogram.filters.command import Command

import database

router = Router()

ACTION_TRANSLATIONS = {"ban": "Бан", "unban": "Разбан", "mute": "Мут", "unmute": "Размут"}
ACTION_EMOJIS = {"ban": "⛔", "unban": "✅", "mute": "🔇", "unmute": "🔊"}


@router.message(Command("info"))
async def info_cmd(message: types.Message):
    reply = message.reply_to_message
    if not reply:
        await message.reply("❗ Пожалуйста, используйте команду в ответ на сообщение пользователя.")
        return

    logs = database.get_user(reply.from_user.id)
    if not logs:
        await message.reply("ℹ️ Нет записей для этого пользователя.")
        return

    text = f"<b>📄 История пользователя @{reply.from_user.username or reply.from_user.id}:</b>\n"
    for log in logs:
        emoji = ACTION_EMOJIS.get(log[3], "❔")
        translated = ACTION_TRANSLATIONS.get(log[3], log[3])

        text += (
            f"\n\n• <b>{translated}</b> {" — " + log[4] if log[4] else ""}\n"
            f"  🕒 {log[5].strftime("%d %B %Y")}   👮 <code>{log[1]}</code>"
        )

    await message.reply(text=text, parse_mode="HTML")
