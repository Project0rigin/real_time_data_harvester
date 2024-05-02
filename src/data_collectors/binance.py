import websockets
import asyncio
import requests
import logging

#TODO build on websocket logic
class Binance:
    def __init__(self, base_url, api_key, api_secret, asset_pairs):
        self.base_url = base_url
        self.api_key = api_key
        self.asset_pairs = asset_pairs

    async def listen_for_trades(self, ws_url):
        async with websockets.connect(f"{ws_url}{self.asset_pairs[0]}@trade") as websocket:
            while True:
                message = await websocket.recv()
                print("Received message:", message)

    def get_current_price(self, symbol_price_ticker_endpoint):
        print(f"Retrieving current price for {self.asset_pairs[0]}")
        try:
            response = requests.get(
                f"{self.base_url}{symbol_price_ticker_endpoint}?symbol={self.asset_pairs[0].upper()}",
                headers={"X-MBX-APIKEY": self.api_key},
            )
            response.raise_for_status()
            price = response.json()["price"]
            print(f"Current price for {self.asset_pairs[0]}: {price}")
            return price
        except requests.RequestException as e:
            print(f"Error retrieving current price for {self.asset_pairs[0]}: {str(e)}")
            return None
