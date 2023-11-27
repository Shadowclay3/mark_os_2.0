import telebot, json, random, uuid, requests, os


token = "6907078461:AAHq17UhG4JoKyjJTDyQZYPgYG2obUts1Ek"

bot = telebot.TeleBot(token)

def json_data(file_name: str):
    with open(file_name, "r", encoding="utf-8") as f:
        return json.load(f)

def write_json_data(file_name: str, data: dict):
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def name_team(message):
    if message.text is None or not message.text.strip():  # Проверка на пустое сообщение
        bot.send_message(message.chat.id, "Напишіть назву команди текстом)")
        return

    global team_name
    team_name = message.text
    msg = bot.send_message(message.chat.id, "Напишіть хто є в команді) пишіть через кому")
    bot.register_next_step_handler(msg, team_members)

def team_members(message):
    if message.text is None or not message.text.strip():  # Проверка на пустое сообщение
        bot.send_message(message.chat.id, "Напишіть текстом хто є в команді) пишіть через кому")
        return
    text = message.text
    text = text.replace(", ", ",")
    participants = text.split(',')

    data = {
        "name": team_name,
        "creator_user": creator_user,
        "participants": participants,
        "bonus": False,
        "bonus_photo": ""
        }

    _data = json_data("data_konkurs.json")

    _data["commands"].append(data)

    write_json_data("data_konkurs.json", _data)

    bot.send_message(message.chat.id, "Ваша команда успішно додана)")

def get_photo(message):
    succes = True
    user = message.from_user
    user_id = user.id
    if message.content_type == 'photo':
        # Получаем информацию о фото
        file_id = message.photo[-1].file_id
        file_info = bot.get_file(file_id)
        file_path = file_info.file_path
        # Генерируем уникальное имя файла с расширением .jpg
        random_filename = str(uuid.uuid4()) + ".jpg"

        # Загружаем фото
        file_url = f"https://api.telegram.org/file/bot{token}/{file_path}"
        response = requests.get(file_url)
        with open(random_filename, 'wb') as file:
            file.write(response.content)
            markup = telebot.types.InlineKeyboardMarkup()
            yes = telebot.types.InlineKeyboardButton(text="Прийняти ✅", callback_data=f"yes_{user_id}_{random_filename}")
            no = telebot.types.InlineKeyboardButton(text="Відхилити ❌", callback_data=f"not_{user_id}_{random_filename}")
            markup.add(yes,no)
            with open(random_filename, 'rb') as photo:
                bot.send_photo(1004574223, photo, caption=user, reply_markup=markup)

        # Вы можете использовать переменную photo_base64 для дальнейшей обработки
    elif message.content_type == 'document':
        # Если пользователь отправил документ, проверим его тип
        if message.document.file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            # Получаем информацию о документе
            file_id = message.document.file_id
            file_info = bot.get_file(file_id)
            file_path = file_info.file_path
            # Генерируем уникальное имя файла с тем же расширением, что и у документа
            file_extension = message.document.file_name.split('.')[-1]
            random_filename = str(uuid.uuid4()) + "." + file_extension

            # Загружаем документ
            file_url = f"https://api.telegram.org/file/bot{token}/{file_path}"
            response = requests.get(file_url)
            with open(random_filename, 'wb') as file:
                file.write(response.content)
                markup = telebot.types.InlineKeyboardMarkup()
                yes = telebot.types.InlineKeyboardButton(text="Прийняти ✅", callback_data=f"yes_{user_id}_{random_filename}")
                no = telebot.types.InlineKeyboardButton(text="Відхилити ❌", callback_data=f"not_{user_id}_{random_filename}")
                markup.add(yes,no)
                with open(random_filename, 'rb') as photo:
                    bot.send_photo(1004574223, photo, caption=user, reply_markup=markup)

        else:
            # Это файл, но не фото
            bot.send_message(message.chat.id, "Пожалуйста, отправьте фото, а не сторонний файл.")
            False
    else:
        # Пользователь отправил что-то, что не является фото
        # Вы можете отправить ему сообщение с просьбой отправить фото или выполнить другие действия
        bot.send_message(message.chat.id, "Пожалуйста, отправьте фото. Другие типы сообщений не поддерживаются.")
        False

    if succes:
        bot.send_message(message.chat.id, "Фото відвшлено очікуйте)")

@bot.message_handler(commands=['start'])
def command_start(message):
    user = message.from_user
    user_id = user.id
    first_name = user.first_name
    last_name = user.last_name
    username = user.username

    global creator_user
    data = json_data("data_konkurs.json")

    creator_user = {
        "id": user_id,
        "first_name": first_name,
        "last_name": last_name,
        "username": username
    }

    user_exists = False
    for user in data["all_users"]:
        if user.get("id") == user_id:
            user_exists = True
            break

    # Если пользователь не существует, добавляем его
    if not user_exists:
        data["all_users"].append(creator_user)
    write_json_data("data_konkurs.json", data)
    bot.send_message(message.chat.id, f"<b>Привіт {message.from_user.first_name}</b>\n\nЯ радий тебе бачити на Конкурсі <b>тут назва</b>\nГлянь на команди в меню якшо шось трапилось то то напиши йому @marklanselot", parse_mode="HTML")

