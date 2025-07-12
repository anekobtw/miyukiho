from aiogram import Router

from . import events

router = Router()

router.include_router(events.router)
