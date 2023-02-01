from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import CallbackQuery
from aiogram.utils import executor
from aiogram.utils.callback_data import CallbackData

import Compile_Results
import Diagrams
import MakePDF
import Predictions
import config, KB, Person,NS_Connection
import time
import datetime



bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)
Current_User = Person.User(Person.Person, 1)

waitig_Start = True



@dp.message_handler(commands=['start'])
async def send_welcome(msg: types.Message):
    global Current_User
    global waitig_Start
    global  current, iters
    iterations = [int(x) for x in range(1, 30)]
    iters = iter(iterations)
    current = iters.__next__()
    if current == 1:
        waitig_Start = False
        Current_User = Person.User(Person.Person, msg.from_user.id)
        await msg.answer(f'Я виртуальный врач кардиолог.\nПриятно познакомиться, {msg.from_user.first_name}\n'
                               f'Пройдем обследование?', reply_markup =KB.Start_KeyBoard())

    print(Current_User.get_id(),Current_User.get_quiz())


@dp.message_handler()
async def messages(msg: types.Message):
    global current
    message = msg.text
    if current == 2:
        if Date_of_Birth(message):
            current = iters.__next__()
            await msg.answer(config.qustionary[1])
        else:
            await msg.answer('Некорректная дата...\nПоробуйте в таком формате: dd.mm.yyyy')
    elif current == 3:
        if User_Height(message):
            current = iters.__next__()
            await msg.answer(config.qustionary[2])
        else:
            await msg.answer('Некорректный рост...\nЭто вообще не похоже на число..')
    elif current == 4:
        if User_Weight(message):
            current = iters.__next__()
            await msg.answer(config.qustionary[3],reply_markup=KB.Male())
        else:
            await msg.answer('Некорректный вес...\nЭто вообще не похоже на число..')
    elif waitig_Start:
        await msg.answer('Напишите команду "/start", чтобы начать обследование!')

def Date_of_Birth(date:str):
    try:
        a = time.strptime(date,'%d.%m.%Y')
        q = Current_User.get_quiz()
        q['bd'] = date
        years = datetime.date.today().year - a.tm_year
        q['age'] = years
        Current_User.set_quiz(q)
        return True
    except ValueError:
        return False

def User_Height(hight:str):
    try:
        if hight.isdigit():
            q = Current_User.get_quiz()
            hight = int(hight)
            if hight > 210 or hight < 100:
                return False
            q['height'] = hight
            Current_User.set_quiz(q)
            return True
    except ValueError:
        return False


def User_Weight(weight:str):
    try:
        if weight.isdigit():
            q = Current_User.get_quiz()
            weight = int(weight)
            if weight < 35 or weight > 150:
                return False
            q['wight'] = int(weight)
            Current_User.set_quiz(q)
            return True
    except ValueError:
        return False


#-----------------------------------Make-Poll---------------------------------------------


@dp.callback_query_handler(KB.cb.filter(action=["Start_1", "Start_2", "Start_3"]))
async def callbacks_num_change_fab(call: types.CallbackQuery, callback_data: dict):
    action = callback_data["action"]
    global current
    if action == "Start_1":
        current = iters.__next__()
        await call.message.answer(config.qustionary[0])
    elif action == "Start_2":
        await call.answer('Проверяем данные...')
    elif action == "Start_3":
        await call.answer('')
    await call.answer()


@dp.callback_query_handler(KB.cb.filter(action=["Male_m", "Male_f"]))
async def callbacks_num_change_fab(call: types.CallbackQuery, callback_data: dict):
    global current
    if current == 5:
        current = iters.__next__()
        action = callback_data["action"]
        if action == "Male_m":
            q = Current_User.get_quiz()
            q['male'] = 3
            Current_User.set_quiz(q)
        elif action == "Male_f":
            q = Current_User.get_quiz()
            q['male'] = 4
            Current_User.set_quiz(q)
        await call.message.answer(config.qustionary[4], reply_markup=KB.Blood())
    await call.answer()

@dp.callback_query_handler(KB.cb.filter(action=["Blood_1", "Blood_2","Blood_3","Blood_4"]))
async def callbacks_num_change_fab(call: types.CallbackQuery, callback_data: dict):
    global current
    if current == 6:
        current = iters.__next__()
        action = callback_data["action"]
        if action == "Blood_1":
            q = Current_User.get_quiz()
            q['blood'] = 1
            Current_User.set_quiz(q)
        elif action == "Blood_2":
            q = Current_User.get_quiz()
            q['blood'] = 2
            Current_User.set_quiz(q)
        elif action == "Blood_3":
            q = Current_User.get_quiz()
            q['blood'] = 3
            Current_User.set_quiz(q)
        elif action == "Blood_4":
            q = Current_User.get_quiz()
            q['blood'] = 4
            Current_User.set_quiz(q)
        await call.message.answer(config.qustionary[5], reply_markup=KB.R_Factor())
    await call.answer()
    print(Current_User.get_quiz())


