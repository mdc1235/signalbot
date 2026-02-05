
import telebot
import random
import time
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(msg.chat.id,"🔥 VIP Signal Bot Started 🔥")

    while True:
        signal = random.choice(["UP 📈","DOWN 📉"])
        pair = random.choice(["EUR/USD","GBP/USD","USD/JPY","AUD/USD"])

        text = f"🔥 1 MIN SIGNAL\n\nPair: {pair}\nSignal: {signal}"

        try:
            bot.send_message(msg.chat.id,text)
        except:
            pass

        time.sleep(60)

print("Bot running...")
bot.infinity_polling()
