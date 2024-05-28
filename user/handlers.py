from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from admin.handlers_admin import start_admin


from config import ADMIN_ID

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    if message.from_user.id not in ADMIN_ID:
        user_catalog_img = "https://ibb.co/z5zwG7F"
        await message.answer_photo(user_catalog_img, caption=f'Привет *{message.from_user.first_name}* ✋\nВыбери язык', parse_mode='Markdown')
    else:
        await start_admin(message)