@dp.callback_query_handler(KB.cb.filter(action=["R_1", "R_2"]))
async def callbacks_num_change_fab(call: types.CallbackQuery, callback_data: dict):
    global current
    if current == 7:
        current = iters.__next__()
        action = callback_data["action"]
        if action == "R_1":
            q = Current_User.get_quiz()
            q['rfactor'] = 1
            Current_User.set_quiz(q)
        elif action == "R_2":
            q = Current_User.get_quiz()
            q['rfactor'] = 0
            Current_User.set_quiz(q)
        await call.message.answer(config.qustionary[6], reply_markup=KB.Smoking())
    await call.answer()

@dp.callback_query_handler(KB.cb.filter(action=["Smoke_1", "Smoke_2", "Smoke_3","Smoke_4"]))
async def callbacks_num_change_fab(call: types.CallbackQuery, callback_data: dict):
    global current
    if current == 8:
        current = iters.__next__()
        action = callback_data["action"]
        if action == "Smoke_1":
            q = Current_User.get_quiz()
            q['smoking'] = 1
            Current_User.set_quiz(q)
        elif action == "Smoke_2":
            q = Current_User.get_quiz()
            q['smoking'] = 0
            Current_User.set_quiz(q)
        elif action == "Smoke_3":
            q = Current_User.get_quiz()
            q['smoking'] = -1
            Current_User.set_quiz(q)
        elif action == "Smoke_4":
            q = Current_User.get_quiz()
            q['smoking'] = -1
            Current_User.set_quiz(q)

        await call.message.answer(config.qustionary[7], reply_markup=KB.Sport())
    await call.answer()

@dp.callback_query_handler(KB.cb.filter(action=["Sport_1", "Sport_2"]))
async def callbacks_num_change_fab(call: types.CallbackQuery, callback_data: dict):
    global current
    if current == 9:
        current = iters.__next__()
        action = callback_data["action"]
        if action == "Sport_1":
            q = Current_User.get_quiz()
            q['sport'] = 1
            Current_User.set_quiz(q)
        elif action == "Sport_1":
            q = Current_User.get_quiz()
            q['sport'] = 0
            Current_User.set_quiz(q)
        await call.message.answer(config.qustionary[8], reply_markup=KB.ReletivesHurtedCardioSistem())
    await call.answer()

@dp.callback_query_handler(KB.cb.filter(action=["RHurtedCS_1", "RHurtedCS_2"]))
async def callbacks_num_change_fab(call: types.CallbackQuery, callback_data: dict):
    global current
    if current == 10:
        current = iters.__next__()
        action = callback_data["action"]
        if action == "RHurtedCS_1":
            q = Current_User.get_quiz()
            q['reletives_cs_illness'] = 1
            Current_User.set_quiz(q)
        elif action == "RHurtedCS_2":
            q = Current_User.get_quiz()
            q['reletives_cs_illness'] = 0
            Current_User.set_quiz(q)
        await call.message.answer(config.qustionary[9], reply_markup=KB.HipertonicalDesise())
    await call.answer()

@dp.callback_query_handler(KB.cb.filter(action=["Hipertonia_1", "Hipertonia_2"]))
async def callbacks_num_change_fab(call: types.CallbackQuery, callback_data: dict):
    global current
    if current == 11:
        current = iters.__next__()
        action = callback_data["action"]
        if action == "Hipertonia_1":
            q = Current_User.get_quiz()
            q['hipertonia'] = 1
            Current_User.set_quiz(q)
        elif action == "Hipertonia_2":
            q = Current_User.get_quiz()
            q['hipertonia'] = 0
            Current_User.set_quiz(q)
        await call.message.answer(config.qustionary[10], reply_markup=KB.Sugar())
    await call.answer()

@dp.callback_query_handler(KB.cb.filter(action=["Sugar_1", "Sugar_2"]))
async def callbacks_num_change_fab(call: types.CallbackQuery, callback_data: dict):
    global current
    if current == 12:
        current = iters.__next__()
        action = callback_data["action"]
        if action == "Sugar_1":
            q = Current_User.get_quiz()
            q['sugar'] = 1
            Current_User.set_quiz(q)
        elif action == "Sugar_2":
            q = Current_User.get_quiz()
            q['sugar'] = 0
            Current_User.set_quiz(q)
        await call.message.answer(config.qustionary[11], reply_markup=KB.BrainBloodCirculation())
    await call.answer()

