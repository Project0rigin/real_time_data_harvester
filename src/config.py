# Symbols
COIN_1 = "btcusdt"
COIN_2 = "ethusdt"
COIN_3 = "bnbusdt"
COIN_4 = "adausdt"
COIN_5 = "xrpusdt"
COIN_6 = "dogeusdt"
COIN_7 = "dotusdt"
COIN_8 = "uniusdt"
COIN_9 = "linkusdt"
COIN_10 = "ltcusdt"

COINS = [COIN_1, COIN_2, COIN_3, COIN_4, COIN_5, COIN_6, COIN_7, COIN_8, COIN_9, COIN_10]

# Binance Base API settings
BASE_URL = "https://api.binance.com"

# Binance Market Data API settings
CHECK_SERVER_TIME_URL_ENDPOINT__MARKETDATA = "/api/v3/time"
EXCHANGE_INFO_URL_ENDPOINT__MARKETDATA = "/api/v3/exchangeInfo"
ACCOUNT_URL_ENDPOINT__MARKETDATA = "/api/v3/account"
SYMBOL_PRICE_TICKER_URL_ENDPOINT__MARKETDATA = "/api/v3/ticker/price"

# Binance Websocket API settings
BINANCE_WEBSOCKET_URI = "wss://stream.binance.com:9443/stream?streams="
WS_TICKER_URL_ENDPOINT = "/btcusdt@ticker"
