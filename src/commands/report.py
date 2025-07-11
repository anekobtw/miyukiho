from aiogram import F, Router, types
from aiogram.filters.command import Command

from utils.logging import log

router = Router()


@router.message(F.reply_to_message, F.chat.type.in_({"group", "supergroup"}), Command("report"))
async def report_cmd(message: types.Message):
    member = await message.chat.get_member(message.from_user.id)
    if not isinstance(member, (types.ChatMember)):
        return

    text = f"""
<b>❗ Новый репорт!</b>

<b>От кого:</b> @{message.from_user.username}
<b>На кого:</b> @{message.reply_to_message.from_user.username}
<b>Сообщение:</b> {message.reply_to_message.text}

<b><a href='https://t.me/c/{str(message.chat.id)[4:]}/{message.reply_to_message.message_id}'>Ссылка на сообщение</a></b>

<b>#report #id{message.from_user.id} #id{message.reply_to_message.from_user.id}</b>
"""

    await log(text=text)

    await message.reply("✅ Репорт успешно отправлен! Спасибо за помощь!")
