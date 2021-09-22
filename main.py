from python_bitvavo_api.bitvavo import Bitvavo
import time

# build api up
bitvavo = Bitvavo({
    'APIKEY': '<apikey>',
    'APISECRET': '<secret>',
    'RESTURL': 'https://api.bitvavo.com/v2',
    'WSURL': 'wss://ws.bitvavo.com/v2/',
    'ACCESSWINDOW': 10000,
    'DEBUGGING': False
})


def checkbalance():
    balance = bitvavo.balance({})
    #todo if statement to check if api is active.
    for currency in balance:
        if currency['symbol'] == 'EUR':
            return float(currency['available'])

def checkorderstatus(orderId):
    order_status = bitvavo.getOrder('ADA-EUR', orderId)
    price = order_status['fills'][0]['price']
    amount = order_status['fills'][0]['amount']
    fee = round(float(order_status['fills'][0]['fee']), 3)
    return amount, price, fee


def buyada(amount_eur=5):
    if checkbalance() > amount_eur:
        order = bitvavo.placeOrder('ADA-EUR', 'buy', 'market', {'amountQuote': amount_eur})
        if order['status'] != 'filled':
            print('Error! - ' + order['error'])
        else:
            order_status = checkorderstatus(order['orderId'])
            print("Successfully bought:")
            print(order_status[0] + ' ADA')
            print(order_status[1] + ' EUR per ADA')
            print(str(order_status[2]) + ' EUR in fees')
    else:
        print("Not enough balance, please top up your account")


buyada()
