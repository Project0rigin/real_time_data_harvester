import requests

class AssetPairs:
    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.pairs = self._get_pairs()

    def _get_pairs(self):
        try:
            response = requests.get(self.endpoint)
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
            return [first_third, second_third, third_third]
        except requests.RequestException as e:
            print(f"Failed to retrieve pairs: {e}")
            return []
