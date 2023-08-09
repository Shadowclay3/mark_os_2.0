import qrcode, random, re, os, telebot, string
from pyzbar.pyzbar import decode
from PIL import Image

'''                                    Тех-підтримка                                        '''
teh_pidtrumka = telebot.types.InlineKeyboardMarkup()
teh_pidtrumka.add(telebot.types.InlineKeyboardButton('Тех підтримка', url="https://t.me/marklanselot"))

def text_to_qr(text, token, message):
    bot = telebot.TeleBot(token)
    # Создаем QR-код с текстом сообщения
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(text)
    qr.make(fit=True)
    # Генерируем изображение QR-кода
    qr_image = qr.make_image(fill_color="black", back_color="white")
    # Сохраняем изображение QR-кода во временный файл
    temp_filename = ''.join(random.choice('0123456789') for _ in range(10))
    temp_filename += ".png"
    qr_image.save(temp_filename)
    # Отправляем изображение QR-кода пользователю
    caption=f"QrCode з текстом: {text}"
    return caption, temp_filename


def qr_to_text(message, token):
    try:
        bot = telebot.TeleBot(token)
        # Получаем информацию о фото
        file_info = bot.get_file(message.photo[-1].file_id)
        file_path = file_info.file_path
                
        # Генерируем случайное имя файла из 10 цифр
        photo_filename = ''.join(random.choices(string.digits, k=10)) + '.jpg'
        photo_path = os.path.join(os.getcwd(), photo_filename)
                
        # Скачиваем фото
        downloaded_file = bot.download_file(file_path)
                
        with open(photo_path, 'wb') as photo:
            photo.write(downloaded_file)
                
        # Расшифровываем QR-код
        qr_code_data = decode(Image.open(photo_path))
        if qr_code_data:
            decoded_text = qr_code_data[0].data.decode('utf-8')
            decoded_text = f'Расшифрованный текст: {decoded_text}'
            return decoded_text, photo_path
        else:
            decoded_text = 'QR-код не найден'
            return decoded_text, photo_path
    except:
        decoded_text = 'Помилонька('
        return decoded_text, photo_path