from datetime import datetime
from telebot import types
import json

def students():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    stroka_sostoyaniya = "⌚️ " +  current_time + "                   📳  📶  ✉️  89% 🔋" #🔋🪫 🔌
    reply_markup = types.InlineKeyboardMarkup()
    pustota = types.InlineKeyboardButton(text=" ", callback_data = ' ')

    list = types.InlineKeyboardButton(text="📜 Список", callback_data="students_list")
    top = types.InlineKeyboardButton(text="🔝 Топ", callback_data="students_top")
    groups = types.InlineKeyboardButton(text="👥 Группи", callback_data="students_groups")
    button_1 = types.InlineKeyboardButton(text=" ", callback_data = ' ')
    button_2 = types.InlineKeyboardButton(text="⏹", callback_data = "⏹")
    button_3 = types.InlineKeyboardButton(text=" ", callback_data = ' ')
    reply_markup.add(list)
    reply_markup.add(top)
    reply_markup.add(groups)
    reply_markup.add(pustota)
    reply_markup.add(pustota)
    reply_markup.add(pustota)
    reply_markup.add(pustota)
    reply_markup.add(pustota)
    reply_markup.add(pustota)
    reply_markup.add(pustota)
    reply_markup.add(button_1, button_2, button_3)
    text=stroka_sostoyaniya
    return text, reply_markup

def students_groups():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    stroka_sostoyaniya = "⌚️ " +  current_time + "                   📳  📶  ✉️  89% 🔋" #🔋🪫 🔌
    reply_markup = types.InlineKeyboardMarkup()
    pustota = types.InlineKeyboardButton(text=" ", callback_data = ' ')
    group1 = types.InlineKeyboardButton(text="Группа 1️⃣", callback_data="students_group1")
    group2 = types.InlineKeyboardButton(text="Группа 2️⃣", callback_data="students_group2")
    button_1 = types.InlineKeyboardButton(text="◀️", callback_data = 'students')
    button_2 = types.InlineKeyboardButton(text="⏹", callback_data = "⏹")
    button_3 = types.InlineKeyboardButton(text=" ", callback_data = ' ')
    reply_markup.add(group1)
    reply_markup.add(group2)
    reply_markup.add(pustota)
    reply_markup.add(pustota)
    reply_markup.add(pustota)
    reply_markup.add(pustota)
    reply_markup.add(pustota)
    reply_markup.add(pustota)
    reply_markup.add(pustota)
    reply_markup.add(pustota)
    reply_markup.add(button_1, button_2, button_3)
    text=stroka_sostoyaniya
    return text, reply_markup

def students_list():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    stroka_sostoyaniya = "⌚️ " +  current_time + "                   📳  📶  ✉️  89% 🔋" #🔋🪫 🔌
    with open("students.json", "r", encoding='utf-8') as file:
        json_data = json.load(file)
        students_list = types.InlineKeyboardMarkup()
        number = 1
        for student in json_data["students_list"]:
            numbers = str(number)
            new_numbers = numbers.replace("0", "0️⃣").replace("1", "1️⃣").replace("2", "2️⃣").replace("3", "3️⃣").replace("4", "4️⃣").replace("5", "5️⃣").replace("6", "6️⃣").replace("7", "7️⃣").replace("8", "8️⃣").replace("9", "9️⃣")
            name = new_numbers + student["name"]
            student = types.InlineKeyboardButton(text=str(name), callback_data=" ")
            students_list.add(student)
            number += 1
        button_1 = types.InlineKeyboardButton(text="◀️", callback_data = 'students')
        button_2 = types.InlineKeyboardButton(text="⏹", callback_data = "⏹")
        button_3 = types.InlineKeyboardButton(text=" ", callback_data = ' ')
        students_list.add(button_1, button_2, button_3)
    text=stroka_sostoyaniya
    reply_markup=students_list
    return text, reply_markup

