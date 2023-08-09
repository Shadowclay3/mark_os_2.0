import speech_recognition as sr
import subprocess, requests, os, telebot, json

def audio_to_text(dest_name: str):
    # Функция для перевода аудио, в формате ".vaw" в текст
    r = sr.Recognizer() # такое вообще надо комментить?
    # тут мы читаем наш .vaw файл
    message = sr.AudioFile(dest_name)
    with message as source:
        audio = r.record(source)
    result = r.recognize_google(audio, language="uk_UK") # используя возможности библиотеки распознаем текст, так же тут можно изменять язык распознавания
    return result

def voice_to_text(message, token):
    try:
        bot = telebot.TeleBot(token)
        file_info = bot.get_file(message.voice.file_id)
        path = file_info.file_path
        fname = os.path.basename(path)
        doc = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(token, file_info.file_path))
        with open(fname+'.oga', 'wb') as f:
            f.write(doc.content)
        process = subprocess.run(['ffmpeg', '-i', fname+'.oga', fname+'.wav'])
        result = audio_to_text(fname+'.wav')
        text_voice = format(result)
        status = True
    except sr.UnknownValueError as e:
        status = False
        # Ошибка возникает, если сообщение не удалось разобрать. В таком случае отсылается ответ пользователю и заносим запись в лог ошибок
        text_voice =  "Перепрошую, але я не розібрав повідомлення, або воно пусте..."
    except Exception as e:
        status = False
        # В случае возникновения любой другой ошибки, отправляется соответствующее сообщение пользователю и заносится запись в лог ошибок
        text_voice = "Щось пішло не так, але наші сміливі програмісти вже працюють над рішенням... \n\nТа лан, ніхто цю помилку виправляти не буде, вона просто загубиться в логах."
    finally:
        # В любом случае удаляем временные файлы с аудио сообщением
        try: os.remove(fname+'.wav')
        except: pass
        try: os.remove(fname+'.oga')
        except: pass
    return text_voice, status

def start(user_id):
    default_config = \
{
    "text": "midjourney",
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
    button_1 = types.KeyboardButton(text=" ")
    button_2 = types.KeyboardButton(text="⏹")
    button_3 = types.KeyboardButton(text=" ")
    reply_markup.add(button_1, button_2, button_3)
    stroka_sostoyaniya = "*голосове 🔄 текст:*"
    return stroka_sostoyaniya, reply_markup