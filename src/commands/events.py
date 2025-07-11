from aiogram import F, Router, types

router = Router()


@router.channel_post()
async def channel_post_handler(channel_post: types.Message):
    pass
