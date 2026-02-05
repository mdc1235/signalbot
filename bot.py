
import telebot
import random
import time
import threading
from datetime import datetime

BOT_TOKEN = "PUT_TOKEN"
CHAT_ID = "PUT_CHANNEL_ID"

bot = telebot.TeleBot(BOT_TOKEN)

SIGNALS_PER_SLOT = 4
GAP = 120

pairs = ["EUR/USD","GBP/USD","USD/JPY","AUD/USD","USD/CHF","EUR/JPY","GBP/JPY"]
directions = ["UP 📈","DOWN 📉"]

def send_result(pair,direction):
    result = random.choices(["WIN ✅","LOSS ❌"], weights=[90,10])[0]
    bot.send_message(CHAT_ID,f"Result: {pair} {direction} → {result}")

def send_signals():
    for i in range(SIGNALS_PER_SLOT):
        pair = random.choice(pairs)
        direction = random.choice(directions)

        now = datetime.now()
        entry = now.strftime("%I:%M %p")

        msg=f"""
🔥 VIP REAL MARKET SIGNAL 🔥

Pair: {pair}
Signal: {direction}
Candle: 1 MIN ⏱
Entry Time: {entry}
Expiry: 1 MIN
"""
        bot.send_message(CHAT_ID,msg)

        threading.Timer(60, send_result, args=(pair,direction)).start()

        if i < SIGNALS_PER_SLOT-1:
            time.sleep(GAP)

def scheduler():
    sent_morning=False
    sent_night=False
    while True:
        now=datetime.now()

        if now.hour==10 and now.minute==30 and not sent_morning:
            send_signals()
            sent_morning=True

        if now.hour==21 and now.minute==0 and not sent_night:
            send_signals()
            sent_night=True

        if now.hour==0 and now.minute==1:
            sent_morning=False
            sent_night=False

        time.sleep(20)

threading.Thread(target=scheduler).start()

print("Bot running...")
bot.infinity_polling()
