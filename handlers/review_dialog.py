from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


class RestourantReview(StatesGroup):
    name = State()
    phone_number = State()
    visit_date = State()
    food_rating = State()
    cleanliness_rating = State()
    extra_comments = State()


reviewdialog_router = Router()


@reviewdialog_router.callback_query(F.data == "feedback")
async def start_review(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(RestourantReview.name)
    await call.message.answer("Как вас зовут?")


@reviewdialog_router.message(RestourantReview.name)
async def review_name(message: types.Message, state: FSMContext):
    await message.answer("Введите ваш номер телефона")
    await state.set_state(RestourantReview.phone_number)


@reviewdialog_router.message(RestourantReview.phone_number)
async def review_phone_number(message: types.Message, state: FSMContext):
    await message.answer("Укажите дату вашего последнего визита (Д/М/Г)")
    await state.set_state(RestourantReview.visit_date)


@reviewdialog_router.message(RestourantReview.visit_date)
async def review_visit_date(message: types.Message, state: FSMContext):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Отлично"),
                types.KeyboardButton(text="Плохо"),
            ]
        ],
        resize_keyboard=True,
    )
    await message.answer("Как вы оцениваете блюда?", reply_markup=kb)
    await state.set_state(RestourantReview.food_rating)


@reviewdialog_router.message(RestourantReview.food_rating)
async def review_food_rating(message: types.Message, state: FSMContext):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Отлично"),
                types.KeyboardButton(text="Плохо"),
            ]
        ],
        resize_keyboard=True,
    )
    await message.answer("Оцените чистоту заведения", reply_markup=kb)
    await state.set_state(RestourantReview.cleanliness_rating)


@reviewdialog_router.message(RestourantReview.cleanliness_rating)
async def review_cleanliness_rating(message: types.Message, state: FSMContext):
    await message.answer("Оставьте ваши комментарии.", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(RestourantReview.extra_comments)


@reviewdialog_router.message(RestourantReview.extra_comments)
async def review_extra_comments(message: types.Message, state: FSMContext):
    await message.answer("Спасибо за ваш отзыв! Все этапы завершены.")
    await state.clear()