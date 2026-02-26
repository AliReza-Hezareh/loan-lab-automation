import requests
import os


class ApiClient:
    def __init__(self, base_url, api_key=None):
        self.base_url = base_url
        self.headers ={
            "Authorization": f"Bearer {api_key}"} if api_key else {}
        