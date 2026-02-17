import requests
from src.config import API_KEY, BASE_URL

BASE_URL = "https://kzmcpfklrqymzazaxlmv.supabase.co/functions/v1/partner-loan-api"

def test_get_health_status():
    
    headers = {
        "x-api-key": API_KEY
    }
    response = requests.get(f"{BASE_URL}/health" , headers=headers)
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
    assert "application/json" in response.headers["Content-Type"]
