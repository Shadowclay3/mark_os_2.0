import random, os, telebot
from langdetect import detect
from gtts import gTTS


def generate(text, message, token):
    try:
        # Генерируем случайное имя файла, состоящее из 10 цифр
        bot = telebot.TeleBot(token)
        # Генерируем случайное имя файла, состоящее из 10 цифр
        file_name = ''.join(random.choice('0123456789') for _ in range(10))
        output_file = file_name + ".mp3"
        # Создаем объект gTTS с указанным текстом и языком
        if text.isdigit():
            lang = "ru"  # Используем "ru" для числовых значений
        else:
            try: lang = detect(text)
            except: lang = "ru"
            if lang == "mk": lang = "ru"
            try: lang = detect(text); tts = gTTS(text, lang=lang)
            except: lang = "ru"
        tts = gTTS(text, lang=lang)
        # Сохраняем аудиофайл
        tts.save(output_file)
        # Отправляем аудиофайл
        bot.delete_message(chat_id=message.chat.id, message_id=message.id+1)
        with open(output_file, 'rb') as audio:
            bot.send_voice(message.chat.id, audio)
        # Закрываем файл и удаляем его
        audio.close()
        os.remove(output_file)
    except Exception as e:
        bot.send_message(message.chat.id, e)