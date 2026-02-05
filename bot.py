import telebot
import random
import time

TOKEN = "8012086587:AAGj86wGPXX8OEPfxghs3_2NamaI3sTnC7A"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(msg.chat.id,"Welcome to VIP Trading Signal Bot 📊")

while True:
    signal = random.choice(["UP 📈","DOWN 📉"])
    text = f"🔥 1 MIN SIGNAL\nSignal: {signal}\nEntry: Next candle"
    try:
        bot.send_message(msg.chat.id,text)
    except:
        pass
    time.sleep(60)

bot.polling()
