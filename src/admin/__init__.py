from aiogram import Router

from . import ban, events, info, mute, report, rules

router = Router()

router.include_router(events.router)
router.include_router(report.router)
router.include_router(mute.router)
router.include_router(ban.router)
router.include_router(info.router)
router.include_router(rules.router)
