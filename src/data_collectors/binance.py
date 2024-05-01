import websockets
import asyncio
import requests
import logging

#TODO build on websocket logic
class Binance:
    def __init__(self, base_url, api_key, asset_pairs):
        self.base_url = base_url
        self.api_key = api_key
        self.asset_pairs = asset_pairs

    async def listen_for_trades(self, ws_url):
        async with websockets.connect(f"{ws_url}{self.asset_pairs[0]}@trade") as websocket:
            while True:
                message = await websocket.recv()
                print("Received message:", message)

    # def get_price(self, ticker, symbol_price_ticker_endpoint):
    #     try:
    #         response = requests.get(
    #             f'{self.base_url}{symbol_price_ticker_endpoint}?symbol={ticker}',
    #             headers = {
    #             'X-MBX-APIKEY': self.api_key,
    #         }
    #         )
    #         response.raise_for_status()
    #         data = response.json()
    #         price = data.get("price")
    #         if price:
    #             logging.info("Price for %s: %s", ticker, price)
    #             return price
    #         else:
    #             logging.info("No price information found for %s", ticker)
    #             return None
    #     except requests.RequestException as e:
    #         logging.error("Error retrieving price for %s: %s", str(e))
    #         return None
# /{self.asset_pairs[1]}@trade
