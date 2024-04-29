# src/main.py
import asyncio
from src.data_collectors.binance import Binance
from src.data_collectors.coinbase import Coinbase
from src.data_collectors.valr import Valr
from src.config import BINANCE_WEBSOCKET_URI

async def main():
    # Initialize exchange objects
    binance = Binance()
    coinbase = Coinbase()
    valr = Valr()

    # Run each exchange's listener concurrently
    await asyncio.gather(
        binance.listen_for_trades(BINANCE_WEBSOCKET_URI),
        coinbase.listen_for_trades("TODO"),
        valr.listen_for_trades("TODO")
    )

if __name__ == "__main__":
    asyncio.run(main())

# TODO set own API key and move to relevant exchange instances (get api key etc from Jack)
# def on_message(ws, message):
#     message = json.loads(message)
#     print("Received message: ", message)

# def on_error(ws, error):
#     print("Error: ", error)

# def on_close(ws):
#     print("### closed ###")

# def on_open(ws):
#     def run(*args):
#         ws.send(json.dumps({'method': 'SUBSCRIBE', 'params': ['btcusdt@ticker'], 'id': 1}))
#     return run

# if __name__ == "__main__":
#     while True:
#         websocket.enableTrace(True)
#         ws = websocket.WebSocketApp("wss://stream.binance.com:9443/ws/btcusdt@ticker",
#                                     on_open=on_open,
#                                     on_message=on_message,
#                                     on_error=on_error,
#                                     on_close=on_close)
#         ws.run_forever()
#         print("Reconnecting...")
#         # Sleep for 10 seconds before reconnecting after websocket disconnected
#         time.sleep(10)
