# testing the valr api with websockets
import asyncio
import websockets
import json
import hmac
import hashlib
import time

api_key = ''
api_secret = ''

def get_auth_headers():
    timestamp = str(int(time.time() * 1000))
    method = 'GET'
    path = '/ws/trade'
    body = ''

    # Create the prehash string
    prehash = timestamp + method.upper() + path + body
    # Create the HMAC SHA512 signature
    signature = hmac.new(bytes(api_secret, 'utf-8'), bytes(prehash, 'utf-8'), hashlib.sha512).hexdigest()

    return {
        'X-VALR-API-KEY': api_key,
        'X-VALR-SIGNATURE': signature,
        'X-VALR-TIMESTAMP': timestamp
    }

async def connect_to_valr():
    url = "wss://api.valr.com/ws/trade"
    headers = get_auth_headers()

    async with websockets.connect(url, extra_headers=headers) as websocket:
        # Subscribe to the NEW_TRADE stream
        subscribe_message = {
            "type": "SUBSCRIBE",
            "subscriptions": [{"event": "NEW_TRADE", "pairs": ["BTCUSDT"]}]
        }
        await websocket.send(json.dumps(subscribe_message))

        try:
            while True:
                message = await websocket.recv()
                print("Received message:", message)
        except websockets.exceptions.ConnectionClosed:
            print("Connection closed, attempting to reconnect")
            await connect_to_valr()  # Reconnect

# Run the connection in an asyncio event loop
asyncio.run(connect_to_valr())
