import websockets
import asyncio
import requests
import json
from src.utils.trade_name_concat import concat_trade_name

#TODO build on websocket logic
class Binance:
    def __init__(self, base_url, api_key, api_secret, asset_pairs):
        self.base_url = base_url
        self.api_key = api_key
        self.asset_pairs = asset_pairs
        self.last_message = {pair: None for pair in asset_pairs}

    async def listen_for_trades(self, ws_url):
        async with websockets.connect(f"{ws_url}{concat_trade_name(self.asset_pairs)}") as websocket:
            while True:
                message = await websocket.recv()
                data = json.loads(message)
                print("Received message:", message)
                if 'stream' in data:
                    asset_pair = data['stream'].split('@')[0]
                    price = data['data']['p'] if 'p' in data['data'] else None
                    if asset_pair in self.last_message:
                        self.last_message[asset_pair] = price
                    else:
                        print(f"Received message for unknown asset pair: {asset_pair}")