def students_top():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    stroka_sostoyaniya = "⌚️ " +  current_time + "                   📳  📶  ✉️  89% 🔋" #🔋🪫 🔌
    with open("students.json", "r", encoding='utf-8') as file:
        json_data = json.load(file)
        students_list = types.InlineKeyboardMarkup()
        number = 1
        for student in json_data["students_top"]:
            numbers = str(number)
            if number < 4: new_numbers = numbers.replace("0", "0️⃣").replace("1", "🥇").replace("2", "🥈").replace("3", "🥉")
            else: new_numbers = numbers.replace("0", "0️⃣").replace("1", "1️⃣").replace("2", "2️⃣").replace("3", "3️⃣").replace("4", "4️⃣").replace("5", "5️⃣").replace("6", "6️⃣").replace("7", "7️⃣").replace("8", "8️⃣").replace("9", "9️⃣")
            name = new_numbers + student["name"]
            student = types.InlineKeyboardButton(text=str(name), callback_data=" ")
            students_list.add(student)
            number += 1
        button_1 = types.InlineKeyboardButton(text="◀️", callback_data = 'students')
        button_2 = types.InlineKeyboardButton(text="⏹", callback_data = "⏹")
        button_3 = types.InlineKeyboardButton(text=" ", callback_data = ' ')
        students_list.add(button_1, button_2, button_3)
    text=stroka_sostoyaniya
    reply_markup=students_list
    return text, reply_markup

def group1():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    stroka_sostoyaniya = "⌚️ " +  current_time + "                   📳  📶  ✉️  89% 🔋" #🔋🪫 🔌
    with open("students.json", "r", encoding='utf-8') as file:
        json_data = json.load(file)
        students_list = types.InlineKeyboardMarkup()
        number = 1
        for student in json_data["group1"]:
            numbers = str(number)
            new_numbers = numbers.replace("0", "0️⃣").replace("1", "1️⃣").replace("2", "2️⃣").replace("3", "3️⃣").replace("4", "4️⃣").replace("5", "5️⃣").replace("6", "6️⃣").replace("7", "7️⃣").replace("8", "8️⃣").replace("9", "9️⃣")
            name = new_numbers + student["name"]
            student = types.InlineKeyboardButton(text=str(name), callback_data=" ")
            students_list.add(student)
            number += 1
        button_1 = types.InlineKeyboardButton(text="◀️", callback_data = 'students_groups')
        button_2 = types.InlineKeyboardButton(text="⏹", callback_data = "⏹")
        button_3 = types.InlineKeyboardButton(text=" ", callback_data = ' ')
        students_list.add(button_1, button_2, button_3)
    text=stroka_sostoyaniya
    reply_markup=students_list
    return text, reply_markup


def group2():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    stroka_sostoyaniya = "⌚️ " +  current_time + "                   📳  📶  ✉️  89% 🔋" #🔋🪫 🔌
    with open("students.json", "r", encoding='utf-8') as file:
        json_data = json.load(file)
        students_list = types.InlineKeyboardMarkup()
        number = 1
        for student in json_data["group2"]:
            numbers = str(number)
            new_numbers = numbers.replace("0", "0️⃣").replace("1", "1️⃣").replace("2", "2️⃣").replace("3", "3️⃣").replace("4", "4️⃣").replace("5", "5️⃣").replace("6", "6️⃣").replace("7", "7️⃣").replace("8", "8️⃣").replace("9", "9️⃣")
            name = new_numbers + student["name"]
            student = types.InlineKeyboardButton(text=str(name), callback_data=" ")
            students_list.add(student)
            number += 1
        button_1 = types.InlineKeyboardButton(text="◀️", callback_data = 'students_groups')
        button_2 = types.InlineKeyboardButton(text="⏹", callback_data = "⏹")
        button_3 = types.InlineKeyboardButton(text=" ", callback_data = ' ')
        students_list.add(button_1, button_2, button_3)
    text=stroka_sostoyaniya
    reply_markup=students_list
    return text, reply_markup
