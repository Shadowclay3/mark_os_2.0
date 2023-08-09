from datetime import datetime
from telebot import types

def Info_OS():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    stroka_sostoyaniya = "⌚️ " +  current_time + "                   📳  📶  ✉️  89% 🔋" #🔋🪫 🔌
    Info_OS = types.InlineKeyboardMarkup()
    button_1 = types.InlineKeyboardButton(text=" ", callback_data = ' ')
    button_2 = types.InlineKeyboardButton(text="⏹", callback_data = '⏹')
    button_3 = types.InlineKeyboardButton(text=" ", callback_data = ' ')
    name_OS = types.InlineKeyboardButton(text="Mark_OS", callback_data = ' ')
    version_bot = types.InlineKeyboardButton(text="версія(боту):  V.3.0", callback_data = ' ')
    version_OS = types.InlineKeyboardButton(text="версія(OS):  V.3.8.66.4", callback_data = ' ')
    yazuk = types.InlineKeyboardButton(text="мова: PYTHON 3.10.6", callback_data = ' ')
    document_OS = types.InlineKeyboardButton(text="Власник -> @marklanselot", callback_data = ' ')
    database = types.InlineKeyboardButton(text="database: json", callback_data = ' ')
    library = types.InlineKeyboardButton(text="бібліотекa: PyTelegramBotAPI", callback_data = ' ')
    library_telebot = types.InlineKeyboardButton(text="pyTelegramBotAPI: pypi v.4.10.0", callback_data = ' ')
    library_TelegramBotAPI  = types.InlineKeyboardButton(text="Telegram Bot API: v.6.4", callback_data = ' ')
    hosting  = types.InlineKeyboardButton(text="hosting: s-host.com.ua", callback_data = ' ')
    system_hosting = types.InlineKeyboardButton(text="Linux-Ubuntu-20.04-x86_64", callback_data = ' ')
    midjorny = types.InlineKeyboardButton(text="midjorney: DALLE", callback_data = ' ')
    Info_OS.add(name_OS)
    Info_OS.add(version_bot)
    Info_OS.add(version_OS)
    Info_OS.add(yazuk)
    Info_OS.add(document_OS)
    Info_OS.add(database)
    Info_OS.add(library)
    Info_OS.add(library_telebot)
    Info_OS.add(library_TelegramBotAPI)
    Info_OS.add(hosting)
    Info_OS.add(system_hosting)
    Info_OS.add(midjorny)
    Info_OS.add(button_1, button_2, button_3)
    text=stroka_sostoyaniya
    reply_markup=Info_OS
    return text, reply_markup