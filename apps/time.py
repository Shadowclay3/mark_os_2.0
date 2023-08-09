from datetime import datetime
from telebot import types

def time():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    stroka_sostoyaniya = "⌚️ " +  current_time + "                   📳  📶  ✉️  89% 🔋" #🔋🪫 🔌
    time = types.InlineKeyboardMarkup()
    pustota = types.InlineKeyboardButton(text=" ", callback_data = ' ')

    time_0 = types.InlineKeyboardButton(text="🕑 час", callback_data = ' ')
    time_1 = types.InlineKeyboardButton(text="1. 9:00  - 10:20", callback_data = ' ')
    time_2 = types.InlineKeyboardButton(text="2. 10:40 - 12:00", callback_data = ' ')
    time_3 = types.InlineKeyboardButton(text="3. 12:30 - 13:50", callback_data = ' ')
    time_4 = types.InlineKeyboardButton(text="4. 14:10 - 15:30", callback_data = ' ')
    time_5 = types.InlineKeyboardButton(text="5. Майдан (Пн)", callback_data = ' ')
    button_1 = types.InlineKeyboardButton(text=" ", callback_data = ' ')
    button_2 = types.InlineKeyboardButton(text="⏹", callback_data = "⏹")
    button_3 = types.InlineKeyboardButton(text=" ", callback_data = ' ')
    time.add(time_0)
    time.add(time_1)
    time.add(time_2)
    time.add(time_3)
    time.add(time_4)
    time.add(time_5)
    time.add(pustota)
    time.add(pustota)
    time.add(pustota)
    time.add(pustota)
    time.add(pustota)
    time.add(button_1, button_2, button_3)
    text=stroka_sostoyaniya
    reply_markup=time
    return text, reply_markup