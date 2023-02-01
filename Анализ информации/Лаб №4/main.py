import logging
from random import choice
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Command
from aiogram.types import Message
from config import TOKEN
from keyboards import *
from aiogram.utils import executor
from ParseCities import get_counttries


bot = Bot(TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)
logger = logging.getLogger(__name__)
countriest = list(get_counttries())
bot_answer = ''
user_answer = ''
used_countries = []

@dp.message_handler(Command(commands=["start"]))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Поиграем?", reply_markup=Start_keyboard())


@dp.callback_query_handler(cb.filter(action='cities'))
async def callback_reg(call: types.CallbackQuery, callback_data: dict):
    global STATE, countriest, bot_answer, used_countries
    STATE = 1
    countriest = list(get_counttries())
    bot_answer = choice(countriest)
    countriest.remove(bot_answer)
    used_countries.append(bot_answer)
    await call.message.answer(f'Я начну! \nПервая страна {bot_answer} \nТвой ход!')

@dp.message_handler()
async def message_handler(message: Message):
    global STATE, used_countries, user_answer, bot_answer
    if STATE == 1:
        if message.text.title().startswith(bot_answer[-1].upper()):
            if message.text.title() not in used_countries:
                if message.text.title() in countriest:
                    user_answer = message.text.title()
                    used_countries.append(user_answer)
                    countriest.remove(user_answer)
                    for i in countriest:
                        if i.startswith(user_answer[-1].upper()):
                            bot_answer = i
                            used_countries.append(i)
                            countriest.remove(bot_answer)
                            await message.answer(bot_answer)
                            break
                    else:
                        STATE = 0
                        await message.answer('Похоже, ты победил c:\nМолодец!')

                else:
                    await message.answer("Не похоже на страну!")
            else:
                await message.answer('Эта страна уже была!')
        else:
            await message.answer(f'Cтрана должна начинаться на \'{bot_answer[-1].lower()}\'')
    else:
        await message.answer('Напиши команду \'start\' чтобы начать игру!')

if __name__ == '__main__':
    STATE = 0
    executor.start_polling(dp)



'''async def Check():
    global STATE
    if STATE != 0:
        await bot.send_message('Останавливаем игру?', reply_markup=YesNo_keyboard())
'''
'''@dp.callback_query_handler(cb.filter(action='yes'))
async def callback_get(call: types.CallbackQuery, callback_data: dict):
    global STATE
    STATE = 0
    await call.message.answer('ОК:)')

@dp.callback_query_handler(cb.filter(action='no'))
async def callback_get(call: types.CallbackQuery, callback_data: dict):
    await call.message.answer('Тогда продолжаем c:')
'''