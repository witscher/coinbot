#!/usr/bin/env python

import coinbase.wallet
import requests
import os

currency =  os.environ['CURRENCY']
price =  os.environ['PRICE']
api_key = os.environ['API_KEY']
api_secret = os.environ['API_SECRET']

#from coinbase.wallet.client import Client



#client = Client(api_key, api_secret)

url = 'https://api.coinbase.com/v2/prices/'+ currency + '-EUR/' + price
headers = {'CB-VERSION': '2017-04-08'}


r = requests.get(url, headers=headers)
# curl -H "CB-VERSION: 2015-04-08"  "https://api.coinbase.com./v2/prices/LTC-EUR/buy"
print(r.json())
#price = client.get_sell_price(currency_pair = 'LTC-EUR')
#print (price)
