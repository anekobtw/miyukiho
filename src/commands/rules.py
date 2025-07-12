from aiogram import F, Router, types
from aiogram.filters import Command

router = Router()


@router.message(Command("rules"))
async def rules_cmd(message: types.Message):
    await message.reply(
        """
<b>ПРАВИЛА ЧАТА</b>

<i>Если заметили нарушение — ответьте на сообщение командой /report.</i>

— Запрещён спам и флуд.
— Запрещён NSFW и шок-контент.
— Запрещены оскорбления.
— Запрещена политика.
— Запрещено неадекватное поведение.
— Запрещено распространение личной информации.
— Запрещена реклама
"""
    )
