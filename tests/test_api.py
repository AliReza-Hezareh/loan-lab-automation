import requests
import pytest
from faker import Faker
fake = Faker()
from src.config import API_KEY, BASE_URL

BASE_URL = "https://kzmcpfklrqymzazaxlmv.supabase.co/functions/v1/partner-loan-api"


@pytest.fixture
def loan_payload():
    return {
        "reference_number": "199001011234",  # Skatteverkets testnummer
        "status": "bra",
        "loan_amount": "50000",     
        "repayment_months": "12",  

    }
    
    
def test_skapa_loan(loan_payload):
    headers = {
        "x-admin-api-key": API_KEY,
        "Content-Type": "application/json"
    }
    
    response = requests.post(f"{BASE_URL}/partner-loan-api", json=loan_payload, headers=headers)
    assert response.status_code == 200
    
    #tillfälligs
    print(f"Response JSON: {response.status_code}")
    print(f"response.json(): {response.text}")

    
    in_the_data = response.json()
    assert in_the_data["success"] == True
    assert in_the_data["partner_name"] == "AliR"
    assert in_the_data["reference_number"] is not None
    
    

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
