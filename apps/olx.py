import re, datetime, telebot, bs4, requests
from urllib.parse import urlparse, unquote

PARAMS = {
    1: 'январь',
    2: 'февраль',
    3: 'март',
    4: 'апрель',
    5: 'май',
    6: 'июнь',
    7: 'июль',
    8: 'август',
    9: 'сентябрь',
    10: 'октябрь',
    11: 'ноябрь',
    12: 'декабрь',
}

def clean_price_olx(price):
    if price == 'Не указано' or price == 'Обмен':
        return price
    else:
        result = price
        return result.replace(' ', '')


def clean_date_olx(publications_date):
    res = re.search('(.*) \d{2}:\d{2}', publications_date)

    if res and res.group(1) == 'Сегодня':
        date = f'{datetime.today().day} {PARAMS[datetime.today().month]}'
        return date
    elif res and res.group(1) == 'Вчера':
        date = f'{datetime.today().day - 1} {PARAMS[datetime.today().month]}'
        return date
    else:
        return publications_date


def clean_name_olx(name):
    return name.replace(',', ' ').replace(';', ' ')



def get_data_olx(html, message, token, page):
    import time
    from telebot import types
    bot = telebot.TeleBot(token)
    bot.send_message(message.chat.id, "<code>Йде пошук...</code>", parse_mode='HTML')
    soup = bs4.BeautifulSoup(html, 'lxml')
    trs = soup.find('table', id='offers_table').findAll('tr', class_='wrap')
    global number_obyavlenie_olx
    beta_msg = ""
    release_msg = ""
    time.sleep(3)
    bot.delete_message(chat_id=message.chat.id, message_id=message.id+1)
    for tr in trs:
        number_obyavlenie_olx += 1
        try:
            price = tr.find('p', class_='price').find('strong').text
        except AttributeError:
            price = 'Не указано'

        delivery = tr.find('div', class_='olx-delivery-badge__suggest hidden')
        
        try:
            data = {
                'href': tr.find('a').get('href'),
                'name': clean_name_olx(tr.find('strong').text),
                'date': clean_date_olx(tr.find('td', valign="bottom").findAll('span')[1].text.strip()),
                'place': tr.find('td', valign="bottom").findAll('span')[0].text.strip(),
                'category': tr.find('small', class_='breadcrumb x-normal').text.strip(),
                'price': clean_price_olx(price),
                'olxdelivery': "Так" if delivery else "Ні"
            }
            description = ""
            description += f"<code>№ {str(number_obyavlenie_olx)}\n"
            Name = data['name']
            Url = data['href']
            description += f'</code><a href="{Url}">{Name}</a><code>\n'
            description += f"Дата: {data['date']}\n"
            description += f"Місто: {data['place']}\n"
            description += f"Категорія: {data['category']}\n"
            description += f"Ціна: {data['price']}\n"
            description += f"OLX доставка: {data['olxdelivery']}</code>\n\n"
            beta_msg += description
        except:
            pass
        current_length = len(beta_msg)
        if current_length < 4000:
            release_msg += description
        else:
            bot.send_message(message.chat.id, f"<code>{release_msg}</code>", parse_mode='HTML', disable_web_page_preview=True)
            beta_msg = description
            release_msg = description
    if beta_msg:
        bot.send_message(message.chat.id, f"<code>{beta_msg}</code>", parse_mode='HTML', disable_web_page_preview=True)
    olx_pages = types.InlineKeyboardMarkup()
    page_next = str(page + 1)
    page_next = types.InlineKeyboardButton(text=f"{page_next} ▶️", callback_data='page_olx_next')
    page_back = str(page - 1)
    page_back = types.InlineKeyboardButton(text=f"◀️ {page_back}", callback_data='page_olx_back')

    if page == 1:
        olx_pages.add(page_next)
    else:
        olx_pages.add(page_back, page_next)

    bot.send_message(message.chat.id, f"<code>Сторінка під номером: '{page}'</code>", reply_markup=olx_pages, parse_mode='HTML')



def get_html_olx(url):
    r = requests.get(url)
    return r.text if re.search(URL, r.url) else r.text


def main_olx(message, token, page, url):
    bot = telebot.TeleBot(token)
    try:
        html = get_html_olx(f'{url}?page={page}')
        if html:
            if "Нам жаль, но мы не нашли эту страницу" in html: bot.reply_to(message, "<code>Нічого не знайдено(</code>", parse_mode='HTML')
            else:
                try: get_data_olx(html, message, token, page)
                except Exception as e:
                    print(e)
                    bot.reply_to(message, "<code>Спробуйте пізніше або перефразуйте prompt</code>", parse_mode='HTML')
    except Exception as e: print(e)



def search(prompt, message, token, page):
    prompt = prompt.replace(" ", "-")
    page = page
    global URL
    URL = f'https://www.olx.ua/list/q-{prompt}/'
    global url
    url = URL
    global number_obyavlenie_olx
    number_obyavlenie_olx = 0
    main_olx(message, token, page, url)


