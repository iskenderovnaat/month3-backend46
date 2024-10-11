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
                    url="https://dodopizza.kg/bishkek"
                ),
                types.InlineKeyboardButton(
                    text="Наш инстаграм",
                    url="https://www.instagram.com/dodopizzakg/profilecard/?igsh=eGY5NXg5a2ZvcWFn"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="Вопросы, Отзывы",
                    url="mailto:feedback@dodopizza.kg"
                )

            ],
            [
                types.InlineKeyboardButton(
                    text="О нас",
                    callback_data="aboutus"
                ),
                types.InlineKeyboardButton(
                    text="Наши контакты",
                    callback_data="phone"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="Адреса ресторанов",
                    callback_data="location"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="Вакансии",
                    callback_data="vacancy"
                )
            ]
        ]
    )
    await message.reply(
        f"Доброго времени суток, {name}. Добро пожаловать в наш бот пиццерии",
        reply_markup=kb
    )


@start_router.callback_query(F.data == "aboutus")
async def about_us_handler(callback: types.CallbackQuery):
    text = "вкус на весь день."
    await callback.message.answer(text)


@start_router.callback_query(F.data == "phone")
async def phone_handler(callback: types.CallbackQuery):
    text = "Наши контакты:\n0(772) 550 550\n0(551) 550 590"
    await callback.message.answer(text)


@start_router.callback_query(F.data == "location")
async def location_handler(callback: types.CallbackQuery):
    text = "Адреса пиццерии:\n1. мкрн.6, 5/1\n2. пр-т Чуйский, 32Б\n3. пр-т Манаса, 7"
    await callback.message.answer(text)



@start_router.callback_query(F.data == "vacancy")
async def vacancy_handler(callback: types.CallbackQuery):
    text = "Вакансии:\n1. Кассир\n2. Курьер\n3. Оператор:\nОтклик на вакансию можно оставить по телефону: 0(312) 550 550"
    await callback.message.answer(text)