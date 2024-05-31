from requests import get
from urllib.parse import urlparse

class CoinloreApi:
    def __init__(self, coin="", exchange=""):
        self.coin = coin
        self.exchange = exchange
        self.exchanges_data = []  # List to store exchange information
        self.coins_data = []  # List to store coin information

    def determine(self):
        if not self.coin == "":
            return self.getCoin()
        if not self.exchange == "":
            return self.getExchange()

    def call_api_once(self, url):
        ENDPOINT = 'https://api.coinlore.net/api/' + url
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        try:
            resp = get(ENDPOINT, headers=headers)
            resp.raise_for_status()
            return resp.json()
        except Exception as e:
            print("Error occurred:", e)
            return False

    def getCoin(self):
        url = "ticker/?id=" + self.coin
        return self.call_api_once(url)

    def getExchange(self):
        url = "exchange/?id=" + self.exchange
        exchange_data = self.call_api_once(url)
        if exchange_data:
            self.exchanges_data.append(exchange_data)
            return exchange_data

    def getAllCoins(self):
        url = "tickers"
        all_coins = self.call_api_once(url)
        if all_coins:
            self.coins_data.extend(all_coins['data'])  # Assuming the response has a 'data' key
            return all_coins['data']

    def getAllExchanges(self):
        url = "exchanges"
        all_exchanges = self.call_api_once(url)
        if all_exchanges:
            self.exchanges_data.extend(all_exchanges)
            return all_exchanges