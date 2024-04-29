import websocket
import json
import time

# TODO change this to own API key and move to more relevant directory
def on_message(ws, message):
    message = json.loads(message)
    print("Received message: ", message)

def on_error(ws, error):
    print("Error: ", error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        ws.send(json.dumps({'method': 'SUBSCRIBE', 'params': ['btcusdt@ticker'], 'id': 1}))
    return run

if __name__ == "__main__":
    while True:
        websocket.enableTrace(True)
        ws = websocket.WebSocketApp("wss://stream.binance.com:9443/ws/btcusdt@ticker",
                                    on_open=on_open,
                                    on_message=on_message,
                                    on_error=on_error,
                                    on_close=on_close)
        ws.run_forever()
        print("Reconnecting...")
        # Sleep for 10 seconds before reconnecting after websocket disconnected
        time.sleep(10)
