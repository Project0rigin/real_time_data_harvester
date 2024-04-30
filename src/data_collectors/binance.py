import websockets
import asyncio

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

# /{self.asset_pairs[1]}@trade