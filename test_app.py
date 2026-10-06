# test_app.py
import pytest
import json
from app import create_app

@pytest.fixture
def client():
    """Configures an isolated browser simulation context for testing Stage 1 routes"""
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_stage1_calculator_success(client):
    """Validates that Stage 1 processes weight input and returns correct calorie metrics"""
    payload = {
        "name": "First Go User",
        "program": "Fat Loss (FL)",
        "weight": 70,
        "adherence": 90
    }
    # Targets the exact path layout exposed in the Stage 1 routes definition file
    response = client.post('/api/clients/calculate', 
                           data=json.dumps(payload), 
                           content_type='application/json')
    
    assert response.status_code == 200
    data = json.loads(response.data)
    
    # Checks Stage 1 core logic: 70 kg * 22 factor = 1540 kcal string format
    assert data["estimated_calories"] == "1540 kcal"
    assert "First Go User" in data["message"]
    assert "training_plan" in data

def test_stage1_missing_fields_validation(client):
    """Verifies that the early prototype gracefully catches empty name/program payloads"""
    payload = {"weight": 80}  # Intentionally missing name and program track keys
    response = client.post('/api/clients/calculate', 
                           data=json.dumps(payload), 
                           content_type='application/json')
    
    # Confirms the endpoint throws a 400 Bad Request error status code instead of crashing
    assert response.status_code == 400
    data = json.loads(response.data)
    assert "error" in data
