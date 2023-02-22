from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
from helpers import *
from telegramBot import *
import os
import sys

apiKey = os.getenv("apiKey", default=None)
secretKey = os.getenv("secretKey", default=None)
print('Hello apiKey! {apiKey}', file=sys.stderr)
print('Hello secretKey! {secretKey}', file=sys.stderr)
client = Client(apiKey, secretKey)


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

def buy_receive(coin, stableCoin, pair):
    stableCoinBalance = get_stablecoin_balance(stableCoin)
    print(stableCoinBalance)
    # telegram
    while stableCoinBalance > 10:
        create_buy_market_order(pair, stableCoinBalance)
        stableCoinBalance = get_stablecoin_balance(stableCoin)
    coinBalance = get_balance(coin)
    stableCoinBalance = get_stablecoin_balance(stableCoin)
    price = get_price(pair)
    print(coinBalance)
    print(stableCoinBalance)
    print(price)
    # telegram

def sell_receive(coin, stableCoin, pair):
    coinBalance = get_balance(coin)
    print(coinBalance)
    # telegram
    while coinBalance > 0.1:
        create_sell_market_order(pair, coinBalance)
        coinBalance = get_balance(coin)
    coinBalance = get_balance(coin)
    stableCoinBalance = get_stablecoin_balance(stableCoin)
    price = get_price(pair)
    print(coinBalance)
    print(stableCoinBalance)
    print(price)
    # telegram



# sent to telegram 

