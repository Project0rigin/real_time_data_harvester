from src.config import UNSUPPORTED_TICKERS

def coinbase_pair_format(pairs_array):
    return [pair.replace('-', '').lower() for pair in pairs_array]

def remove_tickers(pairs_array):
    filtered_list = [item for item in pairs_array if item not in UNSUPPORTED_TICKERS]
    return filtered_list

# array = ["BTC-USD", "ETH-USD", "LTC-USD", "ANKR-USD", "XRP-USD"]
# tickers = ["ANKR-USD", "XRP-USD"]
# print(remove_tickers(array, tickers))
