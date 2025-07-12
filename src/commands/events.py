import random
import time
from collections import defaultdict

from aiogram import F, Router, types

from utils.admin import mute
from utils.logging import log

router = Router()

user_msgs = defaultdict(list)
MAX_MESSAGES = 5
INTERVAL = 10  # seconds

ANTISPAM_TEMPLATE = """
{emoji} <b>Предупреждение об анти спаме! ({reason})</b>

<b>От:</b> @{username}
<b>Сообщение:</b> {message}

<b><a href='https://t.me/c/{chat_id}/{message_id}'>Ссылка на сообщение</a></b>

<b>#spam #id{user_id}</b>
"""


def format_antispam(reason: str, emoji: str, message: types.Message) -> str:
    return ANTISPAM_TEMPLATE.format(
        reason=reason,
        emoji=emoji,
        username=message.from_user.username,
        message=message.text,
        chat_id=str(message.chat.id)[4:],
        message_id=message.message_id,
        user_id=message.from_user.id,
    )


@router.message()
async def message_handler(message: types.Message):
    user_id = message.from_user.id
    now = time.time()

    # --- Anti-spam (message length)
    if message.text:
        msg_len = len(message.text)
        if msg_len >= 150:
            await log(format_antispam("Слишком много символов", "🔴" if msg_len >= 250 else "🟡", message), True)

    # --- Anti-flood (message frequency)
    user_msgs[user_id] = [t for t in user_msgs[user_id] if now - t < INTERVAL]
    user_msgs[user_id].append(now)

    if len(user_msgs[user_id]) > MAX_MESSAGES:
        await message.reply("⚠️ Не спамь!")
        await log(format_antispam("Спам", "🔴", message))
        await mute(message.chat, user_id, "1m")

    # --- 8ball
    if message.text.startswith("@" + (await message.bot.get_me()).username):
        EIGHTBALL_ANSWERS = [
            "Да.",
            "Нет.",
            "Возможно.",
            "Скорее всего.",
            "Спроси позже.",
            "Точно нет.",
            "Без сомнений.",
            "Определённо да.",
            "Не думаю.",
            "Шансы малы.",
            "Конечно!",
            "Хаха, нет.",
            "Слишком туманно...",
            "Лучше не знать.",
        ]

        await message.reply(f"🎱 {random.choice(EIGHTBALL_ANSWERS)}")
