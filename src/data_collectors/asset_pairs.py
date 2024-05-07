import requests
from src.config import EXCHANGE_INFO_URL, COINBASE_PRODUCTS_URL_ENDPOINT, KRAKEN_PRODUCTS_URL_ENDPOINT, WANTED_TICKERS
from src.utils.pair_formatter import remove_tickers, coinbase_pair_format
from src.utils.pair_filter import filter_pairs

class AssetPairs:
    def __init__(self):
        self.pairs = self._get_pairs()
        self.coinbase_pairs = self._get_pairs_coinbase()
        self.kraken_pairs = self._get_pairs_kraken()

    def shared_pairs_binance_coinbase(self):
        set_binance_pairs = set(self.pairs[0])
        set_coinbase_pairs = set(coinbase_pair_format(self.coinbase_pairs[0]))
        common_pairs = set_binance_pairs.intersection(set_coinbase_pairs)
        return list(common_pairs)

    def _get_pairs(self):
        try:
            response = requests.get(EXCHANGE_INFO_URL)
            response.raise_for_status()
            data = response.json()
            asset_pairs = []
            for symbol_data in data["symbols"]:
                formatted_pair = symbol_data["symbol"].lower()
                if formatted_pair in WANTED_TICKERS:
                    asset_pairs.append(symbol_data["symbol"].lower())
            part_size = len(asset_pairs) // 3
            remainder = len(asset_pairs) % 3
            end1 = part_size + (1 if remainder > 0 else 0)
            end2 = end1 + part_size + (1 if remainder > 1 else 0)

            first_third = asset_pairs[:end1]
            second_third = asset_pairs[end1:end2]
            third_third = asset_pairs[end2:]
            return [asset_pairs, first_third, second_third, third_third]
        except requests.RequestException as e:
            print(f"Failed to fetch binance pairs: {e}")
            return []

    def _get_pairs_coinbase(self):
        try:
            response = requests.get(COINBASE_PRODUCTS_URL_ENDPOINT)
            products = response.json()
            unfiltered_asset_pairs = []
            for product in products:
                formatted_pair = product['id'].replace('-', '').lower()
                if formatted_pair in WANTED_TICKERS:
                    unfiltered_asset_pairs.append(product['id'])

            filtered_asset_pairs = remove_tickers(unfiltered_asset_pairs)
            part_size = len(filtered_asset_pairs) // 3
            remainder = len(filtered_asset_pairs) % 3
            end1 = part_size + (1 if remainder > 0 else 0)
            end2 = end1 + part_size + (1 if remainder > 1 else 0)

            first_third = filtered_asset_pairs[:end1]
            second_third = filtered_asset_pairs[end1:end2]
            third_third = filtered_asset_pairs[end2:]
            # print(filtered_asset_pairs)
            return [filtered_asset_pairs, first_third, second_third, third_third]
        except requests.RequestException as e:
            print(f"Failed to fetch coinbase pairs: {e}")
            return []

    def _get_pairs_kraken(self):
        try:
            response = requests.get(KRAKEN_PRODUCTS_URL_ENDPOINT)
            data = response.json()
            asset_pairs = []
            if not data['error']:
                products = data['result']
                for key, value in products.items():
                    unfiltered_pair = value['wsname'].replace('/', '').lower()
                    if unfiltered_pair in WANTED_TICKERS:
                        asset_pairs.append(value['wsname'])

                part_size = len(asset_pairs) // 3
                remainder = len(asset_pairs) % 3
                end1 = part_size + (1 if remainder > 0 else 0)
                end2 = end1 + part_size + (1 if remainder > 1 else 0)

                first_third = asset_pairs[:end1]
                second_third = asset_pairs[end1:end2]
                third_third = asset_pairs[end2:]
                return [asset_pairs, first_third, second_third, third_third]
        except requests.RequestException as e:
            print(f"Failed to retrieve kraken pairs: {e}")
            return []
