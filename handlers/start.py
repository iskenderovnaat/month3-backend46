from aiogram import Router, F, types
from aiogram.types import Message, InlineKeyboardMarkup
from aiogram.filters.command import Command

start_router = Router()


@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="Наш сайт",
                    url="https://mypizza.kg/"
                ),
                types.InlineKeyboardButton(
                    text="Наш инстаграм",
                    url="https://www.instagram.com/mypizzakg/"
                )
            ],

            [
                types.InlineKeyboardButton(
                    text="О нас",
                    callback_data="about_us"
                ),
                types.InlineKeyboardButton(
                    text="Наши контакты",
                    callback_data="phone"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="Адреса империи пиццы",
                    callback_data="location"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="Вакансии",
                    callback_data="vacancies"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="Оставить отзыв",
                    callback_data="feedback"
                )
            ]
        ]
    )

    await message.reply(
        f"Приветствуем, {name}. Добро пожаловать в наш бот пиццерии",
        reply_markup=kb
    )


@start_router.callback_query(F.data == "about_us")
async def about_us_handler(callback: types.CallbackQuery):
    text = "Выбирайте пиццу на свой вкус! \
В «Империи Пиццы» есть все виды пиццы на любой вкус! Мы учитываем предпочтение каждого клиента"
    await callback.message.answer(text)


@start_router.callback_query(F.data == "phone")
async def phone_handler(callback: types.CallbackQuery):
    text = "Наши контакты:0(551) 510 707"
    await callback.message.answer(text)


@start_router.callback_query(F.data == "location")
async def location_handler(callback: types.CallbackQuery):
    text = "Адреса пиццерии:\n1. ул.Горького, 27, \n2. пр-т Чуйский,114\n3. ул.Исы Ахунбаева, 173/1"
    await callback.message.answer(text)

@start_router.callback_query(F.data == "vacancies")
async def vacancies_handler(callback: types.CallbackQuery):
        text = "ВОЗРАСТ:17-25,должность: кассир ,зп 20000с-30000с,по всем вопросам обращаться по этому номеру:0706897899"
        await callback.message.answer(text)