import os
import telebot
from flask import Flask, request
import logging

# Настройки
TOKEN = os.environ.get('BOT_TOKEN', 'YOUR_TOKEN_HERE')
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# Логирование
logging.basicConfig(level=logging.INFO)

# Скрипты база
SCRIPTS = {
    "brainrot": {
        "name": "🧠 Brainrot Auto Steal",
        "code": '''-- Steal a Brainrot Auto Farm
getgenv().AutoSteal = true
print("✅ Brainrot Hack Activated!")''',
        "desc": "Авто-стейл для Steal a Brainrot"
    },
    "trident": {
        "name": "🎯 Trident Silent Aim",
        "code": '''-- Trident Survival Hack
print("🎯 Loading Trident Hack...")
-- Вставьте ваш скрипт здесь''',
        "desc": "Silent Aim для Trident Survival"
    }
}

# Команда /start
@bot.message_handler(commands=['start'])
def start(message):
    text = f"""
⚡ <b>RYZEN CONTROL BOT</b>

👋 Привет, {message.from_user.first_name}!
🤖 Бот: @contr1488ol_bot

🎮 <b>Команды:</b>
/brainrot - Steal a Brainrot
/trident - Trident Survival
/help - Помощь

💡 Бот работает 24/7 на Heroku
"""
    bot.send_message(message.chat.id, text, parse_mode='HTML')

# Команда /brainrot
@bot.message_handler(commands=['brainrot'])
def brainrot(message):
    script = SCRIPTS["brainrot"]
    bot.send_message(message.chat.id, 
        f"<b>{script['name']}</b>\n{script['desc']}\n\n<code>{script['code']}</code>",
        parse_mode='HTML')

# Команда /trident
@bot.message_handler(commands=['trident'])
def trident(message):
    script = SCRIPTS["trident"]
    bot.send_message(message.chat.id,
        f"<b>{script['name']}</b>\n{script['desc']}\n\n<code>{script['code']}</code>",
        parse_mode='HTML')

# Команда /help
@bot.message_handler(commands=['help'])
def help_cmd(message):
    help_text = """
🆘 <b>ПОМОЩЬ</b>

1️⃣ <b>Получить скрипт:</b>
   /brainrot - для Steal a Brainrot
   /trident - для Trident Survival

2️⃣ <b>Использовать:</b>
   • Скопируйте код
   • Откройте Roblox игру
   • Вставьте в Delta/Synapse
   • Нажмите Execute

📞 Бот работает 24/7!
"""
    bot.send_message(message.chat.id, help_text, parse_mode='HTML')

# Для Heroku webhook
@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@app.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://ваше-приложение.herokuapp.com/' + TOKEN)
    return "Bot is running!", 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
