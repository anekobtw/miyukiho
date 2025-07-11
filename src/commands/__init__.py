from aiogram import Router

from . import admin, events, report, rules

router = Router()

router.include_router(admin.router)
router.include_router(events.router)
router.include_router(report.router)
router.include_router(rules.router)
