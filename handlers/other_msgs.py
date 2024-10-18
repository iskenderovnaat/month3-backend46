from aiogram import Router,types

other_messages = Router()


@other_messages.message()
async def other_message(message:types.Message):
    # text = message.text
    await message.answer ("извините, я вас не понима")