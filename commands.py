from aiogram import Router, types
from aiogram.filters import CommandStart

from keyboards import web_app_btn

router = Router()

@router.message(CommandStart())
async def command_start(message: types.Message):
    await message.answer("Keling, boshlaymiz 🍟\n"
                            "Ajoyib tushlikka buyurtma berish uchun quyidagi tugmani bosing!", reply_markup=web_app_btn)