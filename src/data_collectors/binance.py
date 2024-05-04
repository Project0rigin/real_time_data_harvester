import websockets
import asyncio
import requests
import json
from src.utils.trade_name_concat import concat_trade_name
from src.data_collectors.asset_pairs import AssetPairs
from colorama import init, Fore, Back, Style

# Initializing Colorama
init(autoreset=True)

#TODO build on websocket logic
class Binance(AssetPairs):
    def __init__(self, base_url, api_key, api_secret):
        super().__init__()
        self.base_url = base_url
        self.api_key = api_key
        self.api_secret = api_secret
        self.last_message = {pair: {'buy': None, 'sell': None} for pair in self.pairs[0]}
        self.connected = False

    async def listen_for_trades(self, ws_url, stream_index):
        while True:
            try:
                async with websockets.connect(f"{ws_url}{concat_trade_name(self.pairs[stream_index])}") as websocket:
                    self.connected = True
                    while True:
                        message = await websocket.recv()
                        data = json.loads(message)
                        print(Fore.YELLOW + "Binance Market:", message)
                        if 'stream' in data:
                            asset_pair = data['stream'].split('@')[0]
                            price = data['data']['p'] if 'p' in data['data'] else None
                            is_buyer_maker = data['data'].get('m', None)
                            if asset_pair in self.last_message:
                                if is_buyer_maker is not None:
                                    if not is_buyer_maker:
                                        self.last_message[asset_pair]['buy'] = price
                                    else:
                                        self.last_message[asset_pair]['sell'] = price
                            else:
                                print(f"Received message for unknown asset pair: {asset_pair}")

            except websockets.exceptions.ConnectionClosed:
                self.connected = False
                print(Fore.YELLOW + "Binance connection closed, will attempt to reconnect in 10 seconds.")
                await asyncio.sleep(10)
            except Exception as e:
                self.connected = False
                print(Fore.RED + f"An error occurred: {e}")
                print(Fore.YELLOW + "Attempting to reconnect in 10 seconds.")
                await asyncio.sleep(10)
