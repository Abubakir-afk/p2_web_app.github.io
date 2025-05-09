from aiogram import Router, types
from aiogram.filters import CommandStart

from keyboards import web_app_btn

router = Router()

@router.message(CommandStart())
async def command_start(message: types.Message):
    await message.answer("Web App loyihamizga xush kelibsiz!", reply_markup=web_app_btn)