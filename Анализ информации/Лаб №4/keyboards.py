from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

cb = CallbackData('id','action')

#-- Keyboards --
def Start_keyboard():
    buttons = [
        InlineKeyboardButton(text="Страны", callback_data=cb.new(action='cities')),
    ]
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard

def YesNo_keyboard():
    buttons = [
        InlineKeyboardButton(text="Да", callback_data=cb.new(action='yes')),
        InlineKeyboardButton(text="Нет", callback_data=cb.new(action='no')),
    ]
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard