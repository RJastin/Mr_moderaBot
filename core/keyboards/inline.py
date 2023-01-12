from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

select_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='My progect link',
            url='https://github.com/RJastin/Mr_moderaBot'
        )
    ],
    [
        InlineKeyboardButton(
            text='My developer profile',
            url='tg://user?id=807293900'
        )
    ],
])


def get_inline_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='My progect link', url='https://github.com/RJastin/Mr_moderaBot')
    keyboard_builder.button(text='My developer profile', url='tg://user?id=807293900')

    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup()


