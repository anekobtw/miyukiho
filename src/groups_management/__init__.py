from aiogram import Router

from . import create

router = Router()

router.include_router(create.router)
