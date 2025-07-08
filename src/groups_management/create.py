from aiogram import F, types, Router
from aiogram.filters.command import Command


router = Router()


@router.message(Command("add_group"))
async def add_group_handler(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[[types.KeyboardButton(text="📁 Выбрать группу", request_chat=types.KeyboardButtonRequestChat(request_id=1, chat_is_channel=False, text="test"))]],
        one_time_keyboard=True
    )
    await message.answer("Выберите группу для подключения:", reply_markup=kb)


# TODO: FIX IT
@router.message(F.chat_shared)
async def chat_shared_handler(message: types.Message):
    if message. .chat_id:
        chat_id = chat_shared.chat_id
        await message.answer(f"Chat shared! Chat ID: {chat_id}, Request ID: {request_id}")
        # You can now use chat_id to interact with the shared chat
    elif message.chat_shared.user_id:
        user_id = chat_shared.user_id
        await message.answer(f"User shared a chat! User ID: {user_id}, Request ID: {request_id}")
        # You can now use user_id to interact with the user who shared the chat.