@dp.callback_query_handler(KB.cb.filter(action=["BBC_1", "BBC_2"]))
async def callbacks_num_change_fab(call: types.CallbackQuery, callback_data: dict):
    global current
    if current == 13:
        current = iters.__next__()
        action = callback_data["action"]
        if action == "BBC_1":
            q = Current_User.get_quiz()
            q['cerebrovascular_accident'] = 1
            Current_User.set_quiz(q)
        elif action == "BBC_2":
            q = Current_User.get_quiz()
            q['cerebrovascular_accident'] = 0
            Current_User.set_quiz(q)
        await call.message.answer(config.qustionary[12], reply_markup=KB.VerificatedCardioDeffect())
    await call.answer()

@dp.callback_query_handler(KB.cb.filter(action=["Verificated_1", "Verificated_2"]))
async def callbacks_num_change_fab(call: types.CallbackQuery, callback_data: dict):
    global current
    if current == 14:
        current = iters.__next__()
        action = callback_data["action"]
        if action == "Verificated_1":
            q = Current_User.get_quiz()
            q['vereficated_cs'] = 1
            Current_User.set_quiz(q)
        elif action == "Verificated_2":
            q = Current_User.get_quiz()
            q['vereficated_cs'] = 0
            Current_User.set_quiz(q)
        await call.message.answer(config.qustionary[13], reply_markup=KB.CardioSurgery())
    await call.answer()

@dp.callback_query_handler(KB.cb.filter(action=["Surgery_1", "Surgery_2"]))
async def callbacks_num_change_fab(call: types.CallbackQuery, callback_data: dict):
    global current
    if current == 15:
        current = iters.__next__()
        action = callback_data["action"]
        if action == "Surgery_1":
            q = Current_User.get_quiz()
            q['cardio_surgery'] = 1
            Current_User.set_quiz(q)
        elif action == "Surgery_2":
            q = Current_User.get_quiz()
            q['cardio_surgery'] = 0
            Current_User.set_quiz(q)
        await call.message.answer(config.qustionary[14], reply_markup=KB.Varicoz())
    await call.answer()

@dp.callback_query_handler(KB.cb.filter(action=["Varicoz_1", "Varicoz_2"]))
async def callbacks_num_change_fab(call: types.CallbackQuery, callback_data: dict):
    global current
    if current == 16:
        current = iters.__next__()
        action = callback_data["action"]
        if action == "Varicoz_1":
            q = Current_User.get_quiz()
            q['varicoz'] = 1
            Current_User.set_quiz(q)
        elif action == "Varicoz_2":
            q = Current_User.get_quiz()
            q['varicoz'] = 0
            Current_User.set_quiz(q)
        await call.message.answer(config.qustionary[15], reply_markup=KB.PainInLangth())
    await call.answer()

@dp.callback_query_handler(KB.cb.filter(action=["Pain_1", "Pain_2"]))
async def callbacks_num_change_fab(call: types.CallbackQuery, callback_data: dict):
    global current
    if current == 17:
        current = iters.__next__()
        action = callback_data["action"]
        if action == "Pain_1":
            q = Current_User.get_quiz()
            q['heart_pains'] = 0
            Current_User.set_quiz(q)
        elif action == "Pain_2":
            q = Current_User.get_quiz()
            q['heart_pains'] = 0
            Current_User.set_quiz(q)
        await call.message.answer(config.qustionary[16], reply_markup=KB.Odishka())
    await call.answer()

@dp.callback_query_handler(KB.cb.filter(action=["Odishka_1", "Odishka_2","Odishka_3"]))
async def callbacks_num_change_fab(call: types.CallbackQuery, callback_data: dict):
    global current
    if current == 18:
        current = iters.__next__()
        action = callback_data["action"]
        if action == "Odishka_1":
            q = Current_User.get_quiz()
            q['odishka'] = 1
            Current_User.set_quiz(q)
        elif action == "Odishka_2":
            q = Current_User.get_quiz()
            q['odishka'] = 0
            Current_User.set_quiz(q)
        elif action == "Odishka_3":
            q = Current_User.get_quiz()
            q['odishka'] = 0
            Current_User.set_quiz(q)
        await call.message.answer(config.qustionary[17], reply_markup=KB.NightBreathProblems())
    await call.answer()


