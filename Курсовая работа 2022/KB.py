from aiogram import Bot, types
from aiogram.utils.callback_data import CallbackData

cb = CallbackData('id','action')
def Start_KeyBoard():
    buttons = [
        types.InlineKeyboardButton(text="Заполнить данные:", callback_data= cb.new(action = 'Start_1')),
        types.InlineKeyboardButton(text="Увидеть результат", callback_data= cb.new(action = 'Start_2')),
        types.InlineKeyboardButton(text="Закончить общение", callback_data= cb.new(action = 'Start_3'))
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    return keyboard

def Male():
    buttons = [
        types.InlineKeyboardButton(text="Мужской", callback_data=cb.new(action = "Male_m")),
        types.InlineKeyboardButton(text="Женский", callback_data=cb.new(action = "Male_f"))
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    return keyboard

def Blood():
    buttons = [
        types.InlineKeyboardButton(text="Первая", callback_data=cb.new(action = "Blood_1")),
        types.InlineKeyboardButton(text="Вторая", callback_data=cb.new(action = "Blood_2")),
        types.InlineKeyboardButton(text="Третья", callback_data=cb.new(action = "Blood_3")),
        types.InlineKeyboardButton(text="Четвёртая", callback_data=cb.new(action = "Blood_4"))
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    return keyboard

def R_Factor():
    buttons = [
        types.InlineKeyboardButton(text="Отрицательная", callback_data=cb.new(action = "R_1")),
        types.InlineKeyboardButton(text="Положительная", callback_data=cb.new(action = "R_2"))
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    return keyboard


#---------------------------------------------Life history------------------------------------------------

def Smoking():
    buttons = [
        types.InlineKeyboardButton(text="Курю", callback_data=cb.new(action = "Smoke_1")),
        types.InlineKeyboardButton(text="Не курю", callback_data=cb.new(action = "Smoke_2")),
        types.InlineKeyboardButton(text="Бросил после приступа", callback_data=cb.new(action = "Smoke_3")),
        types.InlineKeyboardButton(text="Бросил недавно", callback_data=cb.new(action = "Smoke_4"))
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    return keyboard

def Sport():
    buttons = [
        types.InlineKeyboardButton(text="Зарядка или спорт", callback_data=cb.new(action = "Sport_1")),
        types.InlineKeyboardButton(text="Не занимаюсь", callback_data=cb.new(action = "Sport_2"))
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    return keyboard

def ReletivesHurtedCardioSistem():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data=cb.new(action = "RHurtedCS_1")),
        types.InlineKeyboardButton(text="Нет", callback_data=cb.new(action = "RHurtedCS_2"))
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    return keyboard

def HipertonicalDesise():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data=cb.new(action = "Hipertonia_1")),
        types.InlineKeyboardButton(text="Нет", callback_data=cb.new(action = "Hipertonia_2"))
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    return keyboard

def HurtedCardioSistem():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data=cb.new(action = "HurtedCS_1")),
        types.InlineKeyboardButton(text="Нет", callback_data=cb.new(action = "HurtedCS_2"))
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    return keyboard

def Sugar():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data=cb.new(action = "Sugar_1")),
        types.InlineKeyboardButton(text="Нет", callback_data=cb.new(action = "Sugar_2"))
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    return keyboard


def BrainBloodCirculation():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data=cb.new(action = "BBC_1")),
        types.InlineKeyboardButton(text="Нет", callback_data=cb.new(action = "BBC_2"))
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    return keyboard

def VerificatedCardioDeffect():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data=cb.new(action = "Verificated_1")),
        types.InlineKeyboardButton(text="Нет", callback_data=cb.new(action = "Verificated_2"))
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    return keyboard

def CardioSurgery():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data=cb.new(action = "Surgery_1")),
        types.InlineKeyboardButton(text="Нет", callback_data=cb.new(action = "Surgery_2"))
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    return keyboard

def Varicoz():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data=cb.new(action = "Varicoz_1")),
        types.InlineKeyboardButton(text="Нет", callback_data=cb.new(action = "Varicoz_2"))
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    return keyboard

#------------------------------------------------AllProblems------------------------------------------------

def PainInLangth():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data=cb.new(action = "Pain_1")),
        types.InlineKeyboardButton(text="Нет", callback_data=cb.new(action = "Pain_2"))
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    return keyboard
#!!!!!!!!!!Add description

