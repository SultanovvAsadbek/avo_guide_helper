from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


main = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Каталог", callback_data="catalog")],
        [
            InlineKeyboardButton(text="Корзина", callback_data="basket"),
            InlineKeyboardButton(text="Контакты", callback_data="contacts"),
        ],
    ]
)

settings = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="YouTube", url="https://www.youtube.com/")]
    ]
)

cars = ["Mercedez", "Tesla", "BMW"]


async def inline_cars():
    keyboard = InlineKeyboardBuilder()
    for car in cars:
        keyboard.add(InlineKeyboardButton(text=car, url="https://www.youtube.com/"))

    return keyboard.adjust(2).as_markup()
