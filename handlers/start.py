from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from bot_config import database

start_router = Router()
list_of_clients = []
list_tg_ids = []

@start_router.message(Command(commands=['start']))
async def start_handler(message: types.Message):
    name = message.from_user.first_name

    user_summ = database.fetch("SELECT DISTINCT user_id FROM users_id")
    summ = len(user_summ)

    await message.answer(f"Доброго времени суток {name}.\n"
                         f"На данный момент в боте зарегистрировано {summ} пользователей")

    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Наш сайт", url="https://mypizza.kg/ru/mypizza/menu/4376"),
                types.InlineKeyboardButton(text="Наш инстаграм", url="https://www.instagram.com/mypizzakg/")
            ],
            [
                types.InlineKeyboardButton(text="О нас", callback_data="about_us")
            ],
            [
                types.InlineKeyboardButton(text="Наш адрес", url="https://2gis.kg/bishkek/branches/70000001019359418")
            ],
            [
                types.InlineKeyboardButton(text="Вакансии", callback_data="vacancies")
            ],
            [
                types.InlineKeyboardButton(text="Оставить отзыв", callback_data="review")
            ]
        ]
    )

    await message.answer(f"Приветствуем, {name}, в бот пиццерии! Этот бот был создан для вашего удобства.",
                         reply_markup=keyboard)


@start_router.callback_query(F.data == "about_us")
async def about_us_handler(callback: types.CallbackQuery):
    text = "Выбирайте пиццу на свой вкус! В «Империи Пиццы» есть все виды пиццы на любой вкус! Мы учитываем предпочтение каждого клиента"
    await callback.message.answer(text)


@start_router.callback_query(F.data == "vacancies")
async def vacancies_handler(callback: types.CallbackQuery):
    text = ("Возраст - от 18 до 23 лет.\nЗарплата - от 30000р до 40000р.\nДолжность - кассир.\n"
            "Телефон - +996 709819018.")
    await callback.message.answer(text)