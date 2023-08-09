import json, os

def proverka_files(files):
    try:
        # Перевірка наявності кожної папки/файла
        for file in files:
            if ".json" in file :
                if not os.path.exists(file):
                    # Створення папки/файла
                    open(file, 'a', encoding='utf-8').close()
                    # Добавлення змісту до файлу
                    with open(file, 'w', encoding='utf-8') as f:
                        json.dump({}, f)
                    print(f'{file} | створено')
            else:
                if not os.path.exists(file):
                    os.mkdir(file)
                    
    except: return False
    else: return True


def proverka_list_user(user_id, first_name, last_name, user_name):
    # Завантаження даних з users_info.json
    with open('users_info.json', 'r', encoding='utf-8') as file:
        users_info = json.load(file)
    new_user = {
            f'user_{user_id}': {
                    'first_name': first_name,
                    'last_name': last_name,
                    'user_name': user_name,
                    'user_id': str(user_id),
                }
            }
    try: user = users_info[f"user_{user_id}"]
    except:
        # Користувача немає, додавання нового користувача
        
        users_info.update(new_user)

        # Запис даних знову в users_info.json з ensure_ascii=False
        with open('users_info.json', 'w', encoding='utf-8') as file:
                json.dump(users_info, file, ensure_ascii=False)
        status=True
        return new_user, status
        
    else:
        status=False
        return new_user, status
