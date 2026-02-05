
import telebot
import random
import time
import threading
from datetime import datetime, timedelta
import os

BOT_TOKEN = os.getenv("8012086587:AAHS)
CHAT_ID = "6181352243"

bot = telebot.TeleBot(BOT_TOKEN)

pairs = ["EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", "USD/CHF"]
dirs = ["UP 📈", "DOWN 📉"]

SIGNALS_PER_SLOT = 4
GAP = 120  # 2 min gap

selected_market = "REAL"
selected_platform = "Pocket Option"

# start command
@bot.message_handler(commands=["start"])
def start(msg):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("REAL MARKET", "OTC MARKET")
    markup.add("Pocket Option", "Quotex")
    bot.send_message(msg.chat.id,"Select market & platform",reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def choose(m):
    global selected_market, selected_platform

    if m.text == "REAL MARKET":
        selected_market = "REAL"
        bot.reply_to(m,"✅ Real Market Selected")

    elif m.text == "OTC MARKET":
        selected_market = "OTC"
        bot.reply_to(m,"✅ OTC Selected")

    elif m.text == "Pocket Option":
        selected_platform = "Pocket Option"
        bot.reply_to(m,"✅ Pocket Option Selected")

    elif m.text == "Quotex":
        selected_platform = "Quotex"
        bot.reply_to(m,"✅ Quotex Selected")

# send signal
def send_signal():
    for i in range(SIGNALS_PER_SLOT):

        pair=random.choice(pairs)
        direction=random.choice(dirs)

        entry_time=(datetime.now()+timedelta(minutes=1)).strftime("%I:%M %p")

        bot.send_message(
            CHAT_ID,
f"""🔥 VIP SMART SIGNAL 🔥

Broker: {selected_platform}
Market: {selected_market}

Pair: {pair}
Signal: {direction}

Entry Time: {entry_time}
Candle: 1 MIN
Expiry: 1 MIN"""
        )

        time.sleep(GAP)

# auto time scheduler
def scheduler():
    while True:
        now=datetime.now().strftime("%H:%M")

        if now in ["10:30","21:00"]:
            send_signal()
            time.sleep(240)

        time.sleep(20)

threading.Thread(target=scheduler).start()
bot.infinity_polling()
