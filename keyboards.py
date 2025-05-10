from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

web_app = WebAppInfo(url="https://abubakir-afk.github.io/p2_web_app.github.io/")
web_app_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Buyurtma qiling", web_app=web_app)]
])