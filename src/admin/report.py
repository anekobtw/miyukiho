from aiogram import F, Router, types
from aiogram.filters.command import Command

from utils.logging import log

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

    text = f"""
<b>❗ Новый репорт!</b>

<b>От кого:</b> @{message.from_user.username}
<b>На кого:</b> @{reply.from_user.username}
<b>Сообщение:</b> {reply.text}

<b><a href='https://t.me/c/{str(message.chat.id)[4:]}/{reply.message_id}'>Ссылка на сообщение</a></b>
"""

    await log(text=text)

    await message.reply("✅ Репорт успешно отправлен! Спасибо за помощь!")