def Odishka():
    buttons = [
        types.InlineKeyboardButton(text="Нет", callback_data=cb.new(action = "Odishka_1")),
        types.InlineKeyboardButton(text="При физ. нагрузках", callback_data=cb.new(action = "Odishka_2")),
        types.InlineKeyboardButton(text="В покое", callback_data=cb.new(action = "Odishka_3"))
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    return keyboard


def NightBreathProblems():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data=cb.new(action = "BreathNight_1")),
        types.InlineKeyboardButton(text="Нет", callback_data=cb.new(action = "BreathNight_2"))
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    return keyboard

def HeartBeating():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data=cb.new(action = "HeartBeating_1")),
        types.InlineKeyboardButton(text="Нет", callback_data=cb.new(action = "HeartBeating_2"))
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    return keyboard

def ProblemsWithHeartBeating():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data=cb.new(action = "ProblemsHB_1")),
        types.InlineKeyboardButton(text="Нет", callback_data=cb.new(action = "ProblemsHB_2"))
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    return keyboard

def Oteki():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data=cb.new(action = "Oteki_1")),
        types.InlineKeyboardButton(text="Нет", callback_data=cb.new(action = "Oteki_2"))
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    return keyboard

def Golovokrujenia():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data=cb.new(action = "Golovokr_1")),
        types.InlineKeyboardButton(text="Нет", callback_data=cb.new(action = "Golovokr_2"))
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    return keyboard

def HeadAche():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data=cb.new(action = "HeadAche_1")),
        types.InlineKeyboardButton(text="Нет", callback_data=cb.new(action = "HeadAche_2"))
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    return keyboard

#------------------------------------------------Addition information--------------------------------------------------
def Localization():
    buttons = [
        types.InlineKeyboardButton(text="В области сердца", callback_data=cb.new(action = "Localization_1")),
        types.InlineKeyboardButton(text="Другие части грудной клетки", callback_data=cb.new(action = "Localization_2"))
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    return keyboard

def Pereodichnost():
    buttons = [
        types.InlineKeyboardButton(text="Постоянные", callback_data=cb.new(action = "Period_1")),
        types.InlineKeyboardButton(text="Приступообразные", callback_data=cb.new(action = "Period_2"))
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    return keyboard

def Haracter():
    buttons = [
        types.InlineKeyboardButton(text="Колящие, ноющие, режущие", callback_data=cb.new(action = "type_1")),
        types.InlineKeyboardButton(text="Давящие, сжимающие, жгучие", callback_data=cb.new(action = "type_2"))
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    return keyboard

def Provacation():
    buttons = [
        types.InlineKeyboardButton(text="Возникает при длительной неудобнаой позе", callback_data=cb.new(action = "Provacation_1")),
        types.InlineKeyboardButton(text="В покое", callback_data=cb.new(action = "Provacation_2")),
        types.InlineKeyboardButton(text="ПРи физической или эмоциональной нагрузке", callback_data=cb.new(action = "Provacation_3"))
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    return keyboard

def Symptomth():
    buttons = [
        types.InlineKeyboardButton(text="Отсутствуют", callback_data=cb.new(action = "Symptoms_1")),
        types.InlineKeyboardButton(text="Холодный пот, чувство страха, одышки, удушье", callback_data=cb.new(action = "Symptoms_2"))
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    return keyboard

def Sredstva():
    buttons = [
        types.InlineKeyboardButton(text="Не были приняты", callback_data=cb.new(action = "Sredstva_1")),
        types.InlineKeyboardButton(text="Принятие удобной позы, массаж грудной клетки", callback_data=cb.new(action = "Sredstva_2")),
        types.InlineKeyboardButton(text="Принятие валидола, корвалола", callback_data=cb.new(action = "Sredstva_3")),
        types.InlineKeyboardButton(text="Прекращение физической нагрузки, нитроглицерин", callback_data=cb.new(action = "Sredstva_4")),
        types.InlineKeyboardButton(text="Другие препараты", callback_data=cb.new(action = "Sredstva_5"))
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    return keyboard

def Speed():
    buttons = [
        types.InlineKeyboardButton(text="Не были приняты", callback_data=cb.new(action = "Speed_1")),
        types.InlineKeyboardButton(text="До 5 минут", callback_data=cb.new(action = "Speed_2")),
        types.InlineKeyboardButton(text="Более 5 минут", callback_data=cb.new(action = "Speed_3"))
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    return keyboard
