import random, json, time, string, requests, os
from telebot import types
url = "https://wewordle.org/gptapi/v1/android/turbo"
supports_stream = False
needs_auth = False


def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    base = ''
    for message in messages:
        base += '%s: %s\n' % (message['role'], message['content'])
    base += 'assistant:'
    # randomize user id and app id
    _user_id = ''.join(random.choices(f'{string.ascii_lowercase}{string.digits}', k=16))
    _app_id = ''.join(random.choices(f'{string.ascii_lowercase}{string.digits}', k=31))
    # make current date with format utc
    _request_date = time.strftime("%Y-%m-%dT%H:%M:%S.000Z", time.gmtime())
    headers = {
        'accept': '*/*',
        'pragma': 'no-cache',
        'Content-Type': 'application/json',
        'Connection':'keep-alive'
        # user agent android client
        # 'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 10; SM-G975F Build/QP1A.190711.020)',
        
    }
    data = {
        "user": _user_id,
        "messages": [
            {"role": "user", "content": base}
        ],
        "subscriber": {
            "originalPurchaseDate": None,
            "originalApplicationVersion": None,
            "allPurchaseDatesMillis": {},
            "entitlements": {
                "active": {},
                "all": {}
            },
            "allPurchaseDates": {},
            "allExpirationDatesMillis": {},
            "allExpirationDates": {},
            "originalAppUserId": f"$RCAnonymousID:{_app_id}",
            "latestExpirationDate": None,
            "requestDate": _request_date,
            "latestExpirationDateMillis": None,
            "nonSubscriptionTransactions": [],
            "originalPurchaseDateMillis": None,
            "managementURL": None,
            "allPurchasedProductIdentifiers": [],
            "firstSeen": _request_date,
            "activeSubscriptions": []
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        _json = response.json()
        if 'message' in _json:
            yield _json['message']['content']
    else:
        return "error"

# Temporary For ChatCompletion Class
class ChatCompletion:
    @staticmethod
    def create(model: str, messages: list, provider: None or str, stream: bool = False, auth: str = False, **kwargs):
        kwargs['auth'] = auth
        if provider and needs_auth and not auth:
            return "error"
        try:
            return (_create_completion(model, messages, stream, **kwargs)
                    if stream else ''.join(_create_completion(model, messages, stream, **kwargs)))
        except:
            return "error"
        
def ask(chat: list):
    start_time = time.time()
    answer_ai = ChatCompletion.create(model='gpt-4', provider="BingHuan", messages=chat, stream=False)
    prefix = "assistant: "
    if answer_ai.startswith(prefix) or answer_ai.startswith(prefix.capitalize()): answer_ai = answer_ai[len(prefix):]
    prefix = "**assistant:** "
    if answer_ai.startswith(prefix) or answer_ai.startswith(prefix.capitalize()): answer_ai = answer_ai[len(prefix):]
    end_time = time.time()
    elapsed_time = end_time - start_time
    if elapsed_time < 60: response = f"⏱*Ответ найден за {int(elapsed_time)}sec.*\n________________________________\n{answer_ai}"
    else:
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        response = f"⏱*Ответ найден за {minutes}min. {seconds}sec.*\n______________________________\n{answer_ai}"
    return answer_ai, response



def Gpt(user_id):
    default_config = \
{
    "text": "Gpt",
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
    from telebot import types
    reply_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start = types.KeyboardButton(text="/start - Оримати початкове повідомлення")
    setting = types.KeyboardButton(text="/setting - Налаштування для керування AI та чатами")
    clean_chat = types.KeyboardButton(text="/clean_chat - Почистити історію вашого спілкування з AI")
    help_ = types.KeyboardButton(text="/help - Як використовувати")
    button_1 = types.KeyboardButton(text=" ")
    button_2 = types.KeyboardButton(text="⏹")
    button_3 = types.KeyboardButton(text=" ")
    reply_markup.add(start)
    reply_markup.add(setting)
    reply_markup.add(clean_chat)
    reply_markup.add(help_)
    reply_markup.add(button_1, button_2, button_3)
    stroka_sostoyaniya = "*ChatGPT:*"
    return stroka_sostoyaniya, reply_markup

'''                                      Ролі                                          '''
roles = types.InlineKeyboardMarkup()
bez_roles = types.InlineKeyboardButton(                text="🚫🎭 без ролей",       callback_data='role_bez_roles')
Matematuk = types.InlineKeyboardButton(                text="🧮 Математик",         callback_data='role_Matematuk')
Ruskij = types.InlineKeyboardButton(                   text="🇷🇺 Росіянин",           callback_data='role_Ruskij')
Secret_Agent = types.InlineKeyboardButton(             text="🕵️‍♂️ Секретний Агент",   callback_data='role_Secret_Agent')
Doctor = types.InlineKeyboardButton(                   text="👨‍⚕️ Доктор",            callback_data='role_Doctor')
Poet = types.InlineKeyboardButton(                     text="📜 Поет",              callback_data='role_Poet')
Child = types.InlineKeyboardButton(                    text="👶 Дитя",              callback_data='role_Child')
Super_Programer = types.InlineKeyboardButton(          text="👨‍💻 супер Прогроміст",  callback_data='role_Super_Programer')
roles.add(bez_roles, Matematuk)
roles.add(Ruskij, Secret_Agent)
roles.add(Doctor, Poet)
roles.add(Child, Super_Programer)


'''                                    Тех-підтримка                                        '''
teh_pidtrumka = types.InlineKeyboardMarkup()
teh_pidtrumka.add(types.InlineKeyboardButton('Тех підтримка', url="https://t.me/marklanselot"))


def command_start(message, bot):
    bot.send_message(message.chat.id, '<b>Здоровеькы були! 👋\n\nЦей бот 🤖 власність @marklanselot</b>', parse_mode='HTML')
    bot.send_message(message.chat.id, "<b>Якщо виникли питання подивисьно в меню та обери команду\n\n/help\n\nЯ спробую тобі допомогти)</b>", parse_mode='HTML')
    bot.send_message(message.chat.id, "<b>Якщо бот не працює напиши в тех підтримку нижче</b>", reply_markup=teh_pidtrumka, parse_mode='HTML')

def command_setting(message, bot):
    default_config = { "GPT":{ "history_chat": False, "response_time": False }}
    # Проверяем наличие файла
    if not os.path.exists(f"user_config/setting/{message.chat.id}.json"):
        # Создаем файл и записываем данные
        with open(f"user_config/setting/{message.chat.id}.json", "w") as file:
            json.dump(default_config, file)

    # Читаем данные из файла
    with open(f"user_config/setting/{message.chat.id}.json", "r") as file:
        config = json.load(file)
    set1 = config['GPT']['history_chat']; set2 = config['GPT']['response_time']
    if set1 == True: set1 = "✅"
    else: set1 = "❌"
    if set2 == True: set2 = "✅"
    else: set2 = "❌"

    '''                                    Налаштування                                   '''
    setting = types.InlineKeyboardMarkup()
    setting.add(types.InlineKeyboardButton(         f"Вимкнути пам'ять в AI? | {set1}"           ,callback_data='set1'))
    setting.add(types.InlineKeyboardButton(  f"Писати за який час дана відповідь? | {set2}"      ,callback_data='set2'))
    bot.send_message(message.chat.id, "⚙️ <b>Налаштування:</b> ⚙️", reply_markup=setting, parse_mode='HTML')

def command_clean_chat(message, bot):
    bot.send_message(message.chat.id, "🧹 <b>Чат очищено!</b> 🧹", parse_mode='HTML')

def command_help(message, bot):
    bot.send_message(message.chat.id, "/start - Оримати <b>початкове повідомлення</b>\n\n/setting - <b>Налаштування</b> для керування AI та чатами\n\n/clean_chat - <b>Почистити історію</b> вашого спілкування з AI\n\n/roles - Меню для вибору <b>ролі</b> для AI\n\nпросто <b>напиши</b> своє питання",  parse_mode="HTML")