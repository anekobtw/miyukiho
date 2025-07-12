from aiogram import Router

from . import admin, events, ping, report, rules

router = Router()

router.include_router(admin.router)
router.include_router(events.router)
router.include_router(report.router)
router.include_router(rules.router)
router.include_router(ping.router)
