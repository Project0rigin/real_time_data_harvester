from src.config import WANTED_TICKERS

def filter_pairs(pairs_array):
    # filter an array with tickers to keep
    return [item for item in pairs_array if item in WANTED_TICKERS]
