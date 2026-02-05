from telegram import Bot
from telegram.ext import Updater, CommandHandler
import random, time, threading
from datetime import datetime

TOKEN = "8012086587:AAE6IgMbSe-vTAvzkAlodZtqjZe0Q5x_dWU"
CHAT_ID = "6181352243"

bot = Bot(token=TOKEN)

pairs = ["EUR/USD","GBP/USD","USD/JPY","AUD/USD","USD/CHF"]
dirs = ["UP 📈","DOWN 📉"]

def start(update, context):
    update.message.reply_text("🔥 VIP Signal Bot Started 🔥")

def send_result(pair,dir):
    result=random.choices(["WIN ✅","LOSS ❌"],weights=[90,10])[0]
    bot.send_message(chat_id=CHAT_ID,text=f"🏆 Result: {pair} {dir} → {result}")

def send_signals():
    for i in range(4):
        pair=random.choice(pairs)
        direction=random.choice(dirs)
        now=datetime.now().strftime("%I:%M %p")

        msg=f"""
🔥 VIP SIGNAL 🔥
Pair: {pair}
Signal: {direction}
Candle: 1 MIN
Entry: {now}
Expiry: 1 MIN
"""
        bot.send_message(chat_id=CHAT_ID,text=msg)

        threading.Timer(60,send_result,args=(pair,direction)).start()
        time.sleep(120)

def scheduler():
    sent_m=False
    sent_n=False
    while True:
        now=datetime.now()

        if now.hour==10 and now.minute==30 and not sent_m:
            send_signals()
            sent_m=True

        if now.hour==21 and now.minute==0 and not sent_n:
            send_signals()
            sent_n=True

        if now.hour==0 and now.minute==1:
            sent_m=False
            sent_n=False

        time.sleep(20)

def main():
    updater = Updater(TOKEN,use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))

    threading.Thread(target=scheduler).start()

    updater.start_polling()
    updater.idle()

main()
