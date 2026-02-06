
import os
import telebot
import random
import time
import threading
import pytz
from datetime import datetime, timedelta

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = "6181352243"

bot = telebot.TeleBot(BOT_TOKEN, parse_mode="HTML")

pairs = ["EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", "USD/CHF"]
markets = ["REAL MARKET", "OTC"]
platforms = ["Pocket Option"]
directions = ["UP 📈", "DOWN 📉"]

@bot.message_handler(commands=["start"])
def start(msg):
    bot.reply_to(
        msg,
        "🔥 <b>VIP SIGNAL BOT STARTED</b>\n\n"
        "🇮🇳 India time signals\n"
        "⏱ Entry time ke sath signal\n"
        "📊 REAL / OTC MARKET\n"
        "💹 Pocket Option"
    )

def send_signal():
    pair = random.choice(pairs)
    direction = random.choice(directions)
    market = random.choice(markets)
    platform = random.choice(platforms)

    # 🇮🇳 India timezone
    ist = pytz.timezone('Asia/Kolkata')
    signal_time = datetime.now(ist)
    entry_time = signal_time + timedelta(minutes=1)

    text = (
        f"📊 <b>{platform}</b>\n"
        f"🟡 <b>{market}</b>\n\n"
        f"💱 Pair: <b>{pair}</b>\n"
        f"📈 Direction: <b>{direction}</b>\n\n"
        f"🕒 Signal Time: <b>{signal_time.strftime('%H:%M:%S')}</b>\n"
        f"⏰ Entry Time: <b>{entry_time.strftime('%H:%M:%S')}</b>\n"
        f"⌛ Expiry: 1 Minute"
    )

    bot.send_message(CHAT_ID, text)

def loop():
    while True:
        send_signal()
        time.sleep(60)  # 1 min gap

threading.Thread(target=loop).start()

bot.infinity_polling()
