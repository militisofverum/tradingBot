from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
from helpers import *
from telegramBot import *
import os
import time

# apiKey = os.getenv("apiKey", default=None)
# secretKey = os.getenv("secretKey", default=None)
# client = Client(apiKey, secretKey)
client = Client("jbSBLFwfIJsKG2A75QFQoEEInNdlozA2pJ2gkNNbJatHsVlLprGNStPvy6vU24M2", "uPjScnrYvUNFf9As9YlFDCrp1cyHxcFmQfpwnnvchw86tdMJY0Lm3EAKmwsQp40K",testnet=True)

def create_buy_market_order(pair, stableCoinBalance):
    order = client.create_order(
        symbol=pair,
        side=Client.SIDE_BUY,
        type=Client.ORDER_TYPE_MARKET,
        quoteOrderQty=stableCoinBalance)
    print(order)

def create_sell_market_order(pair, coinBalance):
    order = client.create_order(
        symbol=pair,
        side=Client.SIDE_SELL,
        type=Client.ORDER_TYPE_MARKET,
        quantity=coinBalance)
    print(order)

def get_balance(coin):
    return toBalance(client.get_asset_balance(coin)['free'])

def get_stablecoin_balance(stableCoin):
    return toBalance(client.get_asset_balance(stableCoin)['free'])

def get_price(pair):
    return toPrice(client.get_avg_price(symbol=pair)['price'])

def buy_receive(coin, stableCoin, pair, retryCount = 5):
    try: 
        stableCoinBalance = get_stablecoin_balance(stableCoin)
        send_telegram_message("Buy started stableCoinBalance: " + str(stableCoinBalance))
        while stableCoinBalance > 10:
            create_buy_market_order(pair, stableCoinBalance)
            stableCoinBalance = get_stablecoin_balance(stableCoin)
            send_telegram_message("Buy started stableCoinBalance: " + str(stableCoinBalance))
        coinBalance = get_balance(coin)
        stableCoinBalance = get_stablecoin_balance(stableCoin)
        price = get_price(pair)
        send_telegram_message("Buy finished stableCoinBalance: " + str(stableCoinBalance) + " coinBalance: " + str(coinBalance) + " price: " + str(price))
    except Exception as e:    
        send_telegram_message("Error:" + str(e))
        if retryCount > 0:
            time.sleep(10)
            buy_receive(coin, stableCoin, pair, retryCount - 1)
    
def sell_receive(coin, stableCoin, pair, retryCount = 5):
    try:
        coinBalance = get_balance(coin)
        send_telegram_message("Sell started coinBalance: " + str(coinBalance))
        while coinBalance > 0.1:
            create_sell_market_order(pair, coinBalance)
            coinBalance = get_balance(coin)
            send_telegram_message("Sell started coinBalance: " + str(coinBalance))
        coinBalance = get_balance(coin)
        stableCoinBalance = get_stablecoin_balance(stableCoin)
        price = get_price(pair)
        send_telegram_message("Sell finished stableCoinBalance: " + str(stableCoinBalance) + " coinBalance: " + str(coinBalance) + " price: " + str(price))
    except Exception as e:    
        send_telegram_message("Error:" + str(e))
        if retryCount > 0:
            time.sleep(10)
            sell_receive(coin, stableCoin, pair, retryCount - 1)
        
