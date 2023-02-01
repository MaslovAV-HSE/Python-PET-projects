from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData



cb = CallbackData('id','action')


btn_tek = InlineKeyboardButton(text="Текущая погода", callback_data=cb.new(action='current'))
btn_week = InlineKeyboardButton(text="Прогноз на неделю", callback_data=cb.new(action='week'))
btn_sub = InlineKeyboardButton(text="Подписка на прогноз", callback_data=cb.new(action='subscribe'))
#-- Keyboards --
def Start_keyboard(sub):
    if sub:
        btn_sub.text = 'Отменить подписку'
    else:
        btn_sub.text = "Подписка на прогноз"
    buttons = [
        btn_tek,
        btn_week,
        btn_sub
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