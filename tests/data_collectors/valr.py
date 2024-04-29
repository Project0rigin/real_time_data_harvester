import logging
import requests

class ValrCollector:
    def __init__(self, base_url, api_key, symbol, symbol_price_ticker_endpoint_binance):
        self.base_url = base_url
        self.api_key = api_key
        self.symbol = symbol
        self.symbol_price_ticker_endpoint = symbol_price_ticker_endpoint_binance

    def get_ticker_price(self):
        # Get the latest price of a symbol
        logging.info(f"Retrieving current price for {self.symbol}")
        try:
            response = requests.get(
                f"{self.base_url}{self.symbol_price_ticker_endpoint}?symbol={self.symbol}",
                headers={"X-MBX-APIKEY": self.api_key},
            )
            response.raise_for_status()
            price = response.json()["price"]
            logging.info(f"Current price for {self.symbol}: {price}")

            return price
        except requests.RequestException as e:
            logging.error(f"Could not retrieve current price for {self.symbol}: {str(e)}")
            return None
