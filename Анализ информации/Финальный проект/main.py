import logging
import aioschedule
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Command
from aiogram.types import Message
from config import TOKEN
from keyboards import *
from aiogram.utils import executor
from Database import mongo
from OWM import *

bot = Bot(TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)
logger = logging.getLogger(__name__)


@dp.message_handler(Command(commands=["start"]))
async def command_start_handler(message: Message) -> None:
    if not Mongo.user_exist(tid=message.chat.id):
        Mongo.insert_user(message.chat.id)
    await message.answer(f"Здравствуйте, {message.chat.first_name}!",
                         reply_markup=Start_keyboard(Mongo.get_subscribe(message.chat.id)))


@dp.callback_query_handler(cb.filter(action='current'))
async def callback_cancel(call: types.CallbackQuery, callback_data: dict):
    Mongo.change_state(call.message.chat.id, 1)
    await call.message.answer('Введите название города')


@dp.callback_query_handler(cb.filter(action='week'))
async def callback_reg(call: types.CallbackQuery, callback_data: dict):
    Mongo.change_state(call.message.chat.id, 2)
    await send_forecast()
    await call.message.answer('Введите название города')


@dp.callback_query_handler(cb.filter(action='subscribe'))
async def callback_get(call: types.CallbackQuery, callback_data: dict):
    if Mongo.get_subscribe(call.message.chat.id):
        Mongo.change_subscribe(call.message.chat.id, False)
        await call.message.answer('Подписка отменена')
    else:
        if Mongo.get_location(call.message.chat.id)[0] == "Null":
            Mongo.change_state(call.message.chat.id, 3)
            await call.message.answer('Введите название города')
        else:
            await call.message.answer('Подписка подключена')


@dp.message_handler()
async def message_handler(message: Message):
    if Mongo.get_state(message.chat.id) == 1:
        city = get_city(message.text)
        if len(city) != 0:
            res = get_current_weather(get_responce(city, 1))
            Mongo.change_state(message.chat.id, 0)
            await message.answer(f'Погода для города <b>{message.text}</b>\n'
                                 f'Температура: <b>{res[0]}</b>\n'
                                 f'Ощущается как: <b>{res[1]}</b>\n'
                                 f'<b>{res[2]}</b>')
        else:
            await message.answer('Не могу найти город :с')
    elif Mongo.get_state(message.chat.id) == 2:
        city = get_city(message.text)
        if len(city) != 0:
            res = get_week_forcast(get_responce(city))
            s = ''
            for i in res:
                s += f'<b>{i["date"]}</b>\n{i["temp"]}\t   {i["condition"]}\n'
            Mongo.change_state(message.chat.id, 0)
            await message.answer(f'Погода для города <b>{message.text}</b>\n'+ s)
        else:
            await message.answer('Не могу найти город :с')
    elif Mongo.get_state(message.chat.id) == 3:
        city = get_city(message.text)
        if len(city) != 0:
            Mongo.change_location(message.chat.id, (message.text, city[0], city[1]),
                                  get_city_utf(get_responce(get_city(message.text))))
            Mongo.change_subscribe(message.chat.id, True)
            Mongo.change_state(message.chat.id, 0)
            await message.answer('Подписка подключена!\n'
                                 'Буду отправлять прогноз на день в 8am')
        else:
            await message.answer('Не могу найти город :с')
    else:
        await message.answer('Выберите действие, открыть меню /start')


async def send_forecast():
    for user in Mongo.generate_subscribers_list():
        if time.localtime().tm_hour - 5 + int(user['utf']) == 14:
            try:
                res = get_current_weather(get_responce((user['location'][1], user['location'][2])))
                t = f'Погода для города <b>{user["location"][0]}</b>\n' \
                    f'Температура: <b>{res[0]}</b>\n' \
                    f'Ощущается как: <b>{res[1]}</b>\n' \
                    f'<b>{res[2]}</b>'
                await bot.send_message(chat_id=user['id'], text=t)
            except:
                pass
        else:
            pass


async def scheduler():
    aioschedule.every().hour.do(send_forecast)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def on_startup(x):
    asyncio.create_task(scheduler())


if __name__ == '__main__':
    Mongo = mongo()
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)


