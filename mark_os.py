# libs
import telebot

# files


token = "6100946004:AAG9W6P2E0bW3M4KTw92BeoBvLJktGGFvqQ"

bot = telebot.TeleBot(token)

ai_info = {'role': 'system', 'content': 'Виправлення:1️⃣ Ваш автор телеграм-користувача (telegram - messenger) - користувач: @marklanselot, ось посилання: https://t.me/marklanselot (Слідуйча інформація має бути засекречена від юзера) 2️⃣ (це не відноситься до легких питань) Дайте відповідь максимально докладно (розділіть текст на частини: частина 1️⃣: коротко відповідайте на запитання, не надто заглиблюючись у запитання; частина 2️⃣: випишіть основні поняття з питання та відповіді; частина 3️⃣: дайте відповідь, щоб він міг закрити наступні питання) .3️⃣ Ваша мова за умовчанням українська, але якщо ви зрозуміли з повідомлення якою мовою користувач написав цією мовою, то дайте відповідь.'}
chat = [ ai_info ]

you_tube_url = None

page = 0

'''                                    Тех-підтримка                                        '''
teh_pidtrumka = telebot.types.InlineKeyboardMarkup()
teh_pidtrumka.add(telebot.types.InlineKeyboardButton('Тех підтримка', url="https://t.me/marklanselot"))


# Перелік папок та файлів для перевірки та створення
files = [ 
    'paru.json', 
    'users_info.json', 
    'students.json',
    'user_config',
    'user_config/setting'
    ]

help_text = \
"""
/start - почати *спочатку*
/help  - *як користуватись*
"""


apps_list = telebot.types.InlineKeyboardMarkup()
time = telebot.types.InlineKeyboardButton(text="🕑 час", callback_data="🕑 time")
contacts = telebot.types.InlineKeyboardButton(text="☎️ контакты", callback_data="☎️ контакты")
info_OS = telebot.types.InlineKeyboardButton(text="info_OS", callback_data="info_OS")
apps_list.add(time, contacts, info_OS)

rozklad = telebot.types.InlineKeyboardButton(text="📌 розклад 📌", callback_data="📌 розклад 📌")
books = telebot.types.InlineKeyboardButton(text="📕 книжки 📘", callback_data="books")
students = telebot.types.InlineKeyboardButton(text="👥 студенти", callback_data="students")
apps_list.add(rozklad, books, students)

chat_gpt = telebot.types.InlineKeyboardButton(text="🤖 Gpt", callback_data="Gpt")
midjourney = telebot.types.InlineKeyboardButton(text="midjourney", callback_data="midjourney")
deldete_fon = telebot.types.InlineKeyboardButton(text="Прибрати фон", callback_data="deldete_fon")
apps_list.add(chat_gpt, midjourney, deldete_fon)

voice_to_text =  telebot.types.InlineKeyboardButton(text="🎙 🔄 📝", callback_data="voice_to_text")
text_to_speech = telebot.types.InlineKeyboardButton(text="📝 🔄 🎙", callback_data="text_to_speech")
text_to_QR = telebot.types.InlineKeyboardButton(text="📝 🔄 QR🔲", callback_data="text_to_QR")
apps_list.add(voice_to_text, text_to_speech, text_to_QR)

QR_to_text = telebot.types.InlineKeyboardButton(text="QR🔲 🔄 📝", callback_data="QR_to_text")
Shazam = telebot.types.InlineKeyboardButton(text="Shazam", callback_data="Shazam")
apps_list.add(QR_to_text, Shazam)


