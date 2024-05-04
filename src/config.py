
# Binance Base API settings
BASE_URL = "https://api.binance.com"

# Symbols
EXCHANGE_INFO_URL = "https://api.binance.com/api/v3/exchangeInfo"

COIN_DICT = {
    "coin_1": "btcusdt",
    "coin_2": "ethusdt",
    "coin_3": "bnbusdt",
    "coin_4": "adausdt",
    "coin_5": "xrpusdt",
    "coin_6": "dogeusdt",
    "coin_7": "dotusdt",
    "coin_8": "uniusdt",
    "coin_9": "linkusdt",
    "coin_10": "ltcusdt",
    "coin_11": "maticusdt",
    "coin_12": "solusdt",
    "coin_13": "vetusdt",
    "coin_14": "xemusdt",
    "coin_15": "trxusdt",
    "coin_16": "icpusdt",
    "coin_17": "chzusdt",
    "coin_18": "batusdt",
    "coin_19": "etcusdt",
    "coin_20": "ftmusdt",
    "coin_21": "thetausdt",
    "coin_22": "shibusdt",
    "coin_23": "xlmusdt",
    "coin_24": "dodgeusdt",
    "coin_25": "atomusdt",
    "coin_26": "filusdt",
    "coin_27": "aaveusdt",
    "coin_28": "ethbusdt",
    "coin_29": "yfiusdt",
    "coin_30": "enjusdt",
    "coin_31": "sushiusdt",
    "coin_32": "manausdt",
    "coin_33": "zilusdt",
    "coin_34": "iostusdt",
    "coin_35": "omgusdt",
    "coin_36": "renusdt",
    "coin_37": "batusdt",
    "coin_38": "ksmusdt",
    "coin_39": "ankrusdt",
    "coin_40": "iotxusdt",
    "coin_41": "ognusdt",
    "coin_42": "twtusdt",
    "coin_43": "chrusdt",
    "coin_44": "ltousdt",
    "coin_45": "srmusdt",
    "coin_46": "srmusdt",
    "coin_47": "srmusdt",
    "coin_48": "srmusdt",
    "coin_49": "srmusdt",
    "coin_50": "srmusdt",
    "coin_51": "srmusdt",
    "coin_52": "srmusdt",
}

COINS = list(COIN_DICT.values())



# Binance Market Data API settings
CHECK_SERVER_TIME_URL_ENDPOINT__MARKETDATA = "/api/v3/time"
EXCHANGE_INFO_URL_ENDPOINT__MARKETDATA = "/api/v3/exchangeInfo"
ACCOUNT_URL_ENDPOINT__MARKETDATA = "/api/v3/account"
SYMBOL_PRICE_TICKER_URL_ENDPOINT__MARKETDATA = "/api/v3/ticker/price"

# Binance Websocket API settings
BINANCE_WEBSOCKET_URI = "wss://stream.binance.com:9443/stream?streams="
WS_TICKER_URL_ENDPOINT = "/btcusdt@ticker"
