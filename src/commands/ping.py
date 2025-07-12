import time

import psutil
from aiogram import F, Router, types
from aiogram.filters import Command

router = Router()


@router.message(F.from_user.id == 1718021890, Command("ping"))
async def ping_cmd(message: types.Message):
    start = time.perf_counter()
    sent = await message.reply("<i>Проверка...</i>")
    latency = round((time.perf_counter() - start) * 1000)

    ram = psutil.virtual_memory()
    cpu = psutil.cpu_percent()
    disk = psutil.disk_usage("/")

    reply = (
        f"🏓 <b>Понг!</b>\n\n"
        f"<b>Задержка:</b> <i>{latency} мс</i>\n"
        f"<b>Процессор:</b> <i>{cpu}% загрузка</i>\n"
        f"<b>Оперативная память:</b> <i>{ram.used >> 20}MB / {ram.total >> 20}MB ({ram.percent}% занято)</i>\n"
        f"<b>Диск:</b> <i>{disk.used >> 30}GB / {disk.total >> 30}GB ({int(disk.percent)}% занято)</i>\n"
    )

    await sent.edit_text(reply)
