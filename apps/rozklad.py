from datetime import datetime, time
from telebot import types

week_colors = {
    0: 'жовта',
    1: 'синя'
}

def rozklad():
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        week_number = datetime.today().isocalendar()[1]
        current_week = week_number % 2
        if current_week == 0:
            current_week = 1
        else:
            current_week = 2
        if week_colors[current_week - 1] == "синя": yaka_nedilya = "Синя"
        elif week_colors[current_week - 1] == "жовта": yaka_nedilya = "Жовта"
        else:
            pass
        sms = types.InlineKeyboardMarkup()
        pustota = types.InlineKeyboardButton(text=" ", callback_data = ' ')
        button_1 = types.InlineKeyboardButton(text=" ", callback_data = ' ')
        button_2 = types.InlineKeyboardButton(text="⏹", callback_data = '⏹')
        button_3 = types.InlineKeyboardButton(text=" ", callback_data = ' ')
        today = datetime.today().strftime('%A')

        web_biologia = "https://meet.google.com/rbc-nert-fda?authuser=1&hs=179"
        web_istoruk = "https://meet.google.com/mux-ityd-oxe?authuser=1&hs=179"
        web_math = "https://meet.google.com/kmx-ivom-vun?authuser=1&hs=179"
        web_fizra = "https://meet.google.com/jsk-diap-zrb?authuser=1&hs=179"
        web_vsesvit = "https://meet.google.com/boj-xtkz-wfy?authuser=1&hs=179"
        web_ukr_mova = "https://meet.google.com/gjh-jozr-buf?authuser=1&hs=179"
        web_fizuka = "https://meet.google.com/dph-kqsk-afv?authuser=1&hs=179"
        web_zarub_lit = "https://meet.google.com/oup-zwcz-isn?authuser=1&hs=179"
        web_zahust_ukrain = "https://meet.google.com/bjo-ycnv-kwr?authuser=1&hs=179"
        web_ukr_lit = "https://meet.google.com/zqe-pkiz-jmv?authuser=1&hs=179"
        web_ximia = "https://meet.google.com/kni-tzvi-ina?authuser=1&hs=179"
        web_lyduna_i_svit = "https://meet.google.com/paq-hjko-srn?authuser=1&hs=179"
        today = datetime.today().strftime('%A')
        if today == 'Monday' or today == 'Tuesday' or today == 'Wednesday' or today == 'Thursday' or today == 'Friday':
            if now.time() > time(hour=15, minute=30):
                if today == 'Monday'   : today = 'Tuesday'
                elif today == 'Tuesday'  : today = 'Wednesday'
                elif today == 'Wednesday': today = 'Thursday'
                elif today == 'Thursday' : today = 'Friday'
                elif today == 'Friday'   : today = 'Monday'
                day_next = True
            else:
                day_next = False
        else: day_next = False
        if today == 'Monday':
                day_name = "Пн" + f" | {yaka_nedilya}"
                day_name_b = types.InlineKeyboardButton(text=day_name, callback_data = ' ')
                sms.add(day_name_b)

                predmet1_text = "🦍 Біологія 🚶‍♂️"
                predmet2_text = "🏴󠁧󠁢󠁥󠁮󠁧󠁿 інгліш 🏴󠁧󠁢󠁥󠁮󠁧󠁿"
                predmet3_text = "🇺🇦 Істор.Укp 🇺🇦"
                predmet4_text = "📢 Майдан 📢"

                if day_next == True:
                    time1 = time(hour=9, minute=00)
                    now = datetime.now().time()
                    now_datetime = datetime.combine(datetime.now().date(), now)
                    time1_datetime = datetime.combine(datetime.now().date(), time1)
                    time_diff_seconds = (now_datetime - time1_datetime).total_seconds()
                    if time_diff_seconds >= 3600:
                        hours, remainder = divmod(int(time_diff_seconds), 3600)
                        minutes, seconds = divmod(remainder, 60)
                        time_diff_seconds = str(hours) + "h | " + str(minutes) + "min | " + str(seconds) + "sec."
                    elif time_diff_seconds > 60:
                        minutes, seconds = divmod(int(time_diff_seconds), 60)
                        time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                    else:
                        time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                        
                    predmet1_text = str(time_diff_seconds) + " | " + predmet1_text
                else:
                    if now.time() < time(hour=10, minute=20):
                        if now.time() < time(hour=9, minute=00): 
                            time1 = time(hour=9, minute=00)
                            now = datetime.now().time()
                            now_datetime = datetime.combine(datetime.now().date(), now)
                            time1_datetime = datetime.combine(datetime.now().date(), time1)
                            time_diff_seconds = (time1_datetime - now_datetime).total_seconds()
                            if time_diff_seconds >= 3600:
                                hours, remainder = divmod(int(time_diff_seconds), 3600)
                                minutes, seconds = divmod(remainder, 60)
                                time_diff_seconds = str(hours) + "h | " + str(minutes) + "min | " + str(seconds) + "sec."
                            elif time_diff_seconds > 60:
                                minutes, seconds = divmod(int(time_diff_seconds), 60)
                                time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                            else:
                                time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                            predmet1_text = str(time_diff_seconds) + " | " + predmet1_text
                        else:
                            time1 = time(hour=10, minute=20)
                            now = datetime.now().time()
                            now_datetime = datetime.combine(datetime.now().date(), now)
                            time1_datetime = datetime.combine(datetime.now().date(), time1)
                            time_diff_seconds = (time1_datetime - now_datetime).total_seconds()
                            if time_diff_seconds > 60:
                                minutes, seconds = divmod(int(time_diff_seconds), 60)
                                time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                            else:
                                time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                            predmet1_text = "зараз | " + predmet1_text + " | " + str(time_diff_seconds)
                                
                    elif now.time() < time(hour=12, minute=00) :
                        if now.time() < time(hour=10, minute=40):
                            time1 = time(hour=10, minute=40)
                            now = datetime.now().time()
                            now_datetime = datetime.combine(datetime.now().date(), now)
                            time1_datetime = datetime.combine(datetime.now().date(), time1)
                            time_diff_seconds = (time1_datetime - now_datetime).total_seconds()
                            if time_diff_seconds > 60:
                                minutes, seconds = divmod(int(time_diff_seconds), 60)
                                time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                            else:
                                time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                            predmet2_text = str(time_diff_seconds) + " | " + predmet2_text
                        else:
                            time1 = time(hour=12, minute=00)
                            now = datetime.now().time()
                            now_datetime = datetime.combine(datetime.now().date(), now)
                            time1_datetime = datetime.combine(datetime.now().date(), time1)
                            time_diff_seconds = (time1_datetime - now_datetime).total_seconds()
                            if time_diff_seconds > 60:
                                minutes, seconds = divmod(int(time_diff_seconds), 60)
                                time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                            else:
                                time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                            predmet2_text = "зараз | " + predmet2_text + " | " + str(time_diff_seconds)
                                
                    elif now.time() < time(hour=13, minute=50) :
                        if now.time() < time(hour=12, minute=30):
                            time1 = time(hour=12, minute=30)
                            now = datetime.now().time()
                            now_datetime = datetime.combine(datetime.now().date(), now)
                            time1_datetime = datetime.combine(datetime.now().date(), time1)
                            time_diff_seconds = (time1_datetime - now_datetime).total_seconds()
                            if time_diff_seconds > 60:
                                minutes, seconds = divmod(int(time_diff_seconds), 60)
                                time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                            else:
                                time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                            predmet3_text = str(time_diff_seconds) + " | " + predmet3_text
                        else:
                            time1 = time(hour=13, minute=50)
                            now = datetime.now().time()
                            now_datetime = datetime.combine(datetime.now().date(), now)
                            time1_datetime = datetime.combine(datetime.now().date(), time1)
                            time_diff_seconds = (time1_datetime - now_datetime).total_seconds()
                            if time_diff_seconds > 60:
                                minutes, seconds = divmod(int(time_diff_seconds), 60)
                                time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                            else:
                                time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                            predmet3_text = "зараз | " + predmet3_text + " | " + str(time_diff_seconds)

                    elif now.time() < time(hour=15, minute=30) :
                        if now.time() < time(hour=14, minute=10): 
                            time1 = time(hour=14, minute=10)
                            now = datetime.now().time()
                            now_datetime = datetime.combine(datetime.now().date(), now)
                            time1_datetime = datetime.combine(datetime.now().date(), time1)
                            time_diff_seconds = (time1_datetime - now_datetime).total_seconds()
                            if time_diff_seconds > 60:
                                minutes, seconds = divmod(int(time_diff_seconds), 60)
                                time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                            else:
                                time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                            predmet4_text = str(time_diff_seconds) + " | " + predmet4_text
                        else:
                            time1 = time(hour=15, minute=30)
                            now = datetime.now().time()
                            now_datetime = datetime.combine(datetime.now().date(), now)
                            time1_datetime = datetime.combine(datetime.now().date(), time1)
                            time_diff_seconds = (time1_datetime - now_datetime).total_seconds()
                            if time_diff_seconds > 60:
                                minutes, seconds = divmod(int(time_diff_seconds), 60)
                                time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                            else:
                                time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                            predmet4_text = "зараз | " + predmet4_text + " | " + str(time_diff_seconds)

                predmet1 = types.InlineKeyboardButton(text=predmet1_text, url=web_biologia)
                predmet2 = types.InlineKeyboardButton(text=predmet2_text, callback_data = ' ')
                predmet3 = types.InlineKeyboardButton(text=predmet3_text, url=web_istoruk)
                predmet4 = types.InlineKeyboardButton(text=predmet4_text, url=web_math)
                sms.add(predmet1)
                sms.add(predmet2)
                sms.add(predmet3)
                sms.add(predmet4)
        elif today == 'Tuesday':
                day_name = "Пн" + f" | {yaka_nedilya}"
                day_name_b = types.InlineKeyboardButton(text=day_name, callback_data = ' ')
                sms.add(day_name_b)

                predmet1_text = "⚽️ Фізра 🏀"
                predmet2_text = "📈 Комп.Графіка 📉"
                predmet3_text = "📐 Математика 📏"
                predmet4_text = "🌎 Всесвіт.Істор 🌎"

                if day_next == True:
                    time1 = time(hour=9, minute=00)
                    now = datetime.now().time()
                    now_datetime = datetime.combine(datetime.now().date(), now)
                    time1_datetime = datetime.combine(datetime.now().date(), time1)
                    time_diff_seconds = (now_datetime - time1_datetime).total_seconds()
                    if time_diff_seconds >= 3600:
                        hours, remainder = divmod(int(time_diff_seconds), 3600)
                        minutes, seconds = divmod(remainder, 60)
                        time_diff_seconds = str(hours) + "h | " + str(minutes) + "min | " + str(seconds) + "sec."
                    elif time_diff_seconds > 60:
                        minutes, seconds = divmod(int(time_diff_seconds), 60)
                        time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                    else:
                        time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                        
                    predmet1_text = str(time_diff_seconds) + " | " + predmet1_text
                else:
                    if now.time() < time(hour=10, minute=20):
                        if now.time() < time(hour=9, minute=00): 
                            time1 = time(hour=9, minute=00)
                            now = datetime.now().time()
                            now_datetime = datetime.combine(datetime.now().date(), now)
                            time1_datetime = datetime.combine(datetime.now().date(), time1)
                            time_diff_seconds = (time1_datetime - now_datetime).total_seconds()
                            if time_diff_seconds >= 3600:
                                hours, remainder = divmod(int(time_diff_seconds), 3600)
                                minutes, seconds = divmod(remainder, 60)
                                time_diff_seconds = str(hours) + "h | " + str(minutes) + "min | " + str(seconds) + "sec."
                            elif time_diff_seconds > 60:
                                minutes, seconds = divmod(int(time_diff_seconds), 60)
                                time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                            else:
                                time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                            predmet1_text = str(time_diff_seconds) + " | " + predmet1_text
                        else:
                            time1 = time(hour=10, minute=20)
                            now = datetime.now().time()
                            now_datetime = datetime.combine(datetime.now().date(), now)
                            time1_datetime = datetime.combine(datetime.now().date(), time1)
                            time_diff_seconds = (time1_datetime - now_datetime).total_seconds()
                            if time_diff_seconds > 60:
                                minutes, seconds = divmod(int(time_diff_seconds), 60)
                                time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                            else:
                                time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                            predmet1_text = "зараз | " + predmet1_text + " | " + str(time_diff_seconds)
                                
                    elif now.time() < time(hour=12, minute=00) :
                        if now.time() < time(hour=10, minute=40):
                            time1 = time(hour=10, minute=40)
                            now = datetime.now().time()
                            now_datetime = datetime.combine(datetime.now().date(), now)
                            time1_datetime = datetime.combine(datetime.now().date(), time1)
                            time_diff_seconds = (time1_datetime - now_datetime).total_seconds()
                            if time_diff_seconds > 60:
                                minutes, seconds = divmod(int(time_diff_seconds), 60)
                                time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                            else:
                                time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                            predmet2_text = str(time_diff_seconds) + " | " + predmet2_text
                        else:
                            time1 = time(hour=12, minute=00)
                            now = datetime.now().time()
                            now_datetime = datetime.combine(datetime.now().date(), now)
                            time1_datetime = datetime.combine(datetime.now().date(), time1)
                            time_diff_seconds = (time1_datetime - now_datetime).total_seconds()
                            if time_diff_seconds > 60:
                                minutes, seconds = divmod(int(time_diff_seconds), 60)
                                time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                            else:
                                time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                            predmet2_text = "зараз | " + predmet2_text + " | " + str(time_diff_seconds)
                                
                    elif now.time() < time(hour=13, minute=50) :
                        if now.time() < time(hour=12, minute=30):
                            time1 = time(hour=12, minute=30)
                            now = datetime.now().time()
                            now_datetime = datetime.combine(datetime.now().date(), now)
                            time1_datetime = datetime.combine(datetime.now().date(), time1)
                            time_diff_seconds = (time1_datetime - now_datetime).total_seconds()
                            if time_diff_seconds > 60:
                                minutes, seconds = divmod(int(time_diff_seconds), 60)
                                time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                            else:
                                time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                            predmet3_text = str(time_diff_seconds) + " | " + predmet3_text
                        else:
                            time1 = time(hour=13, minute=50)
                            now = datetime.now().time()
                            now_datetime = datetime.combine(datetime.now().date(), now)
                            time1_datetime = datetime.combine(datetime.now().date(), time1)
                            time_diff_seconds = (time1_datetime - now_datetime).total_seconds()
                            if time_diff_seconds > 60:
                                minutes, seconds = divmod(int(time_diff_seconds), 60)
                                time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                            else:
                                time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                            predmet3_text = "зараз | " + predmet3_text + " | " + str(time_diff_seconds)

                    elif now.time() < time(hour=15, minute=30) :
                        if now.time() < time(hour=14, minute=10): 
                            time1 = time(hour=14, minute=10)
                            now = datetime.now().time()
                            now_datetime = datetime.combine(datetime.now().date(), now)
                            time1_datetime = datetime.combine(datetime.now().date(), time1)
                            time_diff_seconds = (time1_datetime - now_datetime).total_seconds()
                            if time_diff_seconds > 60:
                                minutes, seconds = divmod(int(time_diff_seconds), 60)
                                time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                            else:
                                time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                            predmet4_text = str(time_diff_seconds) + " | " + predmet4_text
                        else:
                            time1 = time(hour=15, minute=30)
                            now = datetime.now().time()
                            now_datetime = datetime.combine(datetime.now().date(), now)
                            time1_datetime = datetime.combine(datetime.now().date(), time1)
                            time_diff_seconds = (time1_datetime - now_datetime).total_seconds()
                            if time_diff_seconds > 60:
                                minutes, seconds = divmod(int(time_diff_seconds), 60)
                                time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                            else:
                                time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                            predmet4_text = "зараз | " + predmet4_text + " | " + str(time_diff_seconds)
                
                predmet1 = types.InlineKeyboardButton(text=predmet1_text, url=web_fizra)
                predmet2 = types.InlineKeyboardButton(text=predmet2_text, callback_data = ' ')
                predmet3 = types.InlineKeyboardButton(text=predmet3_text, url=web_math)
                predmet4 = types.InlineKeyboardButton(text=predmet4_text, url=web_vsesvit) 
                sms.add(predmet1)
                sms.add(predmet2)
                sms.add(predmet3)
                sms.add(predmet4)
        elif today == 'Wednesday':
                day_name = "Пн" + f" | {yaka_nedilya}"
                day_name_b = types.InlineKeyboardButton(text=f"{day_name} | {yaka_nedilya}", callback_data = ' ')
                sms.add(day_name_b)
                if yaka_nedilya == "Жовта":
                    predmet1_text = "🇺🇦 Укр.мова 🇺🇦"
                    predmet2_text = "📱 Технології 💻"
                    predmet3_text = "🧲 Фізика 🔌"
                    predmet4_text = "🌎 Заруб.літ 🌎"
                else:
                    predmet1_text = "🇺🇦 Укр.мова 🇺🇦"
                    predmet2_text = "📱 Технології 💻"
                    predmet3_text = "🧲 Фізика 🔌"
                    predmet4_text = "🇺🇦 Захист України 🇺🇦"

                
                if day_next == True:
                    time1 = time(hour=9, minute=00)
                    now = datetime.now().time()
                    now_datetime = datetime.combine(datetime.now().date(), now)
                    time1_datetime = datetime.combine(datetime.now().date(), time1)
                    time_diff_seconds = (now_datetime - time1_datetime).total_seconds()
                    if time_diff_seconds >= 3600:
                        hours, remainder = divmod(int(time_diff_seconds), 3600)
                        minutes, seconds = divmod(remainder, 60)
                        time_diff_seconds = str(hours) + "h | " + str(minutes) + "min | " + str(seconds) + "sec."
                    elif time_diff_seconds > 60:
                        minutes, seconds = divmod(int(time_diff_seconds), 60)
                        time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                    else:
                        time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                        
                    predmet1_text = str(time_diff_seconds) + " | " + predmet1_text
                else:
                    if now.time() < time(hour=10, minute=20):
                        if now.time() < time(hour=9, minute=00): 
                            time1 = time(hour=9, minute=00)
                            now = datetime.now().time()
                            now_datetime = datetime.combine(datetime.now().date(), now)
                            time1_datetime = datetime.combine(datetime.now().date(), time1)
                            time_diff_seconds = (time1_datetime - now_datetime).total_seconds()
                            if time_diff_seconds >= 3600:
                                hours, remainder = divmod(int(time_diff_seconds), 3600)
                                minutes, seconds = divmod(remainder, 60)
                                time_diff_seconds = str(hours) + "h | " + str(minutes) + "min | " + str(seconds) + "sec."
                            elif time_diff_seconds > 60:
                                minutes, seconds = divmod(int(time_diff_seconds), 60)
                                time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                            else:
                                time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                            predmet1_text = str(time_diff_seconds) + " | " + predmet1_text
                        else:
                            time1 = time(hour=10, minute=20)
                            now = datetime.now().time()
                            now_datetime = datetime.combine(datetime.now().date(), now)
                            time1_datetime = datetime.combine(datetime.now().date(), time1)
                            time_diff_seconds = (time1_datetime - now_datetime).total_seconds()
                            if time_diff_seconds > 60:
                                minutes, seconds = divmod(int(time_diff_seconds), 60)
                                time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                            else:
                                time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                            predmet1_text = "зараз | " + predmet1_text + " | " + str(time_diff_seconds)
                                
                    elif now.time() < time(hour=12, minute=00) :
                        if now.time() < time(hour=10, minute=40):
                            time1 = time(hour=10, minute=40)
                            now = datetime.now().time()
                            now_datetime = datetime.combine(datetime.now().date(), now)
                            time1_datetime = datetime.combine(datetime.now().date(), time1)
                            time_diff_seconds = (time1_datetime - now_datetime).total_seconds()
                            if time_diff_seconds > 60:
                                minutes, seconds = divmod(int(time_diff_seconds), 60)
                                time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                            else:
                                time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                            predmet2_text = str(time_diff_seconds) + " | " + predmet2_text
                        else:
                            time1 = time(hour=12, minute=00)
                            now = datetime.now().time()
                            now_datetime = datetime.combine(datetime.now().date(), now)
                            time1_datetime = datetime.combine(datetime.now().date(), time1)
                            time_diff_seconds = (time1_datetime - now_datetime).total_seconds()
                            if time_diff_seconds > 60:
                                minutes, seconds = divmod(int(time_diff_seconds), 60)
                                time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                            else:
                                time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                            predmet2_text = "зараз | " + predmet2_text + " | " + str(time_diff_seconds)
                                
                    elif now.time() < time(hour=13, minute=50) :
                        if now.time() < time(hour=12, minute=30):
                            time1 = time(hour=12, minute=30)
                            now = datetime.now().time()
                            now_datetime = datetime.combine(datetime.now().date(), now)
                            time1_datetime = datetime.combine(datetime.now().date(), time1)
                            time_diff_seconds = (time1_datetime - now_datetime).total_seconds()
                            if time_diff_seconds > 60:
                                minutes, seconds = divmod(int(time_diff_seconds), 60)
                                time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                            else:
                                time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                            predmet3_text = str(time_diff_seconds) + " | " + predmet3_text
                        else:
                            time1 = time(hour=13, minute=50)
                            now = datetime.now().time()
                            now_datetime = datetime.combine(datetime.now().date(), now)
                            time1_datetime = datetime.combine(datetime.now().date(), time1)
                            time_diff_seconds = (time1_datetime - now_datetime).total_seconds()
                            if time_diff_seconds > 60:
                                minutes, seconds = divmod(int(time_diff_seconds), 60)
                                time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                            else:
                                time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                            predmet3_text = "зараз | " + predmet3_text + " | " + str(time_diff_seconds)

                    elif now.time() < time(hour=15, minute=30) :
                        if now.time() < time(hour=14, minute=10): 
                            time1 = time(hour=14, minute=10)
                            now = datetime.now().time()
                            now_datetime = datetime.combine(datetime.now().date(), now)
                            time1_datetime = datetime.combine(datetime.now().date(), time1)
                            time_diff_seconds = (time1_datetime - now_datetime).total_seconds()
                            if time_diff_seconds > 60:
                                minutes, seconds = divmod(int(time_diff_seconds), 60)
                                time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                            else:
                                time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                            predmet4_text = str(time_diff_seconds) + " | " + predmet4_text
                        else:
                            time1 = time(hour=15, minute=30)
                            now = datetime.now().time()
                            now_datetime = datetime.combine(datetime.now().date(), now)
                            time1_datetime = datetime.combine(datetime.now().date(), time1)
                            time_diff_seconds = (time1_datetime - now_datetime).total_seconds()
                            if time_diff_seconds > 60:
                                minutes, seconds = divmod(int(time_diff_seconds), 60)
                                time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                            else:
                                time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                            predmet4_text = "зараз | " + predmet4_text + " | " + str(time_diff_seconds)

                predmet1 = types.InlineKeyboardButton(text=predmet1_text, url=web_biologia)
                predmet2 = types.InlineKeyboardButton(text=predmet2_text, callback_data = ' ')
                predmet3 = types.InlineKeyboardButton(text=predmet3_text, url=web_istoruk)
                predmet4 = types.InlineKeyboardButton(text=predmet4_text, url=web_math)
                sms.add(predmet1)
                sms.add(predmet2)
                sms.add(predmet3)
                sms.add(predmet4)
        elif today == 'Thursday':
                day_name = "Пн" + f" | {yaka_nedilya}"
                day_name_b = types.InlineKeyboardButton(text=f"{day_name} | {yaka_nedilya}", callback_data = ' ')
                sms.add(day_name_b)
                if yaka_nedilya == "Жовта":
                    predmet1_text = "⚽️ Фізра 🏀"
                    predmet2_text = "📱 Інформатика 💻"  
                    predmet3_text = "🧲 Фізика 🔌"
                    predmet4_text = "🇺🇦 Укр.літ 🇺🇦"
                else:
                    predmet1_text = "📐 Математика 📏"
                    predmet2_text = "📱 Інформатика 💻"
                    predmet3_text = "🏴󠁧󠁢󠁥󠁮󠁧󠁿 інгліш 🏴󠁧󠁢󠁥󠁮󠁧󠁿"
                    predmet4_text = "🇺🇦 Укр.літ 🇺🇦"

                if day_next == True:
                    time1 = time(hour=9, minute=00)
                    now = datetime.now().time()
                    now_datetime = datetime.combine(datetime.now().date(), now)
                    time1_datetime = datetime.combine(datetime.now().date(), time1)
                    time_diff_seconds = (now_datetime - time1_datetime).total_seconds()
                    if time_diff_seconds >= 3600:
                        hours, remainder = divmod(int(time_diff_seconds), 3600)
                        minutes, seconds = divmod(remainder, 60)
                        time_diff_seconds = str(hours) + "h | " + str(minutes) + "min | " + str(seconds) + "sec."
                    elif time_diff_seconds > 60:
                        minutes, seconds = divmod(int(time_diff_seconds), 60)
                        time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                    else:
                        time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                        
                    predmet1_text = str(time_diff_seconds) + " | " + predmet1_text
                else:
                    if now.time() < time(hour=10, minute=20):
                        if now.time() < time(hour=9, minute=00): 
                            time1 = time(hour=9, minute=00)
                            now = datetime.now().time()
                            now_datetime = datetime.combine(datetime.now().date(), now)
                            time1_datetime = datetime.combine(datetime.now().date(), time1)
                            time_diff_seconds = (time1_datetime - now_datetime).total_seconds()
                            if time_diff_seconds >= 3600:
                                hours, remainder = divmod(int(time_diff_seconds), 3600)
                                minutes, seconds = divmod(remainder, 60)
                                time_diff_seconds = str(hours) + "h | " + str(minutes) + "min | " + str(seconds) + "sec."
                            elif time_diff_seconds > 60:
                                minutes, seconds = divmod(int(time_diff_seconds), 60)
                                time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                            else:
                                time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                            predmet1_text = str(time_diff_seconds) + " | " + predmet1_text
                        else:
                            time1 = time(hour=10, minute=20)
                            now = datetime.now().time()
                            now_datetime = datetime.combine(datetime.now().date(), now)
                            time1_datetime = datetime.combine(datetime.now().date(), time1)
                            time_diff_seconds = (time1_datetime - now_datetime).total_seconds()
                            if time_diff_seconds > 60:
                                minutes, seconds = divmod(int(time_diff_seconds), 60)
                                time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                            else:
                                time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                            predmet1_text = "зараз | " + predmet1_text + " | " + str(time_diff_seconds)
                                
                    elif now.time() < time(hour=12, minute=00) :
                        if now.time() < time(hour=10, minute=40):
                            time1 = time(hour=10, minute=40)
                            now = datetime.now().time()
                            now_datetime = datetime.combine(datetime.now().date(), now)
                            time1_datetime = datetime.combine(datetime.now().date(), time1)
                            time_diff_seconds = (time1_datetime - now_datetime).total_seconds()
                            if time_diff_seconds > 60:
                                minutes, seconds = divmod(int(time_diff_seconds), 60)
                                time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                            else:
                                time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                            predmet2_text = str(time_diff_seconds) + " | " + predmet2_text
                        else:
                            time1 = time(hour=12, minute=00)
                            now = datetime.now().time()
                            now_datetime = datetime.combine(datetime.now().date(), now)
                            time1_datetime = datetime.combine(datetime.now().date(), time1)
                            time_diff_seconds = (time1_datetime - now_datetime).total_seconds()
                            if time_diff_seconds > 60:
                                minutes, seconds = divmod(int(time_diff_seconds), 60)
                                time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                            else:
                                time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                            predmet2_text = "зараз | " + predmet2_text + " | " + str(time_diff_seconds)
                                
                    elif now.time() < time(hour=13, minute=50) :
                        if now.time() < time(hour=12, minute=30):
                            time1 = time(hour=12, minute=30)
                            now = datetime.now().time()
                            now_datetime = datetime.combine(datetime.now().date(), now)
                            time1_datetime = datetime.combine(datetime.now().date(), time1)
                            time_diff_seconds = (time1_datetime - now_datetime).total_seconds()
                            if time_diff_seconds > 60:
                                minutes, seconds = divmod(int(time_diff_seconds), 60)
                                time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                            else:
                                time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                            predmet3_text = str(time_diff_seconds) + " | " + predmet3_text
                        else:
                            time1 = time(hour=13, minute=50)
                            now = datetime.now().time()
                            now_datetime = datetime.combine(datetime.now().date(), now)
                            time1_datetime = datetime.combine(datetime.now().date(), time1)
                            time_diff_seconds = (time1_datetime - now_datetime).total_seconds()
                            if time_diff_seconds > 60:
                                minutes, seconds = divmod(int(time_diff_seconds), 60)
                                time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                            else:
                                time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                            predmet3_text = "зараз | " + predmet3_text + " | " + str(time_diff_seconds)

                    elif now.time() < time(hour=15, minute=30) :
                        if now.time() < time(hour=14, minute=10): 
                            time1 = time(hour=14, minute=10)
                            now = datetime.now().time()
                            now_datetime = datetime.combine(datetime.now().date(), now)
                            time1_datetime = datetime.combine(datetime.now().date(), time1)
                            time_diff_seconds = (time1_datetime - now_datetime).total_seconds()
                            if time_diff_seconds > 60:
                                minutes, seconds = divmod(int(time_diff_seconds), 60)
                                time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                            else:
                                time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                            predmet4_text = str(time_diff_seconds) + " | " + predmet4_text
                        else:
                            time1 = time(hour=15, minute=30)
                            now = datetime.now().time()
                            now_datetime = datetime.combine(datetime.now().date(), now)
                            time1_datetime = datetime.combine(datetime.now().date(), time1)
                            time_diff_seconds = (time1_datetime - now_datetime).total_seconds()
                            if time_diff_seconds > 60:
                                minutes, seconds = divmod(int(time_diff_seconds), 60)
                                time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                            else:
                                time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                            predmet4_text = "зараз | " + predmet4_text + " | " + str(time_diff_seconds)

                predmet1 = types.InlineKeyboardButton(text=predmet1_text, url=web_fizra)
                predmet2 = types.InlineKeyboardButton(text=predmet2_text, callback_data = ' ')
                if yaka_nedilya == "Жовта": predmet3 = types.InlineKeyboardButton(text=predmet3_text, url=web_fizuka)
                else: predmet3 = types.InlineKeyboardButton(text=predmet3_text, callback_data = ' ')
                predmet4 = types.InlineKeyboardButton(text=predmet4_text, url=web_ukr_lit)
                sms.add(predmet1)
                sms.add(predmet2)
                sms.add(predmet3)
                sms.add(predmet4)
        elif today == 'Friday':
                day_name = "Пн" + f" | {yaka_nedilya}"
                day_name_b = types.InlineKeyboardButton(text=day_name, callback_data = ' ')
                sms.add(day_name_b)

                predmet1_text = "🧪 Хімія ⚗️" 
                predmet2_text = "📈 Комп.Графіка 📉"
                predmet3_text = "🧍 Людина і світ 🌎"

                if day_next == True:
                    time1 = time(hour=9, minute=00)
                    now = datetime.now().time()
                    now_datetime = datetime.combine(datetime.now().date(), now)
                    time1_datetime = datetime.combine(datetime.now().date(), time1)
                    time_diff_seconds = (now_datetime - time1_datetime).total_seconds()
                    if time_diff_seconds >= 3600:
                        hours, remainder = divmod(int(time_diff_seconds), 3600)
                        minutes, seconds = divmod(remainder, 60)
                        time_diff_seconds = str(hours) + "h | " + str(minutes) + "min | " + str(seconds) + "sec."
                    elif time_diff_seconds > 60:
                        minutes, seconds = divmod(int(time_diff_seconds), 60)
                        time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                    else:
                        time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                        
                    predmet1_text = str(time_diff_seconds) + " | " + predmet1_text
                else:
                    if now.time() < time(hour=10, minute=20):
                        if now.time() < time(hour=9, minute=00): 
                            time1 = time(hour=9, minute=00)
                            now = datetime.now().time()
                            now_datetime = datetime.combine(datetime.now().date(), now)
                            time1_datetime = datetime.combine(datetime.now().date(), time1)
                            time_diff_seconds = (time1_datetime - now_datetime).total_seconds()
                            if time_diff_seconds >= 3600:
                                hours, remainder = divmod(int(time_diff_seconds), 3600)
                                minutes, seconds = divmod(remainder, 60)
                                time_diff_seconds = str(hours) + "h | " + str(minutes) + "min | " + str(seconds) + "sec."
                            elif time_diff_seconds > 60:
                                minutes, seconds = divmod(int(time_diff_seconds), 60)
                                time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                            else:
                                time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                            predmet1_text = str(time_diff_seconds) + " | " + predmet1_text
                        else:
                            time1 = time(hour=10, minute=20)
                            now = datetime.now().time()
                            now_datetime = datetime.combine(datetime.now().date(), now)
                            time1_datetime = datetime.combine(datetime.now().date(), time1)
                            time_diff_seconds = (time1_datetime - now_datetime).total_seconds()
                            if time_diff_seconds > 60:
                                minutes, seconds = divmod(int(time_diff_seconds), 60)
                                time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                            else:
                                time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                            predmet1_text = "зараз | " + predmet1_text + " | " + str(time_diff_seconds)
                                
                    elif now.time() < time(hour=12, minute=00) :
                        if now.time() < time(hour=10, minute=40):
                            time1 = time(hour=10, minute=40)
                            now = datetime.now().time()
                            now_datetime = datetime.combine(datetime.now().date(), now)
                            time1_datetime = datetime.combine(datetime.now().date(), time1)
                            time_diff_seconds = (time1_datetime - now_datetime).total_seconds()
                            if time_diff_seconds > 60:
                                minutes, seconds = divmod(int(time_diff_seconds), 60)
                                time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                            else:
                                time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                            predmet2_text = str(time_diff_seconds) + " | " + predmet2_text
                        else:
                            time1 = time(hour=12, minute=00)
                            now = datetime.now().time()
                            now_datetime = datetime.combine(datetime.now().date(), now)
                            time1_datetime = datetime.combine(datetime.now().date(), time1)
                            time_diff_seconds = (time1_datetime - now_datetime).total_seconds()
                            if time_diff_seconds > 60:
                                minutes, seconds = divmod(int(time_diff_seconds), 60)
                                time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                            else:
                                time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                            predmet2_text = "зараз | " + predmet2_text + " | " + str(time_diff_seconds)
                                
                    elif now.time() < time(hour=13, minute=50) :
                        if now.time() < time(hour=12, minute=30):
                            time1 = time(hour=12, minute=30)
                            now = datetime.now().time()
                            now_datetime = datetime.combine(datetime.now().date(), now)
                            time1_datetime = datetime.combine(datetime.now().date(), time1)
                            time_diff_seconds = (time1_datetime - now_datetime).total_seconds()
                            if time_diff_seconds > 60:
                                minutes, seconds = divmod(int(time_diff_seconds), 60)
                                time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                            else:
                                time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                            predmet3_text = str(time_diff_seconds) + " | " + predmet3_text
                        else:
                            time1 = time(hour=13, minute=50)
                            now = datetime.now().time()
                            now_datetime = datetime.combine(datetime.now().date(), now)
                            time1_datetime = datetime.combine(datetime.now().date(), time1)
                            time_diff_seconds = (time1_datetime - now_datetime).total_seconds()
                            if time_diff_seconds > 60:
                                minutes, seconds = divmod(int(time_diff_seconds), 60)
                                time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                            else:
                                time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                            predmet3_text = "зараз | " + predmet3_text + " | " + str(time_diff_seconds)

                friday1 = types.InlineKeyboardButton(text=predmet1_text, url=web_ximia)
                friday2 = types.InlineKeyboardButton(text=predmet2_text, callback_data = ' ')
                friday3 = types.InlineKeyboardButton(text=predmet3_text, url=web_lyduna_i_svit)
                sms.add(friday1)
                sms.add(friday2)
                sms.add(friday3)
                sms.add(pustota)
        else:
                day_name = "Пн" + f" | {yaka_nedilya}"
                day_name_b = types.InlineKeyboardButton(text=day_name, callback_data = ' ')
                sms.add(day_name_b)

                predmet1_text = "🦍 Біологія 🚶‍♂️"
                predmet2_text = "🏴󠁧󠁢󠁥󠁮󠁧󠁿 інгліш 🏴󠁧󠁢󠁥󠁮󠁧󠁿"
                predmet3_text = "🇺🇦 Істор.Укp 🇺🇦"
                predmet4_text = "📢 Майдан 📢"

                if day_next == True:
                    time1 = time(hour=9, minute=00)
                    now = datetime.now().time()
                    now_datetime = datetime.combine(datetime.now().date(), now)
                    time1_datetime = datetime.combine(datetime.now().date(), time1)
                    time_diff_seconds = (now_datetime - time1_datetime).total_seconds()
                    if time_diff_seconds >= 3600:
                        hours, remainder = divmod(int(time_diff_seconds), 3600)
                        minutes, seconds = divmod(remainder, 60)
                        time_diff_seconds = str(hours) + "h | " + str(minutes) + "min | " + str(seconds) + "sec."
                    elif time_diff_seconds > 60:
                        minutes, seconds = divmod(int(time_diff_seconds), 60)
                        time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                    else:
                        time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                        
                    predmet1_text = str(time_diff_seconds) + " | " + predmet1_text
                else:
                    if now.time() < time(hour=10, minute=20):
                        if now.time() < time(hour=9, minute=00): 
                            time1 = time(hour=9, minute=00)
                            now = datetime.now().time()
                            now_datetime = datetime.combine(datetime.now().date(), now)
                            time1_datetime = datetime.combine(datetime.now().date(), time1)
                            time_diff_seconds = (time1_datetime - now_datetime).total_seconds()
                            if time_diff_seconds >= 3600:
                                hours, remainder = divmod(int(time_diff_seconds), 3600)
                                minutes, seconds = divmod(remainder, 60)
                                time_diff_seconds = str(hours) + "h | " + str(minutes) + "min | " + str(seconds) + "sec."
                            elif time_diff_seconds > 60:
                                minutes, seconds = divmod(int(time_diff_seconds), 60)
                                time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                            else:
                                time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                            predmet1_text = str(time_diff_seconds) + " | " + predmet1_text
                        else:
                            time1 = time(hour=10, minute=20)
                            now = datetime.now().time()
                            now_datetime = datetime.combine(datetime.now().date(), now)
                            time1_datetime = datetime.combine(datetime.now().date(), time1)
                            time_diff_seconds = (time1_datetime - now_datetime).total_seconds()
                            if time_diff_seconds > 60:
                                minutes, seconds = divmod(int(time_diff_seconds), 60)
                                time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                            else:
                                time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                            predmet1_text = "зараз | " + predmet1_text + " | " + str(time_diff_seconds)
                                
                    elif now.time() < time(hour=12, minute=00) :
                        if now.time() < time(hour=10, minute=40):
                            time1 = time(hour=10, minute=40)
                            now = datetime.now().time()
                            now_datetime = datetime.combine(datetime.now().date(), now)
                            time1_datetime = datetime.combine(datetime.now().date(), time1)
                            time_diff_seconds = (time1_datetime - now_datetime).total_seconds()
                            if time_diff_seconds > 60:
                                minutes, seconds = divmod(int(time_diff_seconds), 60)
                                time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                            else:
                                time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                            predmet2_text = str(time_diff_seconds) + " | " + predmet2_text
                        else:
                            time1 = time(hour=12, minute=00)
                            now = datetime.now().time()
                            now_datetime = datetime.combine(datetime.now().date(), now)
                            time1_datetime = datetime.combine(datetime.now().date(), time1)
                            time_diff_seconds = (time1_datetime - now_datetime).total_seconds()
                            if time_diff_seconds > 60:
                                minutes, seconds = divmod(int(time_diff_seconds), 60)
                                time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                            else:
                                time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                            predmet2_text = "зараз | " + predmet2_text + " | " + str(time_diff_seconds)
                                
                    elif now.time() < time(hour=13, minute=50) :
                        if now.time() < time(hour=12, minute=30):
                            time1 = time(hour=12, minute=30)
                            now = datetime.now().time()
                            now_datetime = datetime.combine(datetime.now().date(), now)
                            time1_datetime = datetime.combine(datetime.now().date(), time1)
                            time_diff_seconds = (time1_datetime - now_datetime).total_seconds()
                            if time_diff_seconds > 60:
                                minutes, seconds = divmod(int(time_diff_seconds), 60)
                                time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                            else:
                                time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                            predmet3_text = str(time_diff_seconds) + " | " + predmet3_text
                        else:
                            time1 = time(hour=13, minute=50)
                            now = datetime.now().time()
                            now_datetime = datetime.combine(datetime.now().date(), now)
                            time1_datetime = datetime.combine(datetime.now().date(), time1)
                            time_diff_seconds = (time1_datetime - now_datetime).total_seconds()
                            if time_diff_seconds > 60:
                                minutes, seconds = divmod(int(time_diff_seconds), 60)
                                time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                            else:
                                time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                            predmet3_text = "зараз | " + predmet3_text + " | " + str(time_diff_seconds)

                    elif now.time() < time(hour=15, minute=30) :
                        if now.time() < time(hour=14, minute=10): 
                            time1 = time(hour=14, minute=10)
                            now = datetime.now().time()
                            now_datetime = datetime.combine(datetime.now().date(), now)
                            time1_datetime = datetime.combine(datetime.now().date(), time1)
                            time_diff_seconds = (time1_datetime - now_datetime).total_seconds()
                            if time_diff_seconds > 60:
                                minutes, seconds = divmod(int(time_diff_seconds), 60)
                                time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                            else:
                                time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                            predmet4_text = str(time_diff_seconds) + " | " + predmet4_text
                        else:
                            time1 = time(hour=15, minute=30)
                            now = datetime.now().time()
                            now_datetime = datetime.combine(datetime.now().date(), now)
                            time1_datetime = datetime.combine(datetime.now().date(), time1)
                            time_diff_seconds = (time1_datetime - now_datetime).total_seconds()
                            if time_diff_seconds > 60:
                                minutes, seconds = divmod(int(time_diff_seconds), 60)
                                time_diff_seconds = str(minutes) + "min | " + str(seconds) + "sec."
                            else:
                                time_diff_seconds = str(int(time_diff_seconds)) + "sec."
                            predmet4_text = "зараз | " + predmet4_text + " | " + str(time_diff_seconds)

                predmet1 = types.InlineKeyboardButton(text=predmet1_text, url=web_biologia)
                predmet2 = types.InlineKeyboardButton(text=predmet2_text, callback_data = ' ')
                predmet3 = types.InlineKeyboardButton(text=predmet3_text, url=web_istoruk)
                predmet4 = types.InlineKeyboardButton(text=predmet4_text, url=web_math)
                sms.add(predmet1)
                sms.add(predmet2)
                sms.add(predmet3)
                sms.add(predmet4)
        sms.add(pustota)
        sms.add(pustota)
        sms.add(pustota)
        sms.add(pustota)
        sms.add(pustota)
        sms.add(pustota)
        sms.add(button_1, button_2, button_3)
        stroka_sostoyaniya = "⌚️ " +  current_time + "                   📳  📶  ✉️  89% 🔋" #🔋🪫 🔌
    
        text=stroka_sostoyaniya
        reply_markup=sms
        return text, reply_markup