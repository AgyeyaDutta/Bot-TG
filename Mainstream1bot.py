import telegram.ext
import telegram
import pandas_datareader.data as web
import cryptocompare
import os
with open('C:\\Users\\Agyeya\\Desktop\\TB\\Codes\\token.txt','r') as f:
    TOKEN = f.read()

def start(update, context):
    update.message.reply_text("""send in format- /crypto 'Coin name'""")


def crypto(update, context):
    ticker = context.args[0]
    data = cryptocompare.get_price(ticker, 'USD')
    update.message.reply_text(f"{data}")


updater=telegram.ext.Updater(TOKEN, use_context=True)
dp= updater.dispatcher

dp.add_handler(telegram.ext.CommandHandler("start",start))
dp.add_handler(telegram.ext.CommandHandler("crypto",crypto))

updater.start_polling()
updater.idle()
