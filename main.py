from python_bitvavo_api.bitvavo import Bitvavo
import time

#build api up
bitvavo = Bitvavo({
  'APIKEY': '7502ca59801b417b156b4fbc699a19d475fce3259f707e89af722675b25a855a',
  'APISECRET': '14680e318131e3695dd819207c00cb4359c26ab6696a2b4c9b80f534e5ec564732284be6b0f54c670471d006eec4c54fed9a87eae019ef9e6b14443915d12a59',
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