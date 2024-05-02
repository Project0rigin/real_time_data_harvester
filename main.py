# src/main.py
import asyncio
from fastapi import FastAPI
import uvicorn
from src.data_collectors.binance import Binance
# from src.data_collectors.coinbase import Coinbase
# from src.data_collectors.valr import Valr
from src.config import BINANCE_WEBSOCKET_URI
from src.config import COINS
from src.config import SYMBOL_PRICE_TICKER_URL_ENDPOINT__MARKETDATA
from src.config import BASE_URL

from dotenv import load_dotenv
import os

load_dotenv()

binance_api_key = os.getenv("BINANCE_API_KEY")
binance_api_secret = os.getenv("BINANCE_API_SECRET")
asset_pairs = COINS
symbol_price_ticker_endpoint = SYMBOL_PRICE_TICKER_URL_ENDPOINT__MARKETDATA
base_url = BASE_URL

binance = Binance(base_url, binance_api_key, binance_api_secret, asset_pairs)

async def main():
    # Initialize exchange objects
    binance.get_current_price(symbol_price_ticker_endpoint)
    # coinbase = Coinbase()
    # valr = Valr()

    await asyncio.gather(
        binance.listen_for_trades(BINANCE_WEBSOCKET_URI),
        # coinbase.listen_for_trades("TODO"),
        # valr.listen_for_trades("TODO")
    )

if __name__ == "__main__":
    asyncio.run(main())
