import websockets
import asyncio
import requests
import json
from src.data_collectors.asset_pairs import AssetPairs
from colorama import init, Fore, Back, Style
import gzip

# Initializing Colorama
init(autoreset=True)

#TODO build on websocket logic
class Huobi(AssetPairs):
    def __init__(self, base_url, api_key, api_secret):
        super().__init__()
        self.base_url = base_url
        self.api_key = api_key
        self.api_secret = api_secret
        # self.coin_pairs = huobi_pair_format(self.huobi_pairs[0])
        # self.last_message = {pair: {'buy': None, 'sell': None} for pair in self.coin_pairs}
        self.connected = False

    async def listen_for_trades(self, ws_url, stream_index):
        while True:
            try:
                async with websockets.connect(ws_url) as websocket:
                    subscribe_message = {
                        "sub": "market.btcusdt.trade.detail",
                        "id": "id1"
                    }

                    # Send the subscription message
                    await websocket.send(json.dumps(subscribe_message))
                    print(Fore.BLUE + f"Subscribed to ticker updates for huobi: connection {stream_index}")
                    self.connected = True

                    # Listen for incoming ticker messages
                    while True:
                        message = await websocket.recv()
                        decompressed_data = gzip.decompress(message)
                        data = json.loads(decompressed_data)
                        print(Fore.CYAN + "huobi Market:", data)
                        if 'ping' in data:
                            pong = {
                                'pong': data['ping']
                            }
                            await websocket.send(json.dumps(pong))
                        elif 'ch' in data:
                            asset_pair = data['ch'].split('.')[1]

            except websockets.exceptions.ConnectionClosed:
                self.connected = False
                print(Fore.BLUE + "huobi connection closed, will attempt to reconnect in 10 seconds.")
                await asyncio.sleep(10)
            except Exception as e:
                self.connected = False
                print(Fore.RED + f"An error occurred: {e}")
                print(Fore.BLUE + "Attempting to reconnect in 10 seconds.")
                await asyncio.sleep(10)
