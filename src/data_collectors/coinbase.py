import logging
import requests
import websocket
import json
import time

#TODO change to websocket logic
class Coinbase:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key
