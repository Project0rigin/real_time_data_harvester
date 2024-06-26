import websockets
import asyncio
import requests
import json
from src.utils.pair_formatter import coinbase_pair_format
from src.data_collectors.asset_pairs import AssetPairs
from colorama import init, Fore, Back, Style

# Initializing Colorama
init(autoreset=True)

#TODO build on websocket logic
class Coinbase(AssetPairs):
    def __init__(self, base_url, api_key, api_secret):
        super().__init__()
        self.base_url = base_url
        self.api_key = api_key
        self.api_secret = api_secret
        self.coin_pairs = coinbase_pair_format(self.coinbase_pairs[0])
        self.last_message = {pair: {'buy': None, 'sell': None} for pair in self.coin_pairs}
        self.connected = False
        self.shared_with_binance = self.shared_pairs_binance_coinbase()

    async def listen_for_trades(self, ws_url, stream_index):
        while True:
            try:
                async with websockets.connect(ws_url) as websocket:
                    subscribe_message = {
                        "type": "subscribe",
                        "product_ids": self.coinbase_pairs[stream_index],
                        "channels": ["ticker"]
                    }

                    # Send the subscription message
                    await websocket.send(json.dumps(subscribe_message))
                    print(Fore.BLUE + f"Subscribed to ticker updates for Coinbase: connection {stream_index}")
                    self.connected = True

                    # Listen for incoming ticker messages
                    while True:
                        message = await websocket.recv()
                        data = json.loads(message)
                        print(Fore.BLUE + "Coinbase Market:", message)
                        if 'product_id' in data:
                            asset_pair = data['product_id'].replace('-', '').lower()
                            price = data['price']
                            side = data.get('side', None)
                            if asset_pair in self.last_message:
                                if side == 'buy':
                                    self.last_message[asset_pair]['buy'] = price
                                elif side == 'sell':
                                    self.last_message[asset_pair]['sell'] = price
                            else:
                                print(f"Received message for unknown asset pair: {asset_pair}")

            except websockets.exceptions.ConnectionClosed:
                self.connected = False
                print(Fore.BLUE + "Coinbase connection closed, will attempt to reconnect in 10 seconds.")
                await asyncio.sleep(10)
            except Exception as e:
                self.connected = False
                print(Fore.RED + f"An error occurred: {e}")
                print(Fore.BLUE + "Attempting to reconnect in 10 seconds.")
                await asyncio.sleep(10)
