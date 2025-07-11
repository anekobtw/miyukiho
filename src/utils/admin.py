from datetime import datetime, timedelta

from aiogram import types


def parse_time(text: str) -> timedelta:
    num = int(text[:-1])
    unit = text[-1]

    if unit == "s":
        return timedelta(seconds=num)
    elif unit == "m":
        return timedelta(minutes=num)
    elif unit == "h":
        return timedelta(hours=num)
    elif unit == "d":
        return timedelta(days=num)
    else:
        raise ValueError(f"Unknown time unit: {unit}")


async def mute(chat: types.Chat, user_id: int, duration: str):
    if not chat or not user_id or not duration:
        return ValueError("Not enough arguments.")

    await chat.restrict(
        user_id=user_id,
        permissions=types.ChatPermissions(can_send_messages=False),
        until_date=datetime.now() + parse_time(duration),
    )


async def ban(chat: types.Chat, user_id: int):
    if not chat or not user_id:
        return ValueError("Not enough arguments.")

    await chat.ban(user_id=user_id, revoke_messages=True)


async def unban(chat: types.Chat, user_id: int):
    if not chat or not user_id:
        return ValueError("Not enough arguments.")

    await chat.unban(user_id=user_id, only_if_banned=True)
