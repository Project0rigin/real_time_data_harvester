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
            return data.get('pairs', [])
        except requests.RequestException as e:
            print(f"Failed to retrieve pairs: {e}")
            return []
