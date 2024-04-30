# src/main.py
import asyncio
from src.data_collectors.binance import Binance
from src.data_collectors.coinbase import Coinbase
from src.data_collectors.valr import Valr
from src.config import BINANCE_WEBSOCKET_URI

async def main():
    # Initialize exchange objects
    binance = Binance()
    # coinbase = Coinbase()
    # valr = Valr()

    # Run each exchange's listener concurrently
    await asyncio.gather(
        binance.listen_for_trades(BINANCE_WEBSOCKET_URI),
        # coinbase.listen_for_trades("TODO"),
        # valr.listen_for_trades("TODO")
    )

if __name__ == "__main__":
    asyncio.run(main())
