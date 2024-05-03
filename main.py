# src/main.py
import asyncio
from fastapi import FastAPI
from src.data_collectors.binance import Binance
from src.data_collectors.asset_pairs import AssetPairs
from src.config import BINANCE_WEBSOCKET_URI, COINS, SYMBOL_PRICE_TICKER_URL_ENDPOINT__MARKETDATA, BASE_URL, EXCHANGE_INFO_URL
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

binance_api_key = os.getenv("BINANCE_API_KEY")
binance_api_secret = os.getenv("BINANCE_API_SECRET")
asset_pairs = COINS
symbol_price_ticker_endpoint = SYMBOL_PRICE_TICKER_URL_ENDPOINT__MARKETDATA
base_url = BASE_URL

# asset_pair_collector = AssetPairs(EXCHANGE_INFO_URL)
binance = Binance(base_url, binance_api_key, binance_api_secret, asset_pairs)

@app.get("/latest_trades")
async def get_latest_trades():
    return {"data": binance.last_message} if binance.last_message else {"error": "No data available"}

async def start_binance_listener():
    await binance.listen_for_trades(BINANCE_WEBSOCKET_URI)

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(start_binance_listener())

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
