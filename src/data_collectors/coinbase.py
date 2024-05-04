import websockets
import asyncio
import requests
import json
from src.utils.trade_name_concat import concat_trade_name
from src.data_collectors.asset_pairs import AssetPairs

#TODO build on websocket logic
class Coinbase(AssetPairs):
    def __init__(self, base_url, api_key, api_secret):
        super().__init__()
        self.base_url = base_url
        self.api_key = api_key
        self.api_secret = api_secret
        self.last_message = {pair: {'buy': None, 'sell': None} for pair in self.pairs[0]}

    async def listen_for_trades(self, ws_url, stream_index):
        async with websockets.connect(ws_url) as websocket:
        # Prepare the subscription message according to Coinbase API specifications
            subscribe_message = {
                "type": "subscribe",
                "product_ids": ["ETH-USD", "BTC-USD"],
                "channels": ["ticker"]
            }

            # Send the subscription message
            await websocket.send(json.dumps(subscribe_message))
            print("Subscribed to ticker updates for ETH-USD and BTC-USD")

            # Listen for incoming ticker messages
            while True:
                message = await websocket.recv()
                message = json.loads(message)
                print("Received ticker message:", message)
