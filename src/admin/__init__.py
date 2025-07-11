from aiogram import Router

from . import mute, report, ban

router = Router()

router.include_router(report.router)
router.include_router(mute.router)
router.include_router(ban.router)
