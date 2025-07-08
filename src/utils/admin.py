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
        until_date=datetime.now() + timedelta(duration),
    )

async def ban(chat: types.Chat, user_id: int, duration: str, revoke_messages: bool):
    if not chat or not user_id or not duration or not revoke_messages:
        return ValueError("Not enough arguments.")

    if duration:
        until = datetime.now() + timedelta(duration)
    else:
        until = None

    await chat.ban(
        user_id=user_id,
        until_date=until,
        revoke_messages=revoke_messages
    )
