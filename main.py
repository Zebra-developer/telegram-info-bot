import os
import telebot
import requests
from dotenv import load_dotenv
from flask import Flask, request


load_dotenv() 


TOKEN = os.getenv('TOKEN') # подгружаем токен из пространства
bot = telebot.TeleBot(TOKEN)
WEBHOOK_URL = os.getenv('WEBHOOK_URL')
app = Flask(__name__)


# /help команда вызова помощи по командам бота
@bot.message_handler(commands=['help'])
def help_message(message):
    help_text = (
        "📌 Доступные команды:\n"
        "/start — запустить бота\n"
        "/help — список команд\n"
        "/info — информация о боте\n"
        "/quote — цитата дня\n"
        "/usd — курс доллара\n"
        "/weather <город> — погода\n"
        "/news — последние новости"
    )
    bot.send_message(message.chat.id, help_text)


# /info команда информации о боте и его владельце 
@bot.message_handler(commands=['info'])
def info_message(message):
    info_text = (
        "🤖 Этот бот создан на Python с использованием библиотеки TeleBot.\n"
        "Он предоставляет:\n"
        "— Цитаты\n— Курс валют\n— Погоду\n— Новости (в разработке)\n\n"
        "💡 Автор: Zebra-developer\n"
        "✉️ Связь: напиши, если хочешь свой бот!"
    )
    bot.send_message(message.chat.id, info_text)


# /start пишем старт и смотрим команды тестового бота 
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Я бот.\nНапиши /help, /quote, /usd или /weather <город>")


# /quote команда просмотра фразы дня
@bot.message_handler(commands=['quote'])
def quote_message(message):
    try:
        r = requests.get("https://zenquotes.io/api/random")
        if r.status_code == 200:
            data = r.json()[0]
            quote = data["q"]
            author = data["a"]
            bot.send_message(message.chat.id, f"💬 {quote}\n— {author}")
        else:
            bot.send_message(message.chat.id, "Не удалось получить цитату.")
    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка: {e}")


# /usd команда просмотра курса доллара 
@bot.message_handler(commands=['usd'])
def usd_message(message):
    r = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
    if r.status_code == 200:
        usd = r.json()["Valute"]["USD"]["Value"]
        bot.send_message(message.chat.id, f"💵 Курс USD: {usd:.2f} ₽")
    else:
        bot.send_message(message.chat.id, "Не удалось получить курс валют.")


# /weather команда просмотра погоды
@bot.message_handler(commands=['weather'])
def weather_message(message):
    parts = message.text.split()
    if len(parts) < 2:
        bot.send_message(message.chat.id, "Напиши: /weather Город")
        return
    city = " ".join(parts[1:])
    API_KEY = os.getenv("TOKEN_OPENWEATHER")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ru"
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        desc = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        bot.send_message(message.chat.id, f"🌤 В {city} сейчас: {desc}, {temp}°C")
    else:
        bot.send_message(message.chat.id, "Не удалось получить погоду.")


@bot.message_handler(commands=['news'])
def news_message(message):
    bot.send_message(message.chat.id, "🗞 Команда новостей в разработке.")


@app.route(f'{TOKEN}', method=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return 'ok', 200


# Запуск
print("Bot starting...")
if __name__ == "__main__":
    url = os.getenv("WEBHOOK_URL") 
    bot.remove_webhook()
    bot.set_webhook(url=f"{url}/{TOKEN}")
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000))