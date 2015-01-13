import json, urllib2 
def BitcoinExchangeRate():
    #Coinbase exchange rate as float
    sp = urllib2.urlopen("https://coinbase.com/api/v1/prices/spot_rate")
    data = json.load(sp)
    #print(data)
    price =  data["amount"]
    #print(float(price))
    return float(price)
def LitecoinExchangeRate():
    #btce exchange rate ltc/btc
    sp = urllib2.urlopen("https://btc-e.com/api/2/ltc_btc/ticker")
    data = json.load(sp)
    sellPrice = data["ticker"]
    sellPrice = sellPrice["sell"]    
    return float(sellPrice)
def returnExchangeRates():
    #print(BitcoinExchangeRate())
    #print(LitecoinExchangeRate())
    print(BitcoinExchangeRate()*LitecoinExchangeRate())
returnExchangeRates()
