def concat_trade_name(coins):
    trade_name = ""
    for coin in coins:
        trade_name = f"{trade_name}/{coin}@trade"
    return trade_name[1:]
