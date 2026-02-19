import requests
import pytest
from faker import Faker
fake = Faker()
from src.config import ADMIN_API_KEY, API_KEY, BASE_URL

BASE_URL = "https://kzmcpfklrqymzazaxlmv.supabase.co/functions/v1/partner-loan-api"


@pytest.fixture
def loan_payload():
    return {
        "first_name": fake.first_name(), 
        "last_name": fake.last_name(),
        "personal_number": "19900101-1234",
        "email": fake.email(),
        "loan_amount": 10000,
        "address": fake.street_address(),
        "postcode": fake.postcode(),
        "city": fake.city(),
        "phone": fake.phone_number(),
        "employment_type": "employed",
        "employer": fake.company(),
        "income": 30000,
        "repayment_months": 12,
        "product_type": "personal"
        }
    
    
def test_skapa_loan(loan_payload):
    headers = {
        "x-api-key": API_KEY,
        "Content-Type": "application/json"
    }
    
    
    response = requests.post(f"{BASE_URL}", json=loan_payload, headers=headers)
    #tillfälligs
    #print(f"STATUS: {response.status_code}")
    print(f"BODY: {response.text}")
    assert response.status_code == 200
    
    in_the_data = response.json()
    assert in_the_data["success"] == True
    assert "application" in in_the_data
    assert "reference_number" in in_the_data["application"]
    assert in_the_data["application"]["reference_number"] is not None
    
    

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
