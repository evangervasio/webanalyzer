from requests import get
from urllib.parse import urlparse

class CoinloreApi:
    def __init__(self, website):
        self.website = website

    def call_api_once(self):
        domain = '{uri.netloc}'.format(uri=urlparse(self.website))
        domain = domain.replace("www.", "")
        ENDPOINT = 'https://data.similarweb.com/api/v1/data?domain=' + domain
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
