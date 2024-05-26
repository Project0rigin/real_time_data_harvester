from .data_readers.asset_pairs import read_asset_pairs
# General settings
WANTED_TICKERS = [x.lower() for x in read_asset_pairs()]

# ----Binance Base API settings----
BASE_URL = "https://api.binance.com"

# Symbols
EXCHANGE_INFO_URL = "https://api.binance.com/api/v3/exchangeInfo"

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

# Get Request
KRAKEN_PRODUCTS_URL_ENDPOINT = "https://api.kraken.com/0/public/AssetPairs"
