from aiogram import Router,types
from aiogram.filters.command import Command

other_messages = Router()


@other_messages.message()
async def other_message(message:types.Message):
    # text = message.text
    await message.answer ("извините, я вас не понимаю")