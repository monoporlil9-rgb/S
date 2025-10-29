import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message


async def main():
    token = os.getenv("BOT_TOKEN", "").strip()
    if not token:
    
        raise RuntimeError("Please set BOT_TOKEN environment variable")

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    bot = Bot(token, parse_mode=ParseMode.HTML)
    dp = Dispatcher()

    @dp.message(CommandStart())
    async def on_start(message: Message):
        await message.answer("สวัสดีครับ! บอทรันแล้ว ✅\nใช้ /echo <ข้อความ> เพื่อลองทวนข้อความ")

    @dp.message(Command("echo"))
    async def on_echo(message: Message):
        args = message.text.split(maxsplit=1)
        text = args[1] if len(args) > 1 else ""
        if not text and message.reply_to_message:
            text = message.reply_to_message.text or message.reply_to_message.caption or ""
        await message.reply(text or "พิมพ์ข้อความต่อท้าย /echo หรือ reply ข้อความแล้วใช้ /echo")

    @dp.message(F.text)
    async def on_text(message: Message):
        await message.reply(f"รับทราบ: {message.text}")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
