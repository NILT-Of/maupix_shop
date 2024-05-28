from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import ADMIN_ID

router = Router()

@router.message(CommandStart())
async def start_admin(message: Message):
    if message.from_user.id in ADMIN_ID:
        admin_panel_img = "https://ibb.co/ChKh0Dm"
        await message.answer_photo(admin_panel_img, caption=f'Привет *{message.from_user.first_name}* ✋\nДобро пожаловать в админ панель управления ботом.\nЗдесь ты можешь настроить функционал', parse_mode='Markdown')