@bot.message_handler(commands=['new_team'])
def command_new_team(message):
    user = message.from_user
    data = json_data("data_konkurs.json")
    user_id = user.id
    first_name = user.first_name
    last_name = user.last_name
    username = user.username
    global creator_user
    creator_user = {
        "id": user_id,
        "first_name": first_name,
        "last_name": last_name,
        "username": username
    }

    user_exists = False
    for user in data["all_users"]:
        if user.get("id") == user_id:
            user_exists = True
            break

    # Если пользователь не существует, добавляем его
    if not user_exists:
        data["all_users"].append(creator_user)
    write_json_data("data_konkurs.json", data)
    data = json_data("data_konkurs.json")




    user_has_created_command = False
    for command in data["commands"]:
        creator_id = command["creator_user"]["id"]
        if creator_id == user_id:
            user_has_created_command = True
            break
    if user_has_created_command:
        bot.send_message(message.chat.id, "Нажаль ви вже створили команду тому не можете створити ще одну(")
        return



    msg = bot.send_message(message.chat.id, "Напишіть назву команди)")
    bot.register_next_step_handler(msg, name_team)

@bot.message_handler(commands=['teams'])
def command_teams(message):
    user = message.from_user
    user_id = user.id
    first_name = user.first_name
    last_name = user.last_name
    username = user.username

    global creator_user
    data = json_data("data_konkurs.json")

    creator_user = {
        "id": user_id,
        "first_name": first_name,
        "last_name": last_name,
        "username": username
    }

    user_exists = False
    for user in data["all_users"]:
        if user.get("id") == user_id:
            user_exists = True
            break

    # Если пользователь не существует, добавляем его
    if not user_exists:
        data["all_users"].append(creator_user)
    write_json_data("data_konkurs.json", data)
    data = json_data("data_konkurs.json")


    commands = data['commands']
    if not commands:
        bot.send_message(message.chat.id, f"Нажаль покишо ніхто не створив команди але ти можеш стати першим)", parse_mode="HTML")
    else:
        markup = telebot.types.InlineKeyboardMarkup()
        comand_b = telebot.types.InlineKeyboardButton(text="📜 Список команд: 📜", callback_data=" ")
        markup.add(comand_b)
        i = 0
        for team in commands:
            i += 1
            name = team['name']
            comand_b = telebot.types.InlineKeyboardButton(text=f"{i}: {name}", callback_data=f"team_info_{name}")
            markup.add(comand_b)

        bot.send_message(message.chat.id, f"Ось які команди вже є (натисни щоб подивитися подробиці)", parse_mode="HTML", reply_markup=markup)