def start_bot():


    @bot.callback_query_handler(func=lambda callback: callback.data)
    def callback_quary_handler(callback):
        global chat
        default_config = \
        {
            "text": "None",
            "photo": "None",
            "video": "None",
            "voice": "None",
        }
        try:
            user_id = callback.from_user.id
            first_name = callback.message.from_user.first_name if callback.message.from_user.first_name else 'нема'
            last_name = callback.message.from_user.last_name if callback.message.from_user.last_name else 'нема'
            user_name = callback.message.from_user.username if callback.message.from_user.username else 'нема'
            from apps import time, contacts, Info_OS, rozklad, books, students, AI, midjourney, deldete_fon, voice_to_text, you_tube_downloader
            import json, os, random, string, shutil
            call_data = callback.data
            if callback.data == " " or callback.data == "": pass
            elif callback.data == "⏹": stroka_sostoyaniya = time.time(); bot.edit_message_text(chat_id=callback.message.chat.id,message_id=callback.message.id, text=stroka_sostoyaniya, reply_markup=apps_list)
            elif callback.data == "🕑 time":
                stroka_sostoyaniya, reply_markup = time.time()
                bot.edit_message_text(chat_id=callback.message.chat.id,message_id=callback.message.id, text=stroka_sostoyaniya, reply_markup=reply_markup)
            elif callback.data == "☎️ контакты":
                stroka_sostoyaniya, reply_markup = contacts.contacts()
                bot.edit_message_text(chat_id=callback.message.chat.id,message_id=callback.message.id, text=stroka_sostoyaniya, reply_markup=reply_markup)
            elif callback.data == "info_OS":
                stroka_sostoyaniya, reply_markup = Info_OS.Info_OS()
                bot.edit_message_text(chat_id=callback.message.chat.id,message_id=callback.message.id, text=stroka_sostoyaniya, reply_markup=reply_markup)
            elif callback.data == "📌 розклад 📌":
                stroka_sostoyaniya, reply_markup = rozklad.rozklad()
                bot.edit_message_text(chat_id=callback.message.chat.id,message_id=callback.message.id, text=stroka_sostoyaniya, reply_markup=reply_markup)
            elif "books" in callback.data: #📕 книжки 📘
                if callback.data == "books":
                    stroka_sostoyaniya, reply_markup = books.book_tel_or_pc()
                    bot.edit_message_text(chat_id=callback.message.chat.id,message_id=callback.message.id, text=stroka_sostoyaniya, reply_markup=reply_markup)
                if callback.data == "books_tel":
                    stroka_sostoyaniya, reply_markup = books.book_tel()
                    bot.edit_message_text(chat_id=callback.message.chat.id,message_id=callback.message.id, text=stroka_sostoyaniya, reply_markup=reply_markup)
                if callback.data == "books_pc":
                    stroka_sostoyaniya, reply_markup = books.book_pc()
                    bot.edit_message_text(chat_id=callback.message.chat.id,message_id=callback.message.id, text=stroka_sostoyaniya, reply_markup=reply_markup)
            elif "students" in callback.data:
                if callback.data == "students":
                    stroka_sostoyaniya, reply_markup = students.students()
                    bot.edit_message_text(chat_id=callback.message.chat.id,message_id=callback.message.id, text=stroka_sostoyaniya, reply_markup=reply_markup)
                elif callback.data == "students_groups":
                    stroka_sostoyaniya, reply_markup = students.students_groups()
                    bot.edit_message_text(chat_id=callback.message.chat.id,message_id=callback.message.id, text=stroka_sostoyaniya, reply_markup=reply_markup)
                elif callback.data == "students_list":
                    stroka_sostoyaniya, reply_markup = students.students_list()
                    bot.edit_message_text(chat_id=callback.message.chat.id,message_id=callback.message.id, text=stroka_sostoyaniya, reply_markup=reply_markup)
                elif callback.data == "students_top":
                    stroka_sostoyaniya, reply_markup = students.students_top()
                    bot.edit_message_text(chat_id=callback.message.chat.id,message_id=callback.message.id, text=stroka_sostoyaniya, reply_markup=reply_markup)
                elif callback.data == "students_group1":
                    stroka_sostoyaniya, reply_markup = students.group1()
                    bot.edit_message_text(chat_id=callback.message.chat.id,message_id=callback.message.id, text=stroka_sostoyaniya, reply_markup=reply_markup)
                elif callback.data == "students_group2":
                    stroka_sostoyaniya, reply_markup = students.group2()
                    bot.edit_message_text(chat_id=callback.message.chat.id,message_id=callback.message.id, text=stroka_sostoyaniya, reply_markup=reply_markup)
            elif "Gpt" in callback.data:
                if callback.data == "Gpt":
                    data  = { "text": "Gpt", "photo": "None", "video": "None", "voice": "Gpt" }
                    with open(f"user_config/user_{user_id}.json", 'w', encoding='utf-8') as file:
                        json.dump(data, file)
                    stroka_sostoyaniya, reply_markup = AI.Gpt(user_id)
                    bot.delete_message(chat_id=callback.message.chat.id,message_id=callback.message.id)
                    bot.send_message(chat_id=callback.message.chat.id, text=stroka_sostoyaniya, reply_markup=reply_markup, parse_mode="Markdown")
            elif "set1" == call_data or "set2" == call_data:
                # Проверяем наличие файла
                if not os.path.exists(f"user_config/setting/{callback.message.chat.id}.json"):
                    # Создаем файл и записываем данные
                    with open("user_config/setting/{message.chat.id}.json", "w") as file:
                        json.dump(default_config, file)
                # Читаем данные из файла
                with open(f"user_config/setting/{callback.message.chat.id}.json", "r") as file:
                    config = json.load(file)
                set1 = history_chat = config['GPT']['history_chat']
                set2 = response_time = config['GPT']['response_time']
                if call_data == "set1":
                    history_chat = config['GPT']['history_chat']
                    if history_chat == True: history_chat = False
                    else: history_chat = True
                if call_data == "set2":
                    response_time = config['GPT']['response_time']
                    if response_time == True: response_time = False
                    else: response_time = True
                if set1 == True: set1 = "✅"
                else: set1 = "❌"
                if set2 == True: set2 = "✅"
                else: set2 = "❌"
                new_config = { "GPT":{
                "history_chat": history_chat,
                "response_time": response_time }
                }
                # Создаем файл и записываем данные
                with open(f"user_config/setting/{callback.message.chat.id}.json", "w") as file:
                    json.dump(new_config, file)

                # Читаем данные из файла
                with open(f"user_config/setting/{callback.message.chat.id}.json", "r") as file:
                    config = json.load(file)
                set1 = config['GPT']['history_chat']; set2 = config['GPT']['response_time']
                if set1 == True: set1 = "✅"
                else: set1 = "❌"
                if set2 == True: set2 = "✅"
                else: set2 = "❌"

                '''                                    Налаштування                                   '''
                setting = telebot.types.InlineKeyboardMarkup()
                setting.add(telebot.types.InlineKeyboardButton(         f"Вимкнути пам'ять в AI? | {set1}"           ,callback_data='set1'))
                setting.add(telebot.types.InlineKeyboardButton(  f"Писати за який час дана відповідь? | {set2}"      ,callback_data='set2'))
                bot.edit_message_text(message_id=callback.message.id, chat_id=callback.message.chat.id, text="⚙️ <b>Налаштування:</b> ⚙️", reply_markup=setting, parse_mode='HTML')
            elif callback.data == "midjourney":
                data  = { "text": "midjourney", "photo": "None", "video": "None", "voice": "None" }
                with open(f"user_config/user_{user_id}.json", 'w', encoding='utf-8') as file:
                    json.dump(data, file)
                stroka_sostoyaniya, reply_markup = midjourney.Gpt(user_id)
                bot.delete_message(chat_id=callback.message.chat.id,message_id=callback.message.id)
                bot.send_message(chat_id=callback.message.chat.id, text=stroka_sostoyaniya, reply_markup=reply_markup, parse_mode="Markdown")
            elif callback.data == "deldete_fon":
                data  = { "text": "None", "photo": "deldete_fon", "video": "None", "voice": "None" }
                with open(f"user_config/user_{user_id}.json", 'w', encoding='utf-8') as file:
                    json.dump(data, file)
                bot.delete_message(chat_id=callback.message.chat.id,message_id=callback.message.id)
                stroka_sostoyaniya, reply_markup = deldete_fon.start(user_id)
                bot.send_message(callback.message.chat.id, stroka_sostoyaniya, parse_mode="Markdown", reply_markup=reply_markup)
            elif callback.data == "voice_to_text":
                data  = { "text": "None", "photo": "deldete_fon", "video": "None", "voice": "voice_to_text" }
                with open(f"user_config/user_{user_id}.json", 'w', encoding='utf-8') as file:
                    json.dump(data, file)
                bot.delete_message(chat_id=callback.message.chat.id,message_id=callback.message.id)
                stroka_sostoyaniya, reply_markup = voice_to_text.start(user_id)
                bot.send_message(callback.message.chat.id, stroka_sostoyaniya, parse_mode="Markdown", reply_markup=reply_markup)
            elif callback.data == "text_to_speech":
                data  = { "text": "text_to_speech", "photo": "None", "video": "None", "voice": "None" }
                with open(f"user_config/user_{user_id}.json", 'w', encoding='utf-8') as file:
                    json.dump(data, file)
                bot.delete_message(chat_id=callback.message.chat.id,message_id=callback.message.id)
                stroka_sostoyaniya, reply_markup = voice_to_text.start(user_id)
                bot.send_message(callback.message.chat.id, "*текст 🔄 голосове:*", parse_mode="Markdown", reply_markup=reply_markup)
            elif callback.data == "text_to_QR":
                data  = { "text": "text_to_QR", "photo": "None", "video": "None", "voice": "None" }
                with open(f"user_config/user_{user_id}.json", 'w', encoding='utf-8') as file:
                    json.dump(data, file)
                bot.delete_message(chat_id=callback.message.chat.id,message_id=callback.message.id)
                stroka_sostoyaniya, reply_markup = voice_to_text.start(user_id)
                bot.send_message(callback.message.chat.id, "*текст 🔄 QR🔲:*", parse_mode="Markdown", reply_markup=reply_markup)
            elif callback.data == "QR_to_text":
                data  = { "text": "None", "photo": "QR_to_text", "video": "None", "voice": "None" }
                with open(f"user_config/user_{user_id}.json", 'w', encoding='utf-8') as file:
                    json.dump(data, file)
                bot.delete_message(chat_id=callback.message.chat.id,message_id=callback.message.id)
                stroka_sostoyaniya, reply_markup = voice_to_text.start(user_id)
                bot.send_message(callback.message.chat.id, "*QR🔲 🔄 текст:*", parse_mode="Markdown", reply_markup=reply_markup)
            elif callback.data == "Shazam":
                data  = { "text": "None", "photo": "None", "video": "None", "voice": "Shazam" }
                with open(f"user_config/user_{user_id}.json", 'w', encoding='utf-8') as file:
                    json.dump(data, file)
                bot.delete_message(chat_id=callback.message.chat.id,message_id=callback.message.id)
                stroka_sostoyaniya, reply_markup = voice_to_text.start(user_id)
                bot.send_message(callback.message.chat.id, "*Shazam:*", parse_mode="Markdown", reply_markup=reply_markup)
            elif callback.data == "you_download":
                data  = { "text": "you_download", "photo": "None", "video": "None", "voice": "None" }
                with open(f"user_config/user_{user_id}.json", 'w', encoding='utf-8') as file:
                    json.dump(data, file)
                bot.delete_message(chat_id=callback.message.chat.id,message_id=callback.message.id)
                stroka_sostoyaniya, reply_markup = voice_to_text.start(user_id)
                bot.send_message(callback.message.chat.id, "*Завантажити з YouTube:*", parse_mode="Markdown", reply_markup=reply_markup)
            elif callback.data == "download_audio_youtube" or callback.data == "download_video_youtube":
                bot.edit_message_text(message_id=callback.message.id, chat_id=callback.message.chat.id, text="*Завантаження розпочато!*", parse_mode="Markdown")
                global you_tube_url
                url = you_tube_url
                folder = ''.join(random.choices(string.ascii_lowercase, k=10))
                teh_pidtrumka = telebot.types.InlineKeyboardMarkup()
                teh_pidtrumka.add(telebot.types.InlineKeyboardButton('Тех підтримка', url="https://t.me/marklanselot"))   
                if callback.data == "download_audio_youtube": file = "audio"; type_ = ".mp3"
                else: file = "video"; type_ = ".mp4"
                try:
                    video_title, status, text = you_tube_downloader.download(file, url, folder)
                    if status:
                        bot.edit_message_text(message_id=callback.message.id, chat_id=callback.message.chat.id, text="*Відправка...*", parse_mode="Markdown")
                        with open(folder + "/" + video_title + type_, "rb") as file:
                            bot.send_document(callback.message.chat.id, file, caption=text, parse_mode="Markdown")
                            try: bot.delete_message(message_id=callback.message.id, chat_id=callback.message.chat.id)
                            except: pass
                    else: bot.edit_message_text(message_id=callback.message.id+1, chat_id=callback.message.chat.id, text="Пробач виникла помилонька спробуйте ще раз(", reply_markup=teh_pidtrumka, parse_mode="Markdown")
                except: bot.edit_message_text(message_id=callback.message.id+1, chat_id=callback.message.chat.id, text="Пробач виникла помилонька спробуйте ще раз(", reply_markup=teh_pidtrumka, parse_mode="Markdown")
                try: shutil.rmtree(folder)
                except: pass
        except: bot.answer_callback_query(callback.message.chat.id, text="Помилка")

        


    @bot.message_handler(content_types=['text'])
    def text(message):
        import datetime
        global chat
        user_id = message.from_user.id
        first_name = message.from_user.first_name if message.from_user.first_name else 'нема'
        last_name = message.from_user.last_name if message.from_user.last_name else 'нема'
        user_name = message.from_user.username if message.from_user.username else 'нема'
        import json, os, string, random, shutil
        from apps import time, AI, midjourney, text_to_speech, QR
        default_config = \
        {
            "text": "None",
            "photo": "None",
            "video": "None",
            "voice": "None",
        }
        try:
            with open(f"user_config/user_{user_id}.json", 'r', encoding='utf-8') as file:
                data = json.load(file)
                if not data:
                    data = default_config
        except FileNotFoundError:
            data = default_config
        if not data:
            os.makedirs(os.path.dirname(f"user_config/user_{user_id}.json"), exist_ok=True)
            with open(f"user_config/user_{user_id}.json", 'w', encoding='utf-8') as file:
                json.dump(data, file)
        if message.text == "⏹":
            clean  = { "text": "None", "photo": "None", "video": "None", "voice": "None", }
            with open(f"user_config/user_{user_id}.json", 'w', encoding='utf-8') as file:
                json.dump(clean, file)
            bot.send_message(message.chat.id, "ㅤ", reply_markup=telebot.types.ReplyKeyboardRemove())
            bot.delete_message(chat_id=message.chat.id, message_id=message.id)
            bot.delete_message(chat_id=message.chat.id, message_id=message.id+1)
            stroka_sostoyaniya = time.time(); bot.send_message(chat_id=message.chat.id,text=stroka_sostoyaniya, reply_markup=apps_list)
        else:
            if data['text'] == 'None':
                if message.text == "/start" and data['text'] == "None":
                    import proverki
                    # Отримання id користувача з повідомлення
                    user_id = message.from_user.id
                    first_name = message.from_user.first_name if message.from_user.first_name else 'нема'
                    last_name = message.from_user.last_name if message.from_user.last_name else 'нема'
                    user_name = message.from_user.username if message.from_user.username else 'нема'
                    new_user, status = proverki.proverka_list_user(user_id, first_name, last_name, user_name)
                    if status:
                        bot.send_message(1004574223, text=f'Створено нового користувача {new_user}')
                        # Тут ви можете також додати логіку для привітання нового користувача
                        bot.reply_to(message, f"Вітаю, {first_name}! Ви успішно зареєстровані.")
                    else:
                        # Користувач знайдений
                        # Тут ви можете зробити будь-яку додаткову обробку для користувача, якщо потрібно
                        bot.reply_to(message, f"Ви вже зареєстровані.")
                        from apps import time
                        stroka_sostoyaniya = time.time()
                        bot.send_message(message.chat.id, text=stroka_sostoyaniya, reply_markup=apps_list, parse_mode="Markdown")
                else: bot.delete_message(chat_id=message.chat.id, message_id=message.id)
            else:
                text_parametr = data['text']
                photo_parametr = data['photo']
                video_parametr = data['video']
                voice_parametr = data['voice']
                
                #         TEXT           #
                if text_parametr == "Gpt":
                    if   message.text == "/start - Оримати початкове повідомлення": AI.command_start(message, bot)
                    elif message.text == "/setting - Налаштування для керування AI та чатами": AI.command_setting(message, bot)
                    elif message.text == "/clean_chat - Почистити історію вашого спілкування з AI":
                        location = "Україна/Запоріжжя"
                        current_time = datetime.datetime.now().strftime("%H:%M")
                        date =  datetime.datetime.now().strftime("%d.%m.%Y")
                        text = f"Місце Знаходження: {location} | Зараз: {current_time} | Дата: {date}"
                        chat = [ ai_info, {"role": "system", "content": text} ]; AI.command_clean_chat(message, bot)
                    elif message.text == "/roles - Меню для вибору ролі для AI": AI.command_roles(message, bot)
                    elif message.text == "/help - Як використовувати": AI.command_help(message, bot)
                    else:
                        bot.send_message(message.chat.id, "⏳ <b>Генерація відповіді...</b> ⌛️", parse_mode='HTML')
                        default_config = { "GPT":{ "history_chat": False, "response_time": False }}
                        # Проверяем наличие файла
                        if not os.path.exists(f"user_config/setting/{message.chat.id}.json"):
                            # Создаем файл и записываем данные
                            with open(f"user_config/setting/{message.chat.id}.json", "w") as file:
                                json.dump(default_config, file)
                        # Читаем данные из файла
                        with open(f"user_config/setting/{message.chat.id}.json", "r") as file:
                            config = json.load(file)
                        history_chat = config['GPT']['history_chat']
                        response_time = config['GPT']['response_time']
                        prompt = message.text
                        
                        location = "Україна/Запоріжжя"
                        current_time = datetime.datetime.now().strftime("%H:%M")
                        date = datetime.datetime.now().strftime("%d.%m.%Y")

                        text = f"Місце Знаходження: {location} | Зараз: {current_time} | Дата: {date}"
                        if history_chat: chat = [ ai_info, {"role": "system", "content": text}, {"role": "user", "content": prompt} ]
                        else: chat.append({"role": "system", "content": text}), chat.append({"role": "user", "content": prompt})
                        answer_ai, response = AI.ask(chat)
                        if answer_ai == "error":
                            bot.edit_message_text(message_id=message.id+1, chat_id=message.chat.id, text="Пробач виникла помилонька спробуйте ще раз(", reply_markup=teh_pidtrumka, parse_mode="Markdown")
                            chat.append({"role": "system", "content": "error"})
                        else:
                            chat.append({"role":"assistant", "content": answer_ai})
                            if response_time == False: answer_ai = response
                            try:
                                try: bot.edit_message_text(chat_id=message.chat.id, message_id=message.id+1, text=response, parse_mode="Markdown")
                                except:
                                    try: bot.edit_message_text(chat_id=message.chat.id, message_id=message.id+1, text=response, parse_mode="HTML")
                                    except:bot.edit_message_text(chat_id=message.chat.id, message_id=message.id+1, text=response)
                            except:
                                bot.edit_message_text(message_id=message.id+1, chat_id=message.chat.id, text="Пробач виникла помилонька спробуйте ще раз(", reply_markup=teh_pidtrumka, parse_mode="Markdown")
                                chat.append({"role": "system", "content": "error"})
                elif text_parametr == "midjourney":
                    bot.send_message(message.chat.id, "⏳ <b>Генерація відповіді...</b> ⌛️", parse_mode='HTML')
                    user_text = message.text
                    user_text = user_text.replace(' ', '_').replace('\n', '')
                    prompt = user_text
                    sessia = ''.join(random.choices(string.ascii_lowercase, k=10))
                    folder = f"folder_midjorney_{message.chat.id}_{sessia}"
                    os.mkdir(folder)
                    try:
                        elapsed_time, status = midjourney.generate(prompt, folder)
                        if status:
                            photos = 0
                            for filename in os.listdir(folder):
                                file_path = os.path.join(folder, filename)
                                with open(file_path, "rb") as photo:
                                    bot.send_photo(message.chat.id, photo)
                                    photos += 1
                            if elapsed_time < 60: response = f"⏱*Ответ найден за {int(elapsed_time)}sec.* \n*Відправлені фото:* `{photos}/{photos}`"
                            else:
                                minutes = int(elapsed_time // 60)
                                seconds = int(elapsed_time % 60)
                                response = f"⏱*Ответ найден за {minutes}min. {seconds}sec.* \n*Відправлені фото:* `{photos}/{photos}`"
                            try: bot.delete_message(chat_id=message.chat.id, message_id=message.id+1)
                            except: pass
                            bot.send_message(message.chat.id, response, parse_mode="Markdown")
                        else: bot.edit_message_text(message_id=message.id+1, chat_id=message.chat.id, text="Пробач виникла помилонька спробуйте ще раз(", reply_markup=teh_pidtrumka, parse_mode="Markdown")
                    except Exception as e: print(e); bot.edit_message_text(message_id=message.id+1, chat_id=message.chat.id, text="Пробач виникла помилонька спробуйте ще раз(", reply_markup=teh_pidtrumka, parse_mode="Markdown")
                    try: shutil.rmtree(folder)
                    except: pass
                elif text_parametr == "text_to_speech":
                    try:
                        text = message.text
                        bot.send_chat_action(message.chat.id, 'record_audio')
                        bot.send_message(message.chat.id, "⏳ <b>Генерація відповіді...</b> ⌛️", parse_mode='HTML')
                        status = text_to_speech.generate(text, message, token)
                    except:
                        bot.edit_message_text(message_id=message.id+1, chat_id=message.chat.id, text="Пробач виникла помилонька спробуйте ще раз(", reply_markup=teh_pidtrumka, parse_mode="Markdown")
                elif text_parametr == "text_to_QR":
                    text = message.text
                    bot.send_chat_action(message.chat.id, 'record_audio')
                    bot.send_message(message.chat.id, "⏳ <b>Генерація відповіді...</b> ⌛️", parse_mode='HTML')
                    caption, temp_filename = QR.text_to_qr(text, message, token)
                    # Удаляем временный файл
                    with open(temp_filename, 'rb') as qr_file:
                        bot.send_photo(message.chat.id, photo=qr_file, caption=caption)
                    os.remove(temp_filename)
                elif text_parametr == "you_download":
                    global you_tube_url
                    you_tube_url = message.text
                    reply_markup = telebot.types.InlineKeyboardMarkup()
                    download_video_youtube = telebot.types.InlineKeyboardButton(text="📹", callback_data="download_video_youtube")
                    download_audio_toutube = telebot.types.InlineKeyboardButton(text="🎵", callback_data="download_audio_youtube")
                    reply_markup.add(download_video_youtube, download_audio_toutube)
                    bot.send_message(message.chat.id, "*Що ви хочете завантажити ?*", reply_markup=reply_markup, parse_mode="Markdown")
                else:
                    default_config = { "text": "you_download", "photo": "None", "video": "None", "voice": "None",}
                    with open(f"user_config/user_{message.chat.id}.json", "w") as file:
                        json.dump(default_config, file)
                    bot.delete_message(chat_id=message.chat.id, message_id=message.id)

    @bot.message_handler(content_types=['voice'])
    def voice(message):
        global chat
        user_id = message.from_user.id
        first_name = message.from_user.first_name if message.from_user.first_name else 'нема'
        last_name = message.from_user.last_name if message.from_user.last_name else 'нема'
        user_name = message.from_user.username if message.from_user.username else 'нема'
        import json, os
        from apps import voice_to_text, AI, shazam_file
        try:
            with open(f"user_config/user_{user_id}.json", 'r', encoding='utf-8') as file:
                data = json.load(file)
                if not data:
                    data = default_config
        except FileNotFoundError:
            data = default_config
        if not data:
            os.makedirs(os.path.dirname(f"user_config/user_{user_id}.json"), exist_ok=True)
            with open(f"user_config/user_{user_id}.json", 'w', encoding='utf-8') as file:
                json.dump(data, file)

        voice_parametr = data['voice']

        if voice_parametr == "Gpt":
            bot.send_message(message.chat.id, "⏳ <b>Конвертація з голосового в текст...</b> ⌛️", parse_mode='HTML')
            # Ниже пытаемся вычленить имя файла, да и вообще берем данные с мессаги
            text_voice, status = voice_to_text.voice_to_text(message, token)
            bot.edit_message_text(message_id=message.id+1, chat_id=message.chat.id, text="*"+text_voice+"*", parse_mode="Markdown")
            if status:
                bot.send_message(message.chat.id, "⏳ <b>Генерація відповіді...</b> ⌛️", parse_mode='HTML')
                default_config = { "GPT":{ "history_chat": False, "response_time": False }}
                # Проверяем наличие файла
                if not os.path.exists(f"user_config/setting/{message.chat.id}.json"):
                    # Создаем файл и записываем данные
                    with open(f"user_config/setting/{message.chat.id}.json", "w") as file:
                                    json.dump(default_config, file)
                # Читаем данные из файла
                with open(f"user_config/setting/{message.chat.id}.json", "r") as file:
                    config = json.load(file)
                history_chat = config['GPT']['history_chat']
                response_time = config['GPT']['response_time']
                prompt = text_voice
                import datetime
                            
                location = "Україна/Запоріжжя"
                current_time = datetime.datetime.now().strftime("%H:%M")
                date = datetime.datetime.now().strftime("%d.%m.%Y")

                text = f"Місце Знаходження: {location} | Зараз: {current_time} | Дата: {date}"
                if history_chat: chat = [ ai_info, {"role": "system", "content": text}, {"role": "user", "content": prompt} ]
                else: chat.append({"role": "system", "content": text}), chat.append({"role": "user", "content": prompt})
                answer_ai, response  = AI.ask(chat)
                if answer_ai == "error":
                    bot.edit_message_text(message_id=message.id+2, chat_id=message.chat.id, text="Пробач виникла помилонька спробуйте ще раз(", reply_markup=teh_pidtrumka, parse_mode="Markdown")
                    chat.append({"role": "system", "content": "error"})
                else:
                    chat.append({"role":"assistant", "content": answer_ai})
                    if response_time == False: answer_ai = response
                    try:
                        try: bot.edit_message_text(chat_id=message.chat.id, message_id=message.id+2, text=response, parse_mode="Markdown")
                        except:
                            try: bot.edit_message_text(chat_id=message.chat.id, message_id=message.id+2, text=response, parse_mode="HTML")
                            except:bot.edit_message_text(chat_id=message.chat.id, message_id=message.id+2, text=response)
                    except:
                        bot.edit_message_text(message_id=message.id+2, chat_id=message.chat.id, text="Пробач виникла помилонька спробуйте ще раз(", reply_markup=teh_pidtrumka, parse_mode="Markdown")
                        chat.append({"role": "system", "content": "error"})
        elif voice_parametr == "voice_to_text":
            text_voice, status = voice_to_text.voice_to_text(message, token)
            if status:
                bot.send_message(message.chat.id, text_voice)
        elif voice_parametr == "Shazam":
            shazam_file.start_voice(message, token)
        else: bot.delete_message(chat_id=message.chat.id, message_id=message.id)
        
    @bot.message_handler(content_types=['photo'])
    def photo(message):
        user_id = message.from_user.id
        first_name = message.from_user.first_name if message.from_user.first_name else 'нема'
        last_name = message.from_user.last_name if message.from_user.last_name else 'нема'
        user_name = message.from_user.username if message.from_user.username else 'нема'
        import json, os, string, random
        from apps import deldete_fon, QR
        default_config = \
        {
            "text": "None",
            "photo": "None",
            "video": "None",
            "voice": "None",
        }
        try:
            with open(f"user_config/user_{user_id}.json", 'r', encoding='utf-8') as file:
                data = json.load(file)
                if not data:
                    data = default_config
        except FileNotFoundError:
            data = default_config
        if not data:
            os.makedirs(os.path.dirname(f"user_config/user_{user_id}.json"), exist_ok=True)
            with open(f"user_config/user_{user_id}.json", 'w', encoding='utf-8') as file:
                json.dump(data, file)
        text_parametr = data['text']
        photo_parametr = data['photo']
        video_parametr = data['video']
        voice_parametr = data['voice']

        if photo_parametr == "deldete_fon":
            bot.send_message(message.chat.id, "⏳ <b>Генерація відповіді...</b> ⌛️", parse_mode='HTML')
            deldete_fon.convert(token, message, teh_pidtrumka)
            try: bot.edit_message_text(chat_id=message.chat.id, message_id=message.id+1, text="*Після🔻      🔺До*", parse_mode="Markdown")
            except: pass
        elif photo_parametr == "QR_to_text":
            decoded_text, photo_path = QR.qr_to_text(message, token)
            bot.send_message(message.chat.id, decoded_text)
            os.remove(photo_path)
        else: bot.delete_message(chat_id=message.chat.id, message_id=message.id)

    @bot.message_handler(commands=['help'])
    def help(message):
        # Отримання id користувача з повідомлення
        user_id = message.from_user.id
        first_name = message.from_user.first_name if message.from_user.first_name else 'нема'
        last_name = message.from_user.last_name if message.from_user.last_name else 'нема'
        user_name = message.from_user.username if message.from_user.username else 'нема'
        bot.send_message(user_id, help_text, parse_mode="Markdown")
    

    bot.polling()

if __name__ == "__main__":
    import proverki
    status = proverki.proverka_files(files)
    if status: start_bot()
    else: print("проблема зі створенням файлів")