import json, os, subprocess

def Gpt(user_id):
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
    stroka_sostoyaniya = "*midjourney:*"
    return stroka_sostoyaniya, reply_markup

def generate(prompt, folder):
    import time
    start_time = time.time()
    try:
        # Команда запуска питон файла с параметрами
        command = ["python", "apps/midjourney_generate.py", "--prompt", prompt, "--cookie-file", "cookies.json", "--output-dir", folder]
        process = subprocess.run(command, capture_output=True, text=True)
        status = True
    except : status = False
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time, status