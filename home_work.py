# бот для парсинга данных с таблетка бай и выдачи резуьтата
# по наименьшей стоимости таблеток небилетплюс в Бобруйске
import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
URL = 'https://tabletka.by/result?ls=16945&region=56'
TOKEN = "5919240047:AAG3I-yxpMogdFKtKWmUJzQVLkctzwz18lE"
def parcer(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    base = soup.find_all('tr', class_="tr-border")
    full_list = []
    for item in base:
        price = item.find('span', class_="price-value").text.strip()
        full_list.append(price)
        apteka = item.find('div', class_="tooltip-info-header").text.strip()
        full_list.append(apteka)
        adress = item.find('td', class_="address tooltip-info").find("span").text.strip()
        full_list.append(adress)
    return full_list
list_of_adress = parcer(URL)
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=["start"])

def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttom1 = types.KeyboardButton("Да")
    buttom2 = types.KeyboardButton("Нет")
    markup.add(buttom1, buttom2)
    bot.send_message(message.chat.id, "Поищем небилет плюс в Бобруйске?", reply_markup=markup)

@bot.message_handler(content_types=["text"])
def searc(message):
    if message.text.lower() == "да":
        bot.send_message(message.chat.id, str(list_of_adress))
    elif message.text.lower() == "нет":
        bot.send_message(message.chat.id, "Понял. Готов помочь в любое время")
    else:
        bot.send_message(message.chat.id, "Такой команды пока не знаю")

bot.polling(none_stop = True)







