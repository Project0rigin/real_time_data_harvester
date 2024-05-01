# src/main.py
import asyncio
from src.data_collectors.binance import Binance
# from src.data_collectors.coinbase import Coinbase
# from src.data_collectors.valr import Valr
from src.config import BINANCE_WEBSOCKET_URI
from src.config import COINS
from src.config import SYMBOL_PRICE_TICKER_URL_ENDPOINT__MARKETDATA

from dotenv import load_dotenv
import os

load_dotenv()

binance_api_key = os.getenv("BINANCE_API_KEY")
binance_api_secret = os.getenv("BINANCE_API_SECRET")
asset_pairs = COINS
symbol_price_ticker_endpoint = SYMBOL_PRICE_TICKER_URL_ENDPOINT__MARKETDATA

async def main():
    # Initialize exchange objects
    binance = Binance(binance_api_key, binance_api_secret, asset_pairs)
    # coinbase = Coinbase()
    # valr = Valr()

    # Run each exchange's listener concurrently
    await asyncio.gather(
        binance.listen_for_trades(BINANCE_WEBSOCKET_URI),
        # coinbase.listen_for_trades("TODO"),
        # valr.listen_for_trades("TODO")
    )

# binance.get_price('BTC', symbol_price_ticker_endpoint)

if __name__ == "__main__":
    asyncio.run(main())
