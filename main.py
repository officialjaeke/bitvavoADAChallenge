from python_bitvavo_api.bitvavo import Bitvavo
import time

#build api up
bitvavo = Bitvavo({
  'APIKEY': '<apikey>',
  'APISECRET': '<secret>',
  'RESTURL': 'https://api.bitvavo.com/v2',
  'WSURL': 'wss://ws.bitvavo.com/v2/',
  'ACCESSWINDOW': 10000,
  'DEBUGGING': False
})

def checkBalance():
    balance = bitvavo.balance({})
    for currency in balance:
        if currency['symbol'] == 'EUR':
            return currency['available']

def buyADA(amount_eur = 5):
    if checkBalance() > amount_eur:
        order = bitvavo.placeOrder('ADA-EUR', 'buy', 'market', {'amountQuote': amount_eur})
        time.sleep(5)
        order_status = bitvavo.getOrder('ADA-EUR', order['orderId'])
        if order_status['status'] == 'filled':
            print(order_status['amount'] + 'ADA bought at' + order_status['price'])
        else:
            print(order_status)
    else:
        print("not enough balance, please top up your account")

buyADA(5)