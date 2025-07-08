from aiogram import Router

from . import mute, report

router = Router()

router.include_router(report.router)
router.include_router(mute.router)
