import asyncio
import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

# === ТОКЕН БУДЕМ БРАТЬ ИЗ ПЕРЕМЕННОЙ ОКРУЖЕНИЯ ===
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN не задан! Укажи его в переменных окружения Render.")

# === ССЫЛКА НА ФРОНТ (Vercel) ===
FRONT_URL = "https://luchwallet-frontend.vercel.app/?v=2"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# === КЛАВИАТУРА С WEBAPP-КНОПКОЙ ===
wallet_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Открыть кошелёк сотрудника",
                web_app=WebAppInfo(url=FRONT_URL)
            )
        ]
    ]
)


@dp.message(F.text == "/start")
async def start(message: types.Message):
    await message.answer(
        "Добро пожаловать!\n\nНажмите кнопку ниже, чтобы открыть кошелёк сотрудника.",
        reply_markup=wallet_keyboard
    )


@dp.message()
async def any_message(message: types.Message):
    await message.answer(
        "Нажмите кнопку ниже, чтобы открыть кошелёк.",
        reply_markup=wallet_keyboard
    )


async def main():
    print("Bot is running on Render...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
