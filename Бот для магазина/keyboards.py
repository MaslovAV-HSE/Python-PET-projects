from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

cb = CallbackData('id','action')

#-- Keyboards --
def Start_KeyBoard():
    buttons = [
        InlineKeyboardButton(text="Зарегестрировать пользователя", callback_data=cb.new(action='registration')),
        InlineKeyboardButton(text="Узнать баллы", callback_data=cb.new(action='get_points')),
        InlineKeyboardButton(text="Списать баллы", callback_data=cb.new(action='use_points')),
        InlineKeyboardButton(text="Добавить баллы", callback_data=cb.new(action='add_points')),
        InlineKeyboardButton(text="Отмена", callback_data=cb.new(action='cancel'))
    ]
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard