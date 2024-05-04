def coinbase_pair_format(pairs_array):
    return [pair.replace('-', '').lower() for pair in pairs_array]
