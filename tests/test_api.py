import requests
from src.config import API_KEY, BASE_URL

BASE_URL = "https://kzmcpfklrqymzazaxlmv.supabase.co/functions/v1/partner-loan-api"

def test_get_health_status():
    
    headers = {
        "x-api-key": API_KEY
    }
    response = requests.get(f"{BASE_URL}/health" , headers=headers)
    assert "application/json" in response.headers["Content-Type"]
    
    
    in_the_data = response.json()
    
    assert response.status_code == 200
    assert in_the_data["success"] == True
    assert "application/json" in response.headers["Content-Type"]
