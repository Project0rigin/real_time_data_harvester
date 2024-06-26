# src/main.py
import asyncio
from fastapi import FastAPI
from src.data_collectors.binance import Binance
from src.data_collectors.coinbase import Coinbase
from src.data_collectors.kraken import Kraken
from src.data_collectors.huobi import Huobi
from src.config import BINANCE_WEBSOCKET_URI, COINBASE_WEBSOCKET_URI, COINS, SYMBOL_PRICE_TICKER_URL_ENDPOINT__MARKETDATA, BASE_URL, EXCHANGE_INFO_URL, KRAKEN_WEBSOCKET_URI
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
kraken = Kraken(base_url, binance_api_key, binance_api_secret)
huobi = Huobi(base_url, binance_api_key, binance_api_secret)

@app.get("/latest_trades")
async def get_latest_trades():
    if binance.last_message:
        return {
            "binance": {
                "connected": binance.connected,
                "prices": binance.last_message,
                "shared_coinbase": binance.shared_with_coinbase
                },
            "coinbase": {
                "connected": coinbase.connected,
                "prices": coinbase.last_message,
                "shared_binance": coinbase.shared_with_binance
                },
            "kraken": {
                "connected": kraken.connected,
                "prices": kraken.last_message,
                }
            }
    else:
        return {"error": "No data available"}

async def start_binance_listener():
    tasks = []
    for index in range(3):
        task = asyncio.create_task(binance.listen_for_trades(BINANCE_WEBSOCKET_URI, index + 1))
        tasks.append(task)
    await asyncio.gather(*tasks)

async def start_kraken_listener():
    tasks = []
    for index in range(3):
        task = asyncio.create_task(kraken.listen_for_trades(KRAKEN_WEBSOCKET_URI, index + 1))
        tasks.append(task)
    return asyncio.gather(*tasks)

async def start_coinbase_listener():
    tasks = []
    for index in range(3):
        task = asyncio.create_task(coinbase.listen_for_trades(COINBASE_WEBSOCKET_URI, index + 1))
        tasks.append(task)
    return asyncio.gather(*tasks)

async def start_huobi_listener():
    task = asyncio.create_task(huobi.listen_for_trades("wss://api.huobi.pro/ws", 1))
    return task

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(start_binance_listener())
    asyncio.create_task(start_coinbase_listener())
    asyncio.create_task(start_kraken_listener())
    asyncio.create_task(start_huobi_listener())

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
