from flask import Flask,request
from binanceRequests import *
from telegramBot import *

app = Flask(__name__)
@app.route('/webhook',methods=['POST'])
def webhook():
# Generating a timestamp.
    coin = "BNB"
    stableCoin = "BUSD"
    pair = coin + stableCoin
    balance = get_balance("BUSD")
    send_telegram_message("Receive message from trading view, balance: {balance}")
    message = request.data.decode('UTF-8')
    if message == 'BUY':
        # buy_receive(coin, stableCoin, pair)
        print('bought')
    if message == 'SELL':
        # sell_receive(coin, stableCoin, pair)
        print('sold')
    return 'hello to me'
