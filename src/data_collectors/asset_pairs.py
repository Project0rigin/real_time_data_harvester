import requests
from src.config import EXCHANGE_INFO_URL, COINBASE_PRODUCTS_URL_ENDPOINT
from src.utils.coinbase_pair_formatter import remove_tickers
class AssetPairs:
    def __init__(self):
        self.pairs = self._get_pairs()
        self.coinbase_pairs = self._get_pairs_coinbase()

    def _get_pairs(self):
        try:
            response = requests.get(EXCHANGE_INFO_URL)
            response.raise_for_status()
            data = response.json()
            asset_pairs = []
            for symbol_data in data["symbols"]:
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
            print(f"Failed to retrieve pairs: {e}")
            return []

    def _get_pairs_coinbase(self):
        try:
            response = requests.get(COINBASE_PRODUCTS_URL_ENDPOINT)
            products = response.json()
            unfiltered_asset_pairs = []
            for product in products:
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
            print("Failed to fetch products", response.status_code)
            return []
