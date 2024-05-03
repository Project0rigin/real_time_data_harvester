import websockets
import asyncio
import requests
import json
from src.utils.trade_name_concat import concat_trade_name
from src.data_collectors.asset_pairs import AssetPairs
from src.config import EXCHANGE_INFO_URL

#TODO build on websocket logic
class Binance(AssetPairs):
    def __init__(self, base_url, api_key, api_secret, asset_pairs):
        super().__init__(EXCHANGE_INFO_URL)
        self.base_url = base_url
        self.api_key = api_key
        self.api_secret = api_secret
        self.asset_pairs = asset_pairs
        self.last_message = {pair: {'buy': None, 'sell': None} for pair in self.asset_pairs}

    async def listen_for_trades(self, ws_url):
        async with websockets.connect(f"{ws_url}{concat_trade_name(self.pairs[0])}") as websocket:
            while True:
                message = await websocket.recv()
                data = json.loads(message)
                print("Received message:", message)
                if 'stream' in data:
                    asset_pair = data['stream'].split('@')[0]
                    price = data['data']['p'] if 'p' in data['data'] else None
                    is_buyer_maker = data['data'].get('m', None)
                    if asset_pair in self.last_message:
                        if is_buyer_maker is not None:
                            if not is_buyer_maker:  # Buyer is taker, it's a buy
                                self.last_message[asset_pair]['buy'] = price
                            else:  # Buyer is maker, it's a sell
                                self.last_message[asset_pair]['sell'] = price
                    else:
                        print(f"Received message for unknown asset pair: {asset_pair}")
