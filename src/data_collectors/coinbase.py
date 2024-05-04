import websockets
import asyncio
import requests
import json
from src.utils.trade_name_concat import concat_trade_name
from src.data_collectors.asset_pairs import AssetPairs
from src.config import EXCHANGE_INFO_URL

#TODO build on websocket logic
class Valr(AssetPairs):
    def __init__(self, base_url, api_key, api_secret):
        super().__init__(EXCHANGE_INFO_URL)
        self.base_url = base_url
        self.api_key = api_key
        self.api_secret = api_secret
        self.last_message = {pair: {'buy': None, 'sell': None} for pair in self.pairs[0]}

    async def listen_for_trades(self, ws_url, stream_index):
        # todo establish websocket connection
        return None
