from flask import Flask,request
from binanceRequests import *
from telegramBot import *

app = Flask(__name__)
@app.route('/webhook',methods=['POST'])
def webhook():
    coin = "BNB"
    stableCoin = "BUSD"
    pair = coin + stableCoin
    message = request.data.decode('UTF-8')
    if message == 'BUY':
        buy_receive(coin, stableCoin, pair)
    if message == 'SELL':
        sell_receive(coin, stableCoin, pair)
    if message == 'balance':
        balance = get_balance(coin)
        stableCoinBalance = get_balance(stableCoin)
        send_telegram_message("balance Coin: " + str(balance) + "balance stable Coin: " + str(stableCoinBalance))
    return 'hello to me'
    
    

if __name__ == '__main__':
    app.run(debug=True, port=2000)
