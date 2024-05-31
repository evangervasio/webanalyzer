from requests import get
from urllib.parse import urlparse

class CoinloreApi:
    def __init__(self, coin, exchange):
        self.coin = coin
        self.exchange = exchange

    #determines what method to call based on the variables set 
    def determine(self):
        if not self.coin=="":
            self.apiCoin()
        if not self.exchange=="":
            self.apiExchange()
    
    def call_api_once(self, url):
        ENDPOINT = 'https://api.coinlore.net/api/' + url
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        try:
            resp = get(ENDPOINT, headers=headers)
            print("Response status code:", resp.status_code)
            print("Response text:", resp.text)
            resp.raise_for_status()
            return resp.json()
        except Exception as e:
            print("Error occurred:", e)
            return False
        
    def getCoin(self):
        url="ticker/?id="+self.coin
        self.call_api_once(url)

    def getExchange(self):
        url="exchange/?id="+self.exchange
        self.call_api_once(url)
        print(1)

    def getAllCoins(self):
        print(1)
    
    def getAllExchanges(self):
        print(1)
