from aiogram import Router

from . import ban, mute, report, unban, events, info

router = Router()

router.include_router(events.router)
router.include_router(report.router)
router.include_router(mute.router)
router.include_router(ban.router)
router.include_router(unban.router)
router.include_router(info.router)
