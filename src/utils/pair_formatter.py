from src.config import UNSUPPORTED_TICKERS

def coinbase_pair_format(pairs_array):
    return [pair.replace('-', '').lower() for pair in pairs_array]

def remove_tickers(pairs_array):
    filtered_list = [item for item in pairs_array if item not in UNSUPPORTED_TICKERS]
    return filtered_list

def convert_kraken_pair(pairs_array):
    return [pair.replace('/', '').lower() for pair in pairs_array]
