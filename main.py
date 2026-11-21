import asyncio
import os
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID", "0"))

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "Assalomu alaykum! Kino botga xush kelibsiz.\n"
        "Kino olish uchun uning kodini (raqamini) yuboring. Masalan: 2"
    )


@dp.message(F.text)
async def send_movie(message: Message):
    code_text = message.text.strip()
    if not code_text.isdigit():
        await message.answer("Iltimos, kino kodini faqat raqamda yuboring.")
        return

    msg_id = int(code_text)
    try:
        await bot.copy_message(
            chat_id=message.chat.id,
            from_chat_id=CHANNEL_ID,
            message_id=msg_id,
        )
    except Exception:
        await message.answer("Bunday kodli kino topilmadi yoki vaqtincha mavjud emas.")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
