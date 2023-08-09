import telebot, os, asyncio
from shazamio import Shazam
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

def start_voice(message, token):
    bot = telebot.TeleBot(token)
    voice = message.voice
    file_info = bot.get_file(voice.file_id)
    file_path = file_info.file_path
    file_extension = os.path.splitext(file_path)[1]
    random_filename = f'{os.urandom(8).hex()}{file_extension}'
    global download_path
    download_path = random_filename
    global msg
    msg = message
    downloaded_file = bot.download_file(file_path)
    with open(download_path, 'wb') as new_file:
        new_file.write(downloaded_file)
    loop.run_until_complete(recognize_song(download_path, message, token))
    try: os.remove(downloaded_file)
    except: pass

async def recognize_song(file_path, message, token):
    bot = telebot.TeleBot(token)
    msg = message
    shazam = Shazam()
    out = await shazam.recognize_song(file_path)
    try: error =(out['matches'][0]['id'])
    except: bot.reply_to(msg, f"<code>Не зміг знайти музичку</code>", parse_mode='HTML')
    else: 
        try:
            vuvod = "<code>"
            try:
                photo = str(out['track']['images']['coverart'])
                name =  str(out['track']['title']) + " | " + str(out['track']['subtitle'])
                bot.send_photo(msg.chat.id, photo, caption=f"<code>{name}</code>", parse_mode='HTML')
            except:
                photo = 'error'
                bot.reply_to(msg, f"<code>Не знайшов фото</code>", parse_mode='HTML')
            if photo == 'error':
                try: 
                    name =  str(out['track']['title']) + " | " + str(out['track']['subtitle'])
                    bot.send_message(msg.chat.id, text=f"<code>Зате зміг знайти назву: {name}</code>", parse_mode='HTML')
                except:
                    bot.reply_to(msg, f"<code>Не зміг знайти музичку</code>", parse_mode='HTML')
            try:
                shazam_href = str(out['track']['share']['href'])
                text_song = str(out['track']['sections'][1]['text'])
                # Удаление квадратных скобок и одинарных кавычек из текста
                text_song = text_song.replace("[", "").replace("]", "").replace("'", "")
                # Разделение текста на строки песни
                lines = text_song.split(", ")
                text_song = ""
                # Вывод строк песни
                for line in lines:
                    text_song += f"{line}\n\n"
                vuvod += "\n\n" + str(text_song) +  "\n\n"
                vuvod += "</code>"
                keyboard = telebot.types.InlineKeyboardMarkup()
                keyboard.add(telebot.types.InlineKeyboardButton(text=name, url=shazam_href))
                bot.send_message(msg.chat.id, text=f"{vuvod}", reply_markup=keyboard, parse_mode='HTML')
            except: bot.reply_to(msg, f"<code>Не знайшов текст</code>", parse_mode='HTML')
        except Exception as e: bot.reply_to(msg, f"<code>{e}</code>", parse_mode='HTML')
    try: os.remove(download_path)
    except: pass
    try: os.remove(file_path)
    except: pass