
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from dotenv import dotenv_values
import random
import logging

token = dotenv_values(".env")['BOT_TOKEN']
bot = Bot(token=token)
dp = Dispatcher()


@dp.message(Command(commands=['start']))
async def start_handler(message):
    name = message.from_user.first_name
    await message.answer(f"Добро  пожаловать {name} на бот geeksback,этот бот был создан для изучения создавания ботов!")



@dp.message(Command(commands=['myinfo']))
async def myinfo_handler(message):
    name = message.from_user.first_name
    await message.answer(f'Ваше имя: {name}\nВаш id: {message.from_user.id}\nВаш username: {message.from_user.username}')

@dp.message(Command(commands=['random']))
async def random_handler(message):
    await message.answer(random.choice(["Тынара", "Ангелина", "Диана", "Аяна", "Люба", "Асэма"]))

@dp.message()
async def echo_handler(message):
    text = message.text
    await message.answer(text)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
