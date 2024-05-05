import websockets
import asyncio
import requests
import json
from src.data_collectors.asset_pairs import AssetPairs
from src.utils.pair_formatter import convert_kraken_pair
from colorama import init, Fore, Back, Style

# Initializing Colorama
init(autoreset=True)

class Kraken(AssetPairs):
    def __init__(self, base_url, api_key, api_secret):
        super().__init__()
        self.base_url = base_url
        self.api_key = api_key
        self.api_secret = api_secret
        self.coin_pairs = convert_kraken_pair(self.kraken_pairs[0])
        self.last_message = {pair: {'buy': None, 'sell': None} for pair in self.coin_pairs}
        self.connected = False

    async def listen_for_trades(self, ws_url, stream_index):
        while True:
            try:
                async with websockets.connect(ws_url) as websocket:
                    subscribe_message = {
                        "event": "subscribe",
                        "pair": self.kraken_pairs[stream_index],
                        "subscription": {
                            "name": "trade"
                        }
                    }

                    # Send the subscription message
                    await websocket.send(json.dumps(subscribe_message))
                    print("Subscribed to ticker updates for Kraken.")
                    self.connected = True

                    # Listen for incoming ticker messages
                    while True:
                        message = await websocket.recv()
                        data = json.loads(message)
                        if 'trade' in data:
                            # print(Fore.GREEN + "Kraken Market:", message)
                            asset_pair = data[-1].replace('/', '').lower()
                            trades = data[1]
                            for trade in trades:
                                price = trade[0]
                                side = trade[3]
                                if asset_pair in self.last_message:
                                    if side == 'b':
                                        self.last_message[asset_pair]['buy'] = price
                                    elif side == 's':
                                        self.last_message[asset_pair]['sell'] = price
                                else:
                                    print(f"Received message for unknown asset pair: {asset_pair}")

            except websockets.exceptions.ConnectionClosed:
                self.connected = False
                print(Fore.GREEN + "Kraken connection closed, will attempt to reconnect in 10 seconds.")
                await asyncio.sleep(10)
            except Exception as e:
                self.connected = False
                print(Fore.RED + f"An error occurred: {e}")
                print(Fore.GREEN + "Attempting to reconnect in 10 seconds.")
                await asyncio.sleep(10)
