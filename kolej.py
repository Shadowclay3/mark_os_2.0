import os, telebot, datetime, random, time
os.system('cls' if os.name == 'nt' else 'clear')

for i in range(30):
    loading = ""
    for i in range(20):
        random_number = random.randint(1, 20)
        for i in range(random_number):
            loading += "|"
        loading += "\n"
    print(loading)
    time.sleep(0.1)
    os.system('cls' if os.name == 'nt' else 'clear')
print("Started!")

bot = telebot.TeleBot("5848488708:AAFH_SuJ2R60qLr6bSfm8oHYXX6k_Ipc4sY")
admin_bot = telebot.TeleBot('6109509623:AAHGObSchIH6i42bL1Hz4Md62EJfkw0MZEU')
admin_bot.send_message(1004574223, "kolej.py | started")

@bot.message_handler(commands=['exit'])
def stop(message):
    if message.chat.id == 1004574223:
        os.system('cls' if os.name == 'nt' else 'clear')
        bot.send_message(message.chat.id, "bot: | stoped")
        while True:
            os._exit(0)
    else: bot.send_message(message.from_user.id, "Тебе нема в адмінах")

@bot.message_handler(commands=['start'])
def start (message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton(text="Спеціальності", callback_data="Спеціальності"))
    keyboard.add(telebot.types.InlineKeyboardButton(text="Перелік документів", callback_data="Перелік документів"))
    keyboard.add(telebot.types.InlineKeyboardButton(text="Терміни вступної", callback_data="Терміни вступної"))
    keyboard.add(telebot.types.InlineKeyboardButton(text="Особливості прийому", callback_data="Особливості прийому"))
    keyboard.add(telebot.types.InlineKeyboardButton(text="Підготовчі курси", callback_data="Підготовчі курси"))
    keyboard.add(telebot.types.InlineKeyboardButton(text="Державне замовленя (бюджет)", callback_data="Державне замовлення (бюджет)"))
    keyboard.add(telebot.types.InlineKeyboardButton(text="Вартість навчання", callback_data="Вартість навчання"))
    keyboard.add(telebot.types.InlineKeyboardButton(text="Програми вступних іспитів", callback_data="Програми вступних іспитів"))
    keyboard.add(telebot.types.InlineKeyboardButton(text="Мотивацiйний лист", callback_data="Мотивацiйний_лист"))
    keyboard.add(telebot.types.InlineKeyboardButton(text="Контакти", callback_data="Контакти"))
    bot.send_message(message.from_user.id, text="Що ви хочете дізнатися ?", reply_markup=keyboard)
    current_time = datetime.datetime.now().time()
    formatted_time = current_time.strftime("%Hh %Mmin %Ssec")
    if message.from_user.first_name != None: name = f"| {message.from_user.first_name}\n"
    else: name = ""
    if message.from_user.last_name != None: last_name = f"| {message.from_user.last_name}\n"
    else: last_name = ""
    if message.from_user.username != None: username = f"| @{message.from_user.username}\n"
    else: username = ""
    vuvod = f"|--------------------\n| {message.from_user.id}\n{name}{last_name}{username}|--------------------\n| {message.text}\n|--------------------\n| {formatted_time}\n|--------------------\n"
    print(vuvod)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == " ":
        pass
    if call.data == "Спеціальності_Назад":
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton(text="Спеціальності", callback_data="Спеціальності"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Перелік документів", callback_data="Перелік документів"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Терміни вступної", callback_data="Терміни вступної"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Особливості прийому", callback_data="Особливості прийому"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Підготовчі курси", callback_data="Підготовчі курси"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Державне замовленя (бюджет)", callback_data="Державне замовлення (бюджет)"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Вартість навчання", callback_data="Вартість навчання"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Програми вступних іспитів", callback_data="Програми вступних іспитів"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Мотивацiйний лист", callback_data="Мотивацiйний_лист"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Контакти", callback_data="Контакти"))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Що ви хочете дізнатися ?", reply_markup=keyboard)
    if call.data == "Спеціальності" or call.data == "Назад_Авіаційна" or call.data == "Назад_Металургія" or call.data == "Назад_Техно" or call.data == "Назад_Комп" or call.data == "Назад_Галузеве":
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton(text="Авіаційна ракетно-космічна технікa", callback_data="Авіаційна ракетно-космічна технікa"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Металургія", callback_data="Металургія"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Галузеве машинобудування", callback_data="Галузеве машинобудування"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Прикладна механіка", callback_data="Прикладна механіка"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Комп'ютерні науки", callback_data="Комп'ютерні науки"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Комп'ютерна інженерія", callback_data="Комп'ютерна інженерія"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Економіка", callback_data="Економіка"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data="Спеціальності_Назад"))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Наші спеціальності", reply_markup=keyboard)
    if call.data == "Авіаційна ракетно-космічна технікa":
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton(text="Виробництво авіаційних двигунів", callback_data="Виробництво авіаційних двигунів"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Виробництво літальних апаратів", callback_data="Виробництво літальних апаратів"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data="Спеціальності"))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Випускники цієї спеціальності - інженери ! Це люди, які здатні проектувати і діагностувати будь-які технічні системи будь-якої складності. Авіаційні агрегати - дуже складні і відповідальні системи, що працюють в умовах великих перепадів температур, перевантажень і вібрацій. До їх надійності пред'являються підвищенні вимоги. Тому метою навчання є формування навичок і умінь розрахунку комп'ютерного проєктування паливних, масляних, повітряних і протиобмерзних систем, систем автоматичного управління, виконавчих механізмів систем автоматичного управління і регулювання авіаційних двигунів.\n\nВипускникам цієї спеціальності пропонується широкий вибір при визначенні місця своєї подальшої роботи і розвитку. Це можуть бути як підприємства авіаційної промисловості, так і освітні та науково-дослідні інститути, такі як Національний аерокосмічний університет «Харківський авіаційний інститут», Київський національний авіаційний університет, Інститут проблем машинобудування Національної академії наук України та інші.", reply_markup=keyboard)
    if call.data == "Галузеве машинобудування":
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton(text="Технологія обробки матеріалів на верстатах та автоматичних лініях", callback_data="Технологія"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Комп’ютерні технології в машинобудуванні", callback_data="Комп’ютерні"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data="Спеціальності"))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Існує міф, що машинобудування це спеціальність, на якій навчають будувати машини, але насправді це можливість одержати найкращу технічну освіти й стати справжнім майстром інженерних вершин.\n\nГалузеве машинобудування це спеціальність широкого профілю, яка дозволить навчитись знатися на складових частинах великих промислових виробництв, зрозуміти інноваційні технології виготовлення деталей для літаків і ракетно-космічної техніки, формувати засоби автоматизації сучасних підприємств. \n\nВи будете знати, як впроваджуються новітні комп'ютерні технології на виробництві, вільно оперувати всіма потрібними програмами й розробляти надсучасні підходи до оптимізації української промисловості, Ми готуємо фахівців високого рівня для успішного кар'єрного зростання на підприємствах, де здобуті знання та навички високо цінуються роботодавцями.\n\nТерміни навчання  3 роки 10 місяців\n\nКваліфікація випускника технік-технолог (механіка)\n\nПерспективи навчання та робота\nНавчання можна продовжити у таких закладах як Національний аерокосмічний університет ім. Жуковського “ХАІ”, Національному університеті Запорізька політехніка, а також у закладах вищої освіти відповідно до спеціальності.Навчання відбувається по скороченій програмі та на споріднених спеціальностях.\nНашi випускники можуть обiймати такi посади :\n-технiк - технолог;\n-контролер механоскладальних робiт;\n-майстер виробничої дiльницi;\n-оператор верстатiв з ЧПК.", reply_markup=keyboard)
    if call.data == "Технологія":
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton(text="▶️  Технологія обробки матеріалів на верстатах та автоматичних лініях", callback_data=" "))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Комп’ютерні технології в машинобудуванні", callback_data="Комп’ютерні"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data="Спеціальності"))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Ви отримаєте навички розробки технологiчних процесiв деталей для лiтакiв i ракетно-космiчної технiки виготовлення, будете знати ,як впроваджуються новiтнi комп'ютернi технологiї на виробництвi,вiльно оперувати всiма потрiбнмим програмами i розробляти надсучаснi пiдходи до оптимiзацiї української промисловостi. Ми готуємо фахiвцiв високого рiвня для успiшного кар”єрного зростання на пiдприємствах ,де здобутi знання та навички високо цiнуються роботодавцями.\n\nОсновні спец. дисципліни: основи обробки матерiалiв та рiжучий iнструмент, тех.оснащення, металорiзальнi верстати, технологiчнi основи для програмування верстатiв з ЧПК, лабораторний практикум, технологiя машинобудування, системи автоматизованого проектування технологiчних процесiв.", reply_markup=keyboard)
    if call.data == "Комп’ютерні":
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton(text="Технологія обробки матеріалів на верстатах та автоматичних лініях", callback_data="Технологія"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="▶️  Комп’ютерні технології в машинобудуванні", callback_data=" "))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data="Спеціальності"))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="На данiй спеціальності готують фахівцiв ,що володiють знаннями сучасних комп’ютерних технологій в  галузевому машинобудуваннi.Ви будете володiти такими комп’ютерними  програмами: \nAutoCad,AutoCad3D,Unigraphics.Ця спецiальнiсть дозволить навчитись знатися на iнновацiйних технологiях виготовлення деталей для лiтакiв i ракетно-космiчної технiки ,формувати засоби автоматизацiї сучасних пiдприємств.Ми готуємо конкурентно спроможних фахiвцiв високого рiвня для успiшного кар”єрного зростання на пiдприємствах ,де здобутi знання та навички високо цiнуються роботодавцями.\n\nОсновні спец. дисципліни: основи обробки матерiалiв та рiжучий iнструмент, тех.оснащення, металорiзальнi верстати, технологiчнi основи для програмування верстатiв з ЧПК, технологiя машинобудування, системи автоматизованого проектування технологiчних процесiв, сучаснi технологiї виробництва, комп”ютерне забезпечення пiдготовки виробництва.", reply_markup=keyboard)
    if call.data == "Виробництво авіаційних двигунів":
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton(text="▶️  Виробництво авіаційних двигунів", callback_data=" "))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Виробництво літальних апаратів", callback_data="Виробництво літальних апаратів"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data="Спеціальності"))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="\nОПП Виробництво авіаційних двигунів\n\nТекст (суть спеціальності)\nВипускники цієї спеціальності - інженери найвищого класу! Це люди, які будуть здатні проєктувати та діагностувати авіаційні технічні системи будь-якої складності. Метою навчання є формування навичок і умінь розрахунку та комп'ютерного проєктування паливних, масляних, повітряних і проти обмерзлих систем, систем автоматичного управління і регулювання авіаційних двигунів.\n\nГалузь знань 13 Механічна інженерія\n\nТерміни навчання 3 роки 10 місяців\n\nКваліфікація випускника технік-технолог (механіка)\n\nОсновні спец. дисципліни \n\nТеоретична механіка,Теоретична механіка Термодинаміка і теплообмін Авіаційне матеріалознавство Термодинаміка і теплообмін Гідрогазодинаміка Теоретична  механіка Деталі машин та основи конструювання Теорія  машин і механізмів Теорія авіаційних двигунів  Конструкція авіаційних двигунів Технологія двигунобудування  Електротехніка з основами електроніки  Взаємозамінність, Стандартизація та технічні вимірювання  Технологія конструкційних матеріалів Випробування авіаційних двигунів Експлуатація та обслуговування авіаційних двигунів Технологічне обладнання і оснащення\nКомплексно-графічні системи проєктування та 3D моделювання Основи конструювання літальних апаратів Надійність авіаційної техніки  Цивільний захист та охорона праці в галузі\n\n\nПерспективи навчання та робота \n\nНаші випускники можуть продовжити навчання у вищих навчальних закладах України технічного напряму, а також працювати в організаціях, які займаються проектуванням та переоснащенням повітряних суден, а також їх експлуатацією.", reply_markup=keyboard)
    if call.data == "Виробництво літальних апаратів":
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton(text="Виробництво авіаційних двигунів", callback_data="Виробництво авіаційних двигунів"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="▶️  Виробництво літальних апаратів", callback_data=" "))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data="Спеціальності"))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Підготовка фахівців в галузі механічної інженерії з широким доступом до працевлаштування та зацікавленості до певних галузей механічної інженерії для подальшого навчання.\n\nОкрім високої якості теоретичної підготовки, здобувачі освіти мають можливість отримати практичний досвід завдяки співпраці з провідними авіаційними підприємствами та організаціями. Це дозволяє майбутнім фахівцям отримати необхідні навички та компетенції, які допоможуть їм стати успішними в авіаційній галузі.\nГалузь знань 13 Механічна інженерія\nТерміни навчання 3 роки 10 місяців\nКваліфікація випускника технік-технолог (механіка)\nОсновні спец. дисципліни гідравліка, гідрогазодинаміка, термодинаміка і теплообмін, конструкція та міцність літальних апаратів, функціональні системи повітряних суден, автоматизація процесів конструювання та складання ЛА, експлуатація повітряних суден, основи надійності авіаційної техніки, комп’ютерні технології моделювання, теорія і конструкція авіаційних двигунів, основи технології виробництва авіаційної техніки\nПерспективи навчання та робота\nНаші випускники можуть працювати в організаціях, які займаються проектуванням та переоснащенням повітряних суден, а також їх експлуатацією.", reply_markup=keyboard)
    if call.data == "Металургія":
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton(text="Сeкрeти вигoтoвлeння і oбрoбки мeтaлiв", callback_data="Сeкрeти вигoтoвлeння і oбрoбки мeтaлiв"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Металургія", callback_data="Металургія_текст"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Галузь знань", callback_data="Галузь знань"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Хочю дізнатися більше:", callback_data="Хочю дізнатися більше:"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data="Спеціальності"))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Металургія", reply_markup=keyboard)
    if call.data == "Сeкрeти вигoтoвлeння і oбрoбки мeтaлiв":
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton(text="▶️  Сeкрeти вигoтoвлeння і oбрoбки мeтaлiв", callback_data=" "))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Металургія", callback_data="Металургія_текст"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Галузь знань", callback_data="Галузь знань"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Хочю дізнатися більше:", callback_data="Хочю дізнатися більше:"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data="Спеціальності"))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Це одна з найстародавніших процесій, яку опанувало людство. Зараз метал Використовується для виготовлення різноманітних товарів, приладів та устаткування. Продукцією ливарного виробництва є литі деталі різноманітної конфігурації та розмірів для авіаційних двигунів, складні деталі для всіх галузей машинобудування та навіть ювелірні прикраси та вироби для стоматології.", reply_markup=keyboard)
    if call.data == "Металургія_текст":
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton(text="Сeкрeти вигoтoвлeння і oбрoбки мeтaлiв", callback_data="Сeкрeти вигoтoвлeння і oбрoбки мeтaлiв"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="▶️  Металургія", callback_data=" "))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Галузь знань", callback_data="Галузь знань"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Хочю дізнатися більше:", callback_data="Хочю дізнатися більше:"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data="Спеціальності"))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Це складна галузь промисловості, до якої належать ріні за організацією і технологією виробництва: виробництво чорних та кольорових металів та сплавів, отримання і використання композиційних матеріалів, адитивні технології у вигляді 3D- моделювання та 3D-друку.", reply_markup=keyboard)
    if call.data == "Галузь знань":
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton(text="Сeкрeти вигoтoвлeння і oбрoбки мeтaлiв", callback_data="Сeкрeти вигoтoвлeння і oбрoбки мeтaлiв"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Металургія", callback_data="Металургія_текст"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="▶️  Галузь знань", callback_data=" "))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Хочю дізнатися більше:", callback_data="Хочю дізнатися більше:"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data="Спеціальності"))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="13 Механічна інженерія\n\nТерміни навчання: 3 роки 10 місяців\n\nКваліфікація випускника: технік-технолог (лиття металів)\n\nМеталургія перейшла на новий рівень. Тепер це сучасні виробництва з великою кількістю новітньої техніки та з зовсім іншими методами навчання. \nНа спеціальності Металургія ти отримаєш багаж знань з тих предметів, які і є залогом твого майбутнього\nВважаєш хімію, фізику та креслення неосяжними предметами, а ти не думав, що на рівні Металургії вони можуть бути ще й цікавими?\nУяви собі Металургію в світі комп’ютерних технологій - комп’ютерне проектування та програмування, 3-D моделювання, 3-D принтери, нові композиційні матеріали та адитивні технології.\nДолучайся до команди професіоналів і забезпечуй своє майбутнє!", reply_markup=keyboard)
    if call.data == "Хочю дізнатися більше:": 
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton(text="Сeкрeти вигoтoвлeння і oбрoбки мeтaлiв", callback_data="Сeкрeти вигoтoвлeння і oбрoбки мeтaлiв"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Металургія", callback_data="Металургія_текст"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Галузь знань", callback_data="Галузь знань"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="▶️  Хочю дізнатися більше:", callback_data=" "))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data="Спеціальності"))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Основні спец. дисципліни\n\nФізична хімія, аналітична хімія, Механізація та автоматизація ливарного виробництва, Печі та сушила ливарного виробництва, Обладнання ливарних цехів, Металургія та технологія  ливарних сплавів, Основи теорії плавки та виробництва\nвиливків з чорних та кольорових сплавів, Технологія виготовлення  ливарної форми, Матеріалознавство та технологія конструкційних матеріалів, Художнє та ювелірне литво, Прогресивні методи виробництва виливків, Системи автоматизації проектування процесів та систем\n\nПерспективи навчання та робота\nВипускники Запорізького авіаційного фахового коледжу після закінчення можуть продовжувати навчання в провідних закладах Вищої освіти за спеціалізацією, а також працювати на провідних металургійних і машинобудівних підприємствах міста Запоріжжя і України в цілому.", reply_markup=keyboard)
    if call.data == "Прикладна механіка":
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data="Спеціальності"))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="На спеціальності готують фахівця з обслуговування верстатів з числовим програмним управлінням і робототехнічних комплексів здатний виконувати роботи в бюро відділів головного механіка, головного енергетика, а також у проектних і науково-дослідних організаціях машинобудівного профілю.\n\nГалузь знань 13 Механічна інженерія.\n\nТерміни навчання 3 роки 10 місяців\n\nКваліфікація випускника Технік-електромеханік\n\nОсновні спец. дисципліни Будова та обслуговування верстатів з ПУ та РТК, Приводи верстатів з ПУ та РТК, Електропривод та електрообладнання верстатів з ПУ і РТК, Основи дискретної автоматики, Системи ЧПК, Інтелектуальні системи автоматики, Схемотехніка на мікроконтролерах, Електрорадіовимірювання, Системи автоматизованого проектування, Електрорадіоматеріали, Промислова електроніка, Теоретичні основи електротехніки\n\nПерспективи навчання та робота\nтехнік електромеханік може виконувані такі професійні роботи і займані первинні посади: слюсар КВПіА; налагоджувальник КВПіА; робота у бюро відділу головного механіка, головного енергетика, науково та проектно-дослідницьких підприємствах машинобудівного профілю; виконує роботи з ремонту, налагодження обладнання, профілактичні заходи з підтримання обладнання  в робочому стані; бере участь в розробці і оформленні різної технічної документації для монтажу і експлуатації обладнання з забезпеченням норм охорони праці; виконує розрахунки з визначення потреби в запасних частинах, електрорадіо елементах, інтегральних мікросхемах; бере участь у розробці електричних і електронних схем.\nВипускники можуть обіймати первинні посади за Національним класифікатором України «Класифікатор професій» ДК 003:2010:\n3113 Електромеханік\n3113 Електромеханік дільниці \n3115 Технік з автоматизації виробничих процесів\n3115 Технік з експлуатації та ремонту устаткування\n3139 Технік-оператор електронного устаткування\n7223 Налагоджувальник автоматичних ліній і агрегатних верстатів.\n7223 Налагоджувальник верстатів і маніпуляторів з програмним керуванням.\n7241 Електромеханік з випробувань та ремонту електроустаткування.\n7241 Електромеханік з ремонту та обслуговування устаткування інформаційних систем.\n7241 Електромеханік засобів автоматики та приладів.\n7241 Електромеханік з ремонту та обслуговування лічильно-обчислювальних машин .\n7241 Електромонтажник електричних машин \n8172 Оператор промислових роботів.\n8211 Оператор верстатів з програмним керуванням \n\nНавчання можна продовжити у таких вишах як Національний аерокосмічний університет ім. Жуковського “ХАІ”, Національному університеті Запорізька політехніка. Навчання відбувається по скороченій програмі та на споріднених спеціальностях.", reply_markup=keyboard)
    if call.data == "Комп'ютерні науки":
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data="Спеціальності"))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Якщо ви дружите з математикою, любите технічні предмети і маєте гарне логічне і творче  мислення, то, можливо, вам варто розглянути для себе спеціальність Комп’ютерні науки.\nСпеціальність 122 «Комп’ютерні науки» – спрямована на підготовку фахівців, які:\nмають ґрунтовну математичну підготовку і знання в області програмування, володіють алгоритмічним мисленням; \nзнають сучасні методи побудови і аналізу ефективних алгоритмів і здатність їх реалізовувати в конкретних додатках. \nволодіють стандарти, методи і засоби управління процесами життєвого циклу інформаційних систем, продуктів і сервісів IT;\nмають знання теоретичних основ, процесів і процедур управління IT-проектами, принципів командної роботи.\n\nГалузь знань  12 Інформаційні технології\n\nТерміни навчання 3 роки та 10 місяців\n\nКваліфікація випускника Технік програміст\n\nОсновні спец. дисципліни:  Алгоритмізація та програмування, Об'єктно-орієнтоване програмування, Організація баз даних та знань, Теорія ймовірностей і  математична статистика, Web-технології і  web-дизайн, Комп'ютерна графіка, Технології створення програмних продуктів, Економіка та основи ІТ-бізнесу, Системне програмування та операційні системи\n\nПерспективи навчання та робота\nВипускники коледжу можуть продовжити навчання у будь якому закладі вищої освіти відповідно до спеціальності.\nФахівці можуть працювати на сучасних підприємствах будь-якої організаційно-правової форми( державні, муніципальні, комерційні та некомерційні) та за будь-якими видами економічної діяльності та обіймати такі посади:\n-Технічний фахівець в галузі обчислювальної техніки\n-Технік-програміст\n-Технік з системного адміністрування\n-Фахівець з інформаційних технологій\n-Фахівець з розробки та тестування програмного забезпечення\n-Фахівець з розроблення комп’ютерних програм", reply_markup=keyboard)
    if call.data == "Комп'ютерна інженерія":
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data="Спеціальності"))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="«Комп’ютерна інженерія» — спеціальність для тих, хто більше любить «програмувати залізо»!\nКомп’ютерна інженерія – не просто сучасна професія, але й найактуальніший тренд, який згодом не тільки не втратить своєї популярності, а й отримає подальший розвиток у професіях майбутнього.  \nЦя спеціальність пов’язана з апаратним забезпеченням комп’ютерної техніки і водночас підтримується потужною підготовкою з програмування. Здобувачі освіти отримають професійні знання з розробки, експлуатаційного обслуговування, ремонту та модернізації системних програмних і технічних засобів ІТ, їх локально-мережевих реалізаціях в офісах, установах, організаціях та на підприємствах. Наші студенти вивчають мови програмування, архітектуру комп’ютера, операційні системи та комп’ютерні мережі, бази даних та інформаційно-пошукові системи, штучний інтелект та робототехніку набувають професійних навичок, що допоможуть реалізувати себе в найрізноманітніших сферах діяльності в Україні та за кордоном.\nСпеціальність тісно пов’язана з програмуванням, але має нахил до створення апаратного забезпечення. Якщо програмісти створюють «розум» машини, то комп’ютерні інженери створюють фізичну основу, яка зробить його роботу можливою.  Якщо ви любите ритись у «залізі», платах та процесорах або фанатієте від робототехніки, ця спеціальність точно вам сподобається!\n\nГалузь знань 12 Інформаційні технології\n\nТерміни навчання 3 роки та 10 місяців\n\nКваліфікація випускника Технік з інформаційних технологій\n\nОсновні спец. дисципліни: Комп'ютерна електроніка, Комп'ютерна схемотехніка, Операційні системи, Системне програмування, Архітектура комп'ютерів, Комп'ютерні мережі, Технології захисту інформації та основи кібербезпеки, Надійність, діагностика та експлуатація комп’ютерних мереж та систем, Основи програмної інженерії. \n\nПерспективи навчання та робота:\nВипускники коледжу можуть продовжити навчання у будь якому закладі вищої освіти відповідно до спеціальності.\nФахівці можуть працювати на сучасних підприємствах різних форм власності та обіймати такі посади:\n-фахівець з інформаційних технологій;\n-технічний фахівець в галузі обчислювальної техніки;\n-технік обчислювального (інформаційно-обчислювального) центру;\n-фахівець з розроблення комп'ютерних програм;\n-технік із системного адміністрування.", reply_markup=keyboard)
    if call.data == "Економіка":
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton(text="Економіка підприємства", callback_data="Економіка підприємства"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Бізнес-економіка", callback_data="Бізнес-економіка"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data="Спеціальності"))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="EKOHOMICT - це освіта сучасності, яка має такі унікальні риси як перспективність, універсальність та прибутковість.\n\nЕкономіка в усіх її проявах міцно увійшла в життя людства це наука про Використання обмежених ресурсів, виробництво, розподіл, обмін, продаж та споживання товарів і послуг.\n\nЗдобувачі освіти вивчають функціонування будь-якого підприємства, незалежно від його розміру та організаційно-правової форми господарювання, закономірності функціонування та розвитку соціально- економічних систем і процесів їх моделювання, прогнозування та регулювання, мотивацію і поведінку економічних суб'єктів.\n\nЦя спеціальність надає можливість працевлаштування у будь-якій сфері, де потрібні економічні знання.", reply_markup=keyboard)
    if call.data == "Економіка підприємства":
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton(text="▶️  Економіка підприємства", callback_data=" "))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Бізнес-економіка", callback_data="Бізнес-економіка"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data="Спеціальності"))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Здійснюється  підготовка конкурентоспроможних та висококваліфікованих фахівців, формування професійної компетентності фахівців-економістів, що володіють інноваційними способами мислення, відповідними компетентностями для комплексного аналізу, прогнозування та ефективного управління економічними системами.\nОсвітній процес орієнтується на сучасні наукові дослідження в галузі економіки, враховуючи особливості функціонування підприємств різних форм власності, існуючу стійку тенденцію до віртуалізації функціонування підприємств різних сфер економічної діяльності, передбачає практичне навчання на підприємствах реального та ІКТ-сектора економіки.\n\nГалузь знань  05 Соціальні та поведінкові науки\n\nТерміни навчання  2 роки 10 місяців \n\nКваліфікація випускника Економіст\n\nОсновні спец. дисципліни: Економіка підприємства. Бухгалтерський облік. Фінансовий облік. Економіка і нормування праці. Планування та організація діяльності підприємства. Основи аудиту. Управління витратами. Податкова система. Економічний аналіз.  \n\nПерспективи навчання та робота\nФахівці можуть працювати на сучасних підприємствах різних форм власності та обіймати такі посади:\n-Економіст виробництва\n-Економіст-бухгалтер\n-Економіст-аналітика\n-Фахівець з нормування праці\n-Фахівець з постачання та збуту в сфері виробництва та торгівлі\n-Помічник керівника підприємства (установи, організації)", reply_markup=keyboard)
    if call.data == "Бізнес-економіка":
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton(text="Економіка підприємства", callback_data="Економіка підприємства"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="▶️  Бізнес-економіка", callback_data=" "))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data="Спеціальності"))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Здійснюється  підготовка конкурентоспроможних та кваліфікованих фахівців економіко-управлінського профілю з поглибленим знанням сучасних інформаційних технологій та вмінням комплексного аналітичного мислення, що дозволяє приймати обґрунтовані бізнес-рішення.\nВипускники можуть знайти  застосування своїм знанням практично в будь-якій сфері діяльності, де потрібні дослідження і вирішення широкого спектра питань, пов’язаних з економікою і управління персоналом.\n\nГалузь знань  05 Соціальні та поведінкові науки\n\nТерміни навчання  2 роки 10 місяців \n\nКваліфікація випускника Економіст\n\nОсновні спец. дисципліни: Основи бізнес-економіки. Економіка підприємства. Бухгалтерський облік. Фінансовий облік. Аналіз бізнес-середовища. Інтернет-технології в бізнесі.  Управління витратами. Менеджмент. Економічний аналіз.  Практика з економіко-математичного моделювання. \n\nПерспективи навчання та робота:  Випускники можуть працювати в усіх галузях національної економіки, у державних органах виконавчої влади, органах місцевого самоврядування, у сфері соціальної діяльності, виробництва, бізнесу, туристичної індустрії та ін.", reply_markup=keyboard)
    if call.data == "Перелік документів":
        try:bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        except: pass
        keyboard = telebot.types.InlineKeyboardMarkup() 
        keyboard.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data="photo_Назад"))
        photo_path = f'{call.data}.jpg'   # Укажите путь к фотографии
        with open(photo_path, 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo, reply_markup=keyboard)
    if call.data == "Терміни вступної":
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton(text="Вступ на основі БЗСО (9 класів)", callback_data="Вступ на основі БЗСО (9 класів)"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Вступ на основі ПЗСО (11 класів)", callback_data="Вступ на основі ПЗСО (11 класів)"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Вступ на заочне навчання", callback_data="Вступ на заочне навчання"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data="Спеціальності_Назад"))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Терміни вступної кампанії", reply_markup=keyboard)
    if call.data == "Вступ на основі БЗСО (9 класів)":
        try: bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        except: pass
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton(text="▶️  Вступ на основі БЗСО (9 класів)", callback_data=" "))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Вступ на основі ПЗСО (11 класів)", callback_data="Вступ на основі ПЗСО (11 класів)"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Вступ на заочне навчання", callback_data="Вступ на заочне навчання"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data="photo_Назад"))
        photo_path = f'{call.data}.jpg'  # Укажите путь к фотографии
        with open(photo_path, 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo, reply_markup=keyboard)
    if call.data == "Вступ на основі ПЗСО (11 класів)":
        try: bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        except: pass
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton(text="Вступ на основі БЗСО (9 класів)", callback_data="Вступ на основі БЗСО (9 класів)"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="▶️  Вступ на основі ПЗСО (11 класів)", callback_data=" "))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Вступ на заочне навчання", callback_data="Вступ на заочне навчання"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data="photo_Назад"))
        photo_path = f'{call.data}.jpg'  # Укажите путь к фотографии
        with open(photo_path, 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo, reply_markup=keyboard)
    if call.data == "Вступ на заочне навчання":
        try: bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        except: pass
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton(text="Вступ на основі БЗСО (9 класів)", callback_data="Вступ на основі БЗСО (9 класів)"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Вступ на основі ПЗСО (11 класів)", callback_data="Вступ на основі ПЗСО (11 класів)"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="▶️  Вступ на заочне навчання", callback_data=" "))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data="photo_Назад"))
        photo_path = f'{call.data}.jpg'   # Укажите путь к фотографии
        with open(photo_path, 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo, reply_markup=keyboard)
    if call.data == "photo_Назад":
        try: bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        except: pass
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton(text="Спеціальності", callback_data="Спеціальності"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Перелік документів", callback_data="Перелік документів"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Терміни вступної", callback_data="Терміни вступної"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Особливості прийому", callback_data="Особливості прийому"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Підготовчі курси", callback_data="Підготовчі курси"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Державне замовленя (бюджет)", callback_data="Державне замовлення (бюджет)"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Вартість навчання", callback_data="Вартість навчання"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Програми вступних іспитів", callback_data="Програми вступних іспитів"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Мотивацiйний лист", callback_data="Мотивацiйний_лист"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Контакти", callback_data="Контакти"))
        bot.send_message(call.message.chat.id, text="Що ви хочете дізнатися ?", reply_markup=keyboard)
    if call.data == "Особливості прийому":
        try: bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        except: pass
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data="delete_photos 'Особливості прийому'"))
        with open('Особливості прийому1.jpg', 'rb') as photo1:
            bot.send_photo(call.message.chat.id, photo1)

        # Send the second photo
        with open('Особливості прийому2.jpg', 'rb') as photo2:
            bot.send_photo(call.message.chat.id, photo2)

        # Send the third photo
        with open('Особливості прийому3.jpg', 'rb') as photo3:
            bot.send_photo(call.message.chat.id, photo3)

        # Send the fourth photo
        with open('Особливості прийому4.jpg', 'rb') as photo4:
            bot.send_photo(call.message.chat.id, photo4, reply_markup=keyboard)
    if call.data == "delete_photos 'Особливості прийому'":
        for i in range(4):
            try: bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id - i - 0)
            except: pass
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton(text="Спеціальності", callback_data="Спеціальності"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Перелік документів", callback_data="Перелік документів"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Терміни вступної", callback_data="Терміни вступної"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Особливості прийому", callback_data="Особливості прийому"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Підготовчі курси", callback_data="Підготовчі курси"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Державне замовленя (бюджет)", callback_data="Державне замовлення (бюджет)"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Вартість навчання", callback_data="Вартість навчання"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Програми вступних іспитів", callback_data="Програми вступних іспитів"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Мотивацiйний лист", callback_data="Мотивацiйний_лист"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Контакти", callback_data="Контакти"))
        bot.send_message(call.message.chat.id, text="Що ви хочете дізнатися ?", reply_markup=keyboard)
    if call.data == "Підготовчі курси": 
        try: bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        except: pass
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data="photo_Назад"))
        photo_path = f'{call.data}.jpg'   # Укажите путь к фотографии
        with open(photo_path, 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo, reply_markup=keyboard)
    if call.data == "Державне замовлення (бюджет)": 
        try: bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        except: pass
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data="photo_Назад"))
        photo_path = 'бюджет.jpg'   # Укажите путь к фотографии
        with open(photo_path, 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo, reply_markup=keyboard)
    if call.data == "Вартість навчання":
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data="Спеціальності_Назад"))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Інформацію щодо вартості навчання буде надано пізніше", reply_markup=keyboard)
    if call.data == "Мотивацiйний_лист":
        try: bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        except: pass
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data="delete_documents 'Мотивацiйний_лист'"))
        with open('Вимоги до мотиваційного листа.pdf', 'rb') as document:
            bot.send_document(call.message.chat.id, document)
        with open('Мотиваційний лист бланк.pdf', 'rb') as document:
            bot.send_document(call.message.chat.id, document, reply_markup=keyboard)
    if call.data == "Програми вступних іспитів":
        try:bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        except: pass
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data="delete_documents 'Прoгрaми встyпниx icпитiв'"))
        with open('програма_співбесіда_з_укр_мови_бзсо.pdf', 'rb') as document:
            bot.send_document(call.message.chat.id, document)
        with open('програма_співбесіди_математика_бзсо.pdf', 'rb') as document:
            bot.send_document(call.message.chat.id, document, reply_markup=keyboard)
    if call.data == "delete_documents 'Прoгрaми встyпниx icпитiв'" or call.data == "delete_documents 'Мотивацiйний_лист'":
        for i in range(2):
            try:bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id - i - 0)
            except: pass
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton(text="Спеціальності", callback_data="Спеціальності"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Перелік документів", callback_data="Перелік документів"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Терміни вступної", callback_data="Терміни вступної"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Особливості прийому", callback_data="Особливості прийому"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Підготовчі курси", callback_data="Підготовчі курси"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Державне замовленя (бюджет)", callback_data="Державне замовлення (бюджет)"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Вартість навчання", callback_data="Вартість навчання"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Програми вступних іспитів", callback_data="Програми вступних іспитів"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Мотивацiйний лист", callback_data="Мотивацiйний_лист"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Контакти", callback_data="Контакти"))
        bot.send_message(call.message.chat.id, text="Що ви хочете дізнатися ?", reply_markup=keyboard)
    if call.data == "Контакти":
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton(text="маршрут до коледжу", url="https://goo.gl/maps/4qA4H3d2ANuQnnHP8"))
        keyboard.add(telebot.types.InlineKeyboardButton(text=" ", callback_data=" "))
        keyboard.add(telebot.types.InlineKeyboardButton(text="приймальна комісія:", callback_data=" "))
        keyboard.add(telebot.types.InlineKeyboardButton(text="(095)116-98-77", callback_data=" "))
        keyboard.add(telebot.types.InlineKeyboardButton(text="або", callback_data=" "))
        keyboard.add(telebot.types.InlineKeyboardButton(text="(063)182-63-61", callback_data=" "))
        keyboard.add(telebot.types.InlineKeyboardButton(text=" ", callback_data=" "))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Приймальня директора:", callback_data=" "))
        keyboard.add(telebot.types.InlineKeyboardButton(text="(061)720-55-26", callback_data=" "))
        keyboard.add(telebot.types.InlineKeyboardButton(text=" ", callback_data=" "))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Ел.пошта коледжу:", callback_data=" "))
        keyboard.add(telebot.types.InlineKeyboardButton(text="zac.office@meta.ua", callback_data=" "))
        keyboard.add(telebot.types.InlineKeyboardButton(text=" ", callback_data=" "))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Вебсайт коледжу", url="zac.org.ua"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data="Спеціальності_Назад"))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Контакти:", reply_markup=keyboard)
    current_time = datetime.datetime.now().time()
    formatted_time = current_time.strftime("%Hh %Mmin %Ssec")
    if call.from_user.first_name != None: name = f"| {call.from_user.first_name}\n"
    else: name = ""
    if call.from_user.last_name != None: last_name = f"| {call.from_user.last_name}\n"
    else: last_name = ""
    if call.from_user.username != None: username = f"| @{call.from_user.username}\n"
    else: username = ""
    vuvod = f"|--------------------\n| {call.from_user.id}\n{name}{last_name}{username}|--------------------\n| {call.data}\n|--------------------\n| {formatted_time}\n|--------------------\n"
    print(vuvod)
    
bot.infinity_polling(timeout=999, long_polling_timeout = 5)
