import requests
from src.config import EXCHANGE_INFO_URL, COINBASE_PRODUCTS_URL_ENDPOINT

class AssetPairs:
    def __init__(self):
        self.pairs = self._get_pairs()

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
            print(f"First third: {first_third}")
            return [asset_pairs, first_third, second_third, third_third]
        except requests.RequestException as e:
            print(f"Failed to retrieve pairs: {e}")
            return []

    def _get_pairs_coinbase(self):
        url = COINBASE_PRODUCTS_URL_ENDPOINT
        response = requests.get(url)
        if response.status_code == 200:
            products = response.json()
            for product in products:
                print(f"ID: {product['id']}, Base: {product['base_currency']}, Quote: {product['quote_currency']}")
        else:
            print("Failed to fetch products", response.status_code)
