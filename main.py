# src/main.py
import asyncio
from fastapi import FastAPI
from src.data_collectors.binance import Binance
from src.data_collectors.coinbase import Coinbase
from src.config import BINANCE_WEBSOCKET_URI, COINBASE_WEBSOCKET_URI, COINS, SYMBOL_PRICE_TICKER_URL_ENDPOINT__MARKETDATA, BASE_URL, EXCHANGE_INFO_URL
from dotenv import load_dotenv
import os
import uvicorn

load_dotenv()

app = FastAPI()

binance_api_key = os.getenv("BINANCE_API_KEY")
binance_api_secret = os.getenv("BINANCE_API_SECRET")
symbol_price_ticker_endpoint = SYMBOL_PRICE_TICKER_URL_ENDPOINT__MARKETDATA
base_url = BASE_URL

binance = Binance(base_url, binance_api_key, binance_api_secret)
coinbase = Coinbase(base_url, binance_api_key, binance_api_secret)

@app.get("/latest_trades")
async def get_latest_trades():
    if binance.last_message:
        return {
            "connected": True,
            "binance": {"prices": binance.last_message},
            "coinbase": {"prices": coinbase.last_message}
            }
    else:
        return {"error": "No data available"}

async def start_binance_listener():
    tasks = []
    for index in range(3):
        task = asyncio.create_task(binance.listen_for_trades(BINANCE_WEBSOCKET_URI, index + 1))
        tasks.append(task)
    await asyncio.gather(*tasks)

async def start_valr_listener():
    task = ... # asyncio.create_task(valr.listen_for_trades(VALR_WEBSOCKET_URI, 0))
    return task

async def start_coinbase_listener():
    tasks = []
    for index in range(3):
        task = asyncio.create_task(coinbase.listen_for_trades(COINBASE_WEBSOCKET_URI, index + 1))
        tasks.append(task)
    return asyncio.gather(*tasks)

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(start_binance_listener())
    asyncio.create_task(start_coinbase_listener())
    # asyncio.create_task(start_valr_listener())

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
