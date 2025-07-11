from aiogram import Router

from . import ban, mute, report, unban

router = Router()

router.include_router(report.router)
router.include_router(mute.router)
router.include_router(ban.router)
router.include_router(unban.router)
