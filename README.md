# 🤖 Telegram Info Bot

Многофункциональный Telegram-бот на Python, развернутый на Render. Поддерживает полезные команды — от курса валют и погоды до случайных цитат.

## 📌 Возможности

- 💬 `/quote` — случайная цитата дня (ZenQuotes API)
- 💵 `/usd` — курс доллара по ЦБ РФ (CBR JSON API)
- 🌤 `/weather <город>` — текущая погода (OpenWeather API)
- 🗞 `/news` — главные новости *(в разработке)*
- 🛠 `/help`, `/info` — список команд и информация о боте

---

## 🚀 Используемые технологии

- Python 3.x
- [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)
- Flask — Webhook-сервер
- requests
- python-dotenv
- API-сервисы:
  - [OpenWeatherMap](https://openweathermap.org/api)
  - [ZenQuotes](https://zenquotes.io/)
  - [ЦБ РФ JSON API](https://www.cbr-xml-daily.ru/)
  - *(News API — в разработке)*

---

## ✍️ Автор
Zebra-developer
Моя визитка - [Zebra_developer](https://my-business-card-4qs2.onrender.com)

## 📦 Установка и запуск локально

```bash
git clone https://github.com/Zebra-developer/telegram-info-bot.git
cd telegram-info-bot

pip install -r requirements.txt

