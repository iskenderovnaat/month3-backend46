from aiogram import F, Router, types
from aiogram.filters import Command

from bot_config import database

catalog_router = Router()

@catalog_router.message(Command("catalog"))
async def show_all_dishes(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Супы"),
                types.KeyboardButton(text="Вторые"),
            ],
            [
                types.KeyboardButton(text="Горячие напитки"),
                types.KeyboardButton(text="Холодные напитки"),
                types.KeyboardButton(text="Гарниры")
            ]
        ],
        resize_keyboard=True,
        input_field_placeholder="Выберите пожалуйста категорию"
    )
    await message.answer("Выберите категорию блюда", reply_markup=kb)

categories = ("Супы", "Вторые", "Гарниры", "Холодные напитки", "Горячие напитки")

@catalog_router.message(F.text.in_(categories))
async def show_dishes_by_category(message: types.Message):
    category = message.text
    print(category)
    dishes = database.fetch("SELECT * FROM dishes WHERE category = ?", (category,))

    if dishes:
        await message.answer(" Все блюда в категории " + category + ":\n")
        for dish in dishes:
            msg = f"Название: {dish['name_of_Food']}\nЦена: {dish['price']} с."
            await message.answer(msg)
    else:
        await message.answer(f"В категории '{category}' пока нет блюд.")