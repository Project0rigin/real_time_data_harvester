
# ----Binance Base API settings----
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

# ----Coinbase Base API settings----

# Websocket
COINBASE_WEBSOCKET_URI = "wss://ws-feed.exchange.coinbase.com"

# Get Request
COINBASE_PRODUCTS_URL_ENDPOINT = "https://api.pro.coinbase.com/products"

# Extra Global variables
UNSUPPORTED_TICKERS = ["ARPA-USDT", "GALA-USD"] # Add any unsupported tickers here

# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"ERN-USDT is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"XCN-USDT is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"POND-USDT is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"PAX-USDT is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"DYP-USDT is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"BTRST-BTC is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"DREP-USD is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"UMA-GBP is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"PERP-EUR is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"BTRST-EUR is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"YFII-USD is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"RLY-EUR is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"RAD-EUR is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"WCFG-EUR is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"POLY-USDT is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"DAI-USDC is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"JUP-USD is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"METIS-USDT is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"BAND-GBP is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"PLA-USD is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"BUSD-USD is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"SHPING-EUR is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"BNT-GBP is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"UMA-EUR is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"ELA-USDT is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"FORT-USDT is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"OOKI-USD is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"KRL-USDT is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"NU-USD is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"TRU-USDT is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"ATA-USDT is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"MEDIA-USDT is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"LQTY-EUR is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"BNT-EUR is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"KRL-EUR is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"ASM-USDT is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"ZRX-BTC is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"GNO-USDT is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"LCX-EUR is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"HFT-USDT is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"MIR-EUR is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"GALA-EUR is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"TRB-BTC is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"LQTY-USDT is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"POWR-EUR is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"RLY-GBP is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"XYO-USDT is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"BAND-BTC is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"QSP-USDT is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"SHPING-USDT is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"DESO-USDT is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"NEST-USD is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"BADGER-USDT is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"MUSD-USD is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"IDEX-USDT is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"TRIBE-USD is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"VGX-EUR is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"CRPT-USD is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"MIR-GBP is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"ANT-USD is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"CTX-EUR is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"ZRX-EUR is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"MONA-USD is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"NMR-BTC is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"RAD-GBP is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"CLV-EUR is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"LOOM-USDC is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"NKN-GBP is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"REQ-GBP is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"XRP-GBP is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"UST-EUR is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"NU-BTC is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"GAL-USDT is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"FORTH-EUR is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"MATH-USDT is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"UPI-USD is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"POLY-USD is delisted"}
# Received ticker message: {"type":"error","message":"Failed to subscribe","reason":"TRU-EUR is delisted"}