@bot.message_handler(commands=['get_bonus'])
def command_get_bonus(message):
    user = message.from_user
    data = json_data("data_konkurs.json")
    user_id = user.id
    first_name = user.first_name
    last_name = user.last_name
    username = user.username
    global creator_user
    creator_user = {
        "id": user_id,
        "first_name": first_name,
        "last_name": last_name,
        "username": username
    }

    user_exists = False
    for user in data["all_users"]:
        if user.get("id") == user_id:
            user_exists = True
            break

    # Если пользователь не существует, добавляем его
    if not user_exists:
        data["all_users"].append(creator_user)
    write_json_data("data_konkurs.json", data)
    data = json_data("data_konkurs.json")




    user_has_created_command = True
    for command in data["commands"]:
        creator_id = command["creator_user"]["id"]
        if creator_id == user_id:
            user_has_created_command = False
            break

    team = True
    if user_has_created_command:
        bot.send_message(message.chat.id, "Нажаль ви не створили команду(")
        team = False
    else:
        if command['bonus']:
            bot.send_message(message.chat.id, "Ви вже отримали бонус)")
            team = False

    if team:
        emoji_list = ["🛤", "🛣", "🗾", "🎑", "🏞", "🌆", "🌇", "🎆", "🎇", "🌠", "🌄", "🌅", "🏙", "🌃", "🌌", "🌉", "🌁"]

        # Выбираем случайный emoji
        random_emoji = random.choice(emoji_list)
        bot.send_message(message.chat.id, random_emoji)
        msg = bot.send_message(message.chat.id, f"Пришліть мені фоточку)")
        bot.register_next_step_handler(msg, get_photo)

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if "team_info_" in call.data:
        string = call.data
        prefix = "team_info_"
        name = string[len(prefix):]

        # Проходим по объектам в списке и ищем совпадение
        data = None
        data = json_data("data_konkurs.json")
        for command in data['commands']:
            if 'name' in command and command['name'] == name:
                data = command
                break
        if data:
            markup = telebot.types.InlineKeyboardMarkup()
            name_command = telebot.types.InlineKeyboardButton(text='Назва: ' + data['name'], callback_data=" ")
            creator_user = telebot.types.InlineKeyboardButton(text='Створив: "' + data['creator_user']['first_name'] + '"', callback_data=" ")
            bonus = data['bonus']
            if bonus: bonus = "Отримали бонус ✅"
            else: bonus = "Не отримали бонус ❌"
            bonus = telebot.types.InlineKeyboardButton(text=bonus, callback_data=" ")
            team_name = telebot.types.InlineKeyboardButton(text='Команда:', callback_data=" ")

            markup.add(name_command)
            markup.add(creator_user)
            markup.add(bonus)
            markup.add(team_name)

            i = 0
            for name in data['participants']:
                i += 1
                comand_b = telebot.types.InlineKeyboardButton(text=f"{i}: {name}", callback_data=f"team_info_{name}")
                markup.add(comand_b)

            back1 = telebot.types.InlineKeyboardButton(text=f"◀️", callback_data=f"back1")
            markup.add(back1)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f"Команда {data['name']}", reply_markup=markup)
    elif call.data == "back1":
        data = json_data("data_konkurs.json")
        commands = data['commands']
        if not commands:
            bot.send_message(call.message.chat.id, f"Нажаль покишо ніхто не створив команди але ти можеш стати першим)", parse_mode="HTML")
        else:
            markup = telebot.types.InlineKeyboardMarkup()
            comand_b = telebot.types.InlineKeyboardButton(text="📜 Список команд: 📜", callback_data=" ")
            markup.add(comand_b)
            i = 0
            for team in commands:
                i += 1
                name = team['name']
                comand_b = telebot.types.InlineKeyboardButton(text=f"{i}: {name}", callback_data=f"team_info_{name}")
                markup.add(comand_b)

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f"Ось які команди вже є (натисни щоб подивитися подробиці)", reply_markup=markup)
    elif "yes" in call.data or "not" in call.data:

        text = call.data
        parts = text.split('_')

        user_id = parts[1]
        s = parts[0] + "_" + parts[2]
        parts = s.split('_')
        status = parts[0]
        filename = parts[-1]

        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)
        if status == "not":
            user_id = int(user_id)
            with open(filename, 'rb') as photo:
                markup = telebot.types.InlineKeyboardMarkup()
                no = telebot.types.InlineKeyboardButton(text="Відхилено( ❌", callback_data=f" ")
                markup.add(no)
                bot.send_photo(user_id, photo, reply_markup=markup)
                os.path.exists(filename)
        elif status == "yes":
            data = json_data("data_konkurs.json")
            # Идентификатор, который нужно найти
            target_id = int(user_id)

            # Значение для изменения поля bonus
            new_bonus_value = True

            # Значение для изменения поля bonus_photo
            new_bonus_photo_value = filename

            # Находим и изменяем соответствующий объект
            for command in data["commands"]:
                if command["creator_user"]["id"] == target_id:
                    command["bonus"] = new_bonus_value
                    command["bonus_photo"] = new_bonus_photo_value

            # Записываем измененный объект в файл data_konkurs.json
            with open('data_konkurs.json', 'w', encoding='utf-8') as json_file:
                json.dump(data, json_file, ensure_ascii=False, indent=4)
            user_id = int(user_id)
            with open(filename, 'rb') as photo:
                markup = telebot.types.InlineKeyboardMarkup()
                no = telebot.types.InlineKeyboardButton(text="Прийнято) ✅", callback_data=f" ")
                markup.add(no)
                bot.send_photo(user_id, photo, reply_markup=markup)
            with open(filename, 'rb') as photo:
                markup = telebot.types.InlineKeyboardMarkup()
                no = telebot.types.InlineKeyboardButton(text="Прийнято) ✅", callback_data=f" ")
                markup.add(no)

                data = json_data("data_konkurs.json")
                name__team = "???"
                user_has_created_command = False
                for command in data["commands"]:
                    creator_id = command["creator_user"]["id"]
                    if creator_id == user_id:
                        name__team = command['name']
                        break
                caption = f"id: {call.message.chat.id}\nusername: @{call.message.chat.username}\nname: {call.message.chat.first_name}\nlast_name: {call.message.chat.last_name}\n teat: {name__team}\n\n\n{call.message.chat}"
                bot.send_photo(1004574223, photo, reply_markup=markup, caption=caption)



bot.infinity_polling(timeout=999, long_polling_timeout = 5)