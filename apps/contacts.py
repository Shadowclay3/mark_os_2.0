import json
from telebot import types
from datetime import datetime

def contacts():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    stroka_sostoyaniya = "⌚️ " +  current_time + "                   📳  📶  ✉️  89% 🔋" #🔋🪫 🔌
    # Читання файлу users_info.json
    with open('users_info.json', 'r') as file:
        data = json.load(file)
    keyboard = types.InlineKeyboardMarkup()
    button_1 = types.InlineKeyboardButton(text=" ", callback_data = ' ')
    button_2 = types.InlineKeyboardButton(text="⏹", callback_data = '⏹')
    button_3 = types.InlineKeyboardButton(text=" ", callback_data = ' ')
    # Виведення даних
    for user_id, user_info in data.items():
        first_name = user_info['first_name']
        user_id = user_info['user_id']
        button = types.InlineKeyboardButton(text=f"+{user_id} ( {first_name} )", callback_data=" ")
        keyboard.add(button)
    keyboard.add(button_1, button_2, button_3)
    text=stroka_sostoyaniya
    reply_markup=keyboard
    return text, reply_markup