@dp.callback_query_handler(KB.cb.filter(action=["BreathNight_1", "BreathNight_2"]))
async def callbacks_num_change_fab(call: types.CallbackQuery, callback_data: dict):
    global current
    if current == 19:
        current = iters.__next__()
        action = callback_data["action"]
        if action == "BreathNight_1":
            q = Current_User.get_quiz()
            q['breath_problems'] = 1
            Current_User.set_quiz(q)
        elif action == "BreathNight_2":
            q = Current_User.get_quiz()
            q['breath_problems'] = 0
            Current_User.set_quiz(q)
        await call.message.answer(config.qustionary[18], reply_markup=KB.HeartBeating())
    await call.answer()

@dp.callback_query_handler(KB.cb.filter(action=["HeartBeating_1", "HeartBeating_2"]))
async def callbacks_num_change_fab(call: types.CallbackQuery, callback_data: dict):
    global current
    if current == 20:
        current = iters.__next__()
        action = callback_data["action"]
        if action == "HeartBeating_1":
            q = Current_User.get_quiz()
            q['heart_rithm_problems'] = 1
            Current_User.set_quiz(q)
        elif action == "HeartBeating_2":
            q = Current_User.get_quiz()
            q['heart_rithm_problems'] = 0
            Current_User.set_quiz(q)
        await call.message.answer(config.qustionary[19], reply_markup=KB.ProblemsWithHeartBeating())
    await call.answer()

@dp.callback_query_handler(KB.cb.filter(action=["ProblemsHB_1", "ProblemsHB_2"]))
async def callbacks_num_change_fab(call: types.CallbackQuery, callback_data: dict):
    global current
    if current == 21:
        current = iters.__next__()
        action = callback_data["action"]
        if action == "ProblemsHB_1":
            q = Current_User.get_quiz()
            q['heart_problems'] = 1
            Current_User.set_quiz(q)
        elif action == "ProblemsHB_2":
            q = Current_User.get_quiz()
            q['heart_problems'] = 0
            Current_User.set_quiz(q)
        await call.message.answer(config.qustionary[20], reply_markup=KB.Oteki())
    await call.answer()


@dp.callback_query_handler(KB.cb.filter(action=["Oteki_1", "Oteki_2"]))
async def callbacks_num_change_fab(call: types.CallbackQuery, callback_data: dict):
    global current
    if current == 22:
        current = iters.__next__()
        action = callback_data["action"]
        if action == "Oteki_1":
            q = Current_User.get_quiz()
            q['oteki'] = 1
            Current_User.set_quiz(q)
        elif action == "Oteki_2":
            q = Current_User.get_quiz()
            q['oteki'] = 0
            Current_User.set_quiz(q)
        await call.message.answer(config.qustionary[21], reply_markup=KB.Golovokrujenia())
    await call.answer()

@dp.callback_query_handler(KB.cb.filter(action=["Golovokr_1", "Golovokr_2"]))
async def callbacks_num_change_fab(call: types.CallbackQuery, callback_data: dict):
    global current
    if current == 23:
        current = iters.__next__()
        action = callback_data["action"]
        if action == "Golovokr_1":
            q = Current_User.get_quiz()
            q['golovokrujenia'] = 1
            Current_User.set_quiz(q)
        elif action == "Golovokr_2":
            q = Current_User.get_quiz()
            q['golovokrujenia'] = 0
            Current_User.set_quiz(q)
        await call.message.answer(config.qustionary[22], reply_markup=KB.HeadAche())
    await call.answer()


@dp.callback_query_handler(KB.cb.filter(action=["HeadAche_1", "HeadAche_2"]))
async def callbacks_num_change_fab(call: types.CallbackQuery, callback_data: dict):
    global current
    if current == 24:
        current = iters.__next__()
        action = callback_data["action"]
        if action == "HeadAche_1":
            q = Current_User.get_quiz()
            q['head_ache'] = 1
            Current_User.set_quiz(q)
        elif action == "HeadAche_2":
            q = Current_User.get_quiz()
            q['head_ache'] = 0
            Current_User.set_quiz(q)
        prepared_data = Current_User.Compile()
        result = NS_Connection.Make_Request(prepared_data,Current_User.get_quiz()["bd"])
        msg, pic_name = Compile_Results.Results(result)

        media = types.MediaGroup()
        media.attach_photo(types.InputFile(pic_name))
        await call.message.answer_media_group(media=media)
        await call.message.answer(msg)

        result2, text = Predictions.MakePredictions(prepared_data)
        NS_Connection.Make_Request(result2, Current_User.get_quiz()["bd"])
        MakePDF.CreatePDF(text)

        media2 = types.MediaGroup()
        media2.attach_document(types.InputFile("results.pdf"))
        msg = "Результаты предсказаний находятся в PDF файле"
        await call.message.answer_media_group(media=media2)
        await call.message.answer(msg)

    await call.answer()




if __name__ == '__main__':
   executor.start_polling(dp)