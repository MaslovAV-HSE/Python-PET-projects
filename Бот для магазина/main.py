import logging
from MongoDB import mongo
import re
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Command
from aiogram.types import Message
from config import TOKEN, Group_ID
from keyboards import *
from aiogram.utils import executor

bot = Bot(TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)
logger = logging.getLogger(__name__)
STATE = 0
msg_id = 0

def check_phone(phone:str):
    if "+" in phone: phone = phone.replace("+", '')
    if phone[0] == "8": phone = phone.replace('8', '7', 1)
    if len(phone) != 11: return False
    try:
        return int(phone)
    except:
        return False


@dp.message_handler(Command(commands=["start"]))
async def command_start_handler(message: Message) -> None:
    if message.chat.id in Group_ID:
        await message.answer("Выберите действие: ", reply_markup=Start_KeyBoard(), protect_content=True)
    else:
        print(message.chat.id)
        await message.answer('У вас нет доступа')

@dp.callback_query_handler(cb.filter(action='cancel'))
async def callback_cancel(call: types.CallbackQuery, callback_data: dict):
    global STATE
    if STATE != 0:
        STATE = 0
        await call.message.answer("Отменил операцию!")

@dp.callback_query_handler(cb.filter(action='registration'))
async def callback_reg(call: types.CallbackQuery, callback_data: dict):
    global STATE
    STATE = 1
    await call.message.answer(f"---<b>Регистрация</b>---\n"
                              f"Введите номер, фамилию, имя пользователя через пробел:\n"
                              f"<b>89999999999 Иванов Иван</b>")


@dp.callback_query_handler(cb.filter(action='get_points'))
async def callback_get(call: types.CallbackQuery, callback_data: dict):
    global STATE
    if call.message.chat.id in Group_ID:
        STATE = 2
        await call.message.answer(f"---<b>Узнать баллы</b>---\n"
                                  f"Введите номер пользователя:")


@dp.callback_query_handler(cb.filter(action='use_points'))
async def callback_use(call: types.CallbackQuery, callback_data: dict):
    global STATE
    if call.message.chat.id in Group_ID:
        STATE = 3
        await call.message.answer(f"---<b>Списать баллы</b>---\n"
                                  f"Введите номер, баллы для списания и текущую покупку пользователя через пробел:\n"
                                  f"<b>89999999999 500 1000</b>")


@dp.callback_query_handler(cb.filter(action='add_points'))
async def callback_add(call: types.CallbackQuery, callback_data: dict):
    global STATE
    if call.message.chat.id in Group_ID:
        STATE = 4
        await call.message.answer(f"---<b>Добавить баллы</b>---\n"
                                  f"Введите номер и текущую покупку пользователя через пробел:\n"
                                  f"<b>89999999999 1000</b>")


@dp.message_handler()
async def message_handler(message: Message):
    global STATE
    if STATE == 1:
        try:
            data = message.text.split()
            if len(data) != 3: raise Exception
            if check_phone(data[0]) == False: raise Exception
            else:
                result = db.insert_user(data[2], data[1], check_phone(data[0]))
                if result:
                    STATE = 0
                    await message.answer('Пользователь добавлен!')
                else:
                    STATE = 0
                    await message.answer('Пользователь уже существует!')

        except:
            await message.answer("Ошибка, повторите ввод!")
    elif STATE == 2:
        try:
            phone = check_phone(message.text)
            if phone == False: raise FileNotFoundError
            if db.user_exist(phone=phone):
                STATE = 0
                await message.answer(f"Пользователь: {phone}\n"
                                    f"Текущий баланс: {db.get_points(phone=phone)}")
            else:
                await message.answer('Номер не зарегестрирован в системе!')
        except:
            await message.answer("Не могу распознать номер, попробуйте еще раз!")
    elif STATE == 3:
        try:
            data = message.text.split()
            if len(data) != 3: raise Exception
            if check_phone(data[0]) == False:
                raise Exception
            else:
                result = db.use_points(float(check_phone(data[0])), float(data[1]), float(data[2]))
                if result:
                    STATE = 0
                    await message.answer('Баллы списаны!')
                else:
                    await message.answer('Ошибка добавления в базу, проверьте данные \n'
                                         f'Максимальные баллы для списания при покупке- {int(float(data[2]) * 0.45)}\n'
                                         f'Всего баллов у пользователя {db.get_points(check_phone(data[0]))}')
        except:
            await message.answer("Ошибка, повторите ввод!")

    elif STATE == 4:
        try:
            data = message.text.split()
            if len(data) != 2: raise Exception
            if check_phone(data[0]) == False: raise Exception
            else:
                result = db.add_purchase(float(check_phone(data[0])), float(data[1]))
                if result:
                    STATE = 0
                    await message.answer('Баллы добавлены!')
                else:
                    await message.answer('Ошибка добавления в базу, проверьте данные')
        except:
            await message.answer("Ошибка, повторите ввод!")
    else:
        pass



if __name__ == '__main__':
    db = mongo()
    executor.start_polling(dp)