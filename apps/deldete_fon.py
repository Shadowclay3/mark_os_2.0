import telebot, os, json, random, string
from rembg import remove
from PIL import Image
from PIL import UnidentifiedImageError

def convert(token, message, teh_pidtrumka):
    try:
        random_name = ''.join(random.choices(string.ascii_lowercase, k=10))
        bot = telebot.TeleBot(token)
        # Получаем фотографию из сообщения
        photo = message.photo[-1].file_id
        
        # Скачиваем фотографию
        file_info = bot.get_file(photo)
        downloaded_file = bot.download_file(file_info.file_path)
        
        # Сохраняем фотографию на сервере
        photo_path = f'{random_name}.jpg'
        with open(photo_path, 'wb') as f:
            f.write(downloaded_file)
        
        # Загружаем фотографию
        open_image = Image.open(photo_path)
        
        # Удаляем фон
        result = remove(open_image)
        
        # Сохраняем результат
        result_path = f'{random_name}.png'
        result.save(result_path)
        
        # Отправляем результат пользователю
        with open(result_path, 'rb') as f:
            bot.send_photo(message.chat.id, f)
        
        # Удаляем временные файлы
        os.remove(photo_path)
        os.remove(result_path)
    except UnidentifiedImageError as e:
        # Если возникла ошибка с чтением изображения
        bot.send_message(message.chat.id, "Виникла помилка при обробці зображення. Переконайтеся, що це зображення підтримується (наприклад, JPEG або PNG).")
    except Exception as e:
        # Если возникла другая ошибка
        bot.send_message(message.chat.id, "Відбулася непередбачена помилка. Будь ласка, спробуйте ще раз пізніше.", reply_markup=teh_pidtrumka)

        
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
    stroka_sostoyaniya = "*Прибрати фон:*"
    return stroka_sostoyaniya, reply_markup