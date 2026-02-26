import requests
import os


class ApiClient:
    def __init__(self, base_url, api_key=None):
        self.base_url = base_url
        self.headers ={
            "Authorization": f"Bearer {api_key}"
            } if api_key else {}
        
    def get_products(self):
        return requests.get(f"{self.base_url}/products", headers=self.headers)

    def create_application(self, payload):
        return requests.post(
            f"{self.base_url}/applications", 
            json=payload, 
            headers=self.headers
            )