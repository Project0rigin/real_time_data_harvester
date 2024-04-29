import logging
import requests
import websocket
import json
import time

#TODO build on websocket logic
class Binance:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key

    async def listen_for_trades(self, ws_url):
        # Set up websocket connection
        ws = websocket.WebSocketApp(ws_url,
                                    on_open=self.on_open,
                                    on_message=self.on_message,
                                    on_error=self.on_error,
                                    on_close=self.on_close)
        ws.run_forever()
