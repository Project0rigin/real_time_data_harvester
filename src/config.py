
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
UNSUPPORTED_TICKERS = [
    "ARPA-USDT",
    "GALA-USD",
    "ERN-USDT",
    "XCN-USDT",
    "POND-USDT",
    "PAX-USDT",
    "DYP-USDT",
    "BTRST-BTC",
    "DREP-USD",
    "UMA-GBP",
    "PERP-EUR",
    "BTRST-EUR",
    "YFII-USD",
    "RLY-EUR",
    "RAD-EUR",
    "WCFG-EUR",
    "POLY-USDT",
    "DAI-USDC",
    "JUP-USD",
    "METIS-USDT",
    "BAND-GBP",
    "PLA-USD",
    "BUSD-USD",
    "SHPING-EUR",
    "BNT-GBP",
    "UMA-EUR",
    "ELA-USDT",
    "FORT-USDT",
    "OOKI-USD",
    "KRL-USDT",
    "NU-USD",
    "TRU-USDT",
    "ATA-USDT",
    "MEDIA-USDT",
    "LQTY-EUR",
    "BNT-EUR",
    "KRL-EUR",
    "ASM-USDT",
    "ZRX-BTC",
    "GNO-USDT",
    "LCX-EUR",
    "HFT-USDT",
    "MIR-EUR",
    "GALA-EUR",
    "TRB-BTC",
    "LQTY-USDT",
    "POWR-EUR",
    "RLY-GBP",
    "XYO-USDT",
    "BAND-BTC",
    "QSP-USDT",
    "SHPING-USDT",
    "DESO-USDT",
    "NEST-USD",
    "BADGER-USDT",
    "MUSD-USD",
    "IDEX-USDT",
    "TRIBE-USD",
    "VGX-EUR",
    "CRPT-USD",
    "MIR-GBP",
    "ANT-USD",
    "CTX-EUR",
    "ZRX-EUR",
    "MONA-USD",
    "NMR-BTC",
    "RAD-GBP",
    "CLV-EUR",
    "LOOM-USDC",
    "NKN-GBP",
    "REQ-GBP",
    "XRP-GBP",
    "UST-EUR",
    "NU-BTC",
    "GAL-USDT",
    "FORTH-EUR",
    "MATH-USDT",
    "UPI-USD",
    "POLY-USD",
    "TRU-EUR"
]

# ----Kraken Base API settings----

# Websocket
KRAKEN_WEBSOCKET_URI = "wss://ws.kraken.com"
