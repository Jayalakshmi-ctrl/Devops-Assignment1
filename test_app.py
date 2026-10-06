import pytest
import json
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_stage1_calculator_success(client):
    payload = {"name": "BITS Student", "program": "Fat Loss (FL)", "weight": 70}
    response = client.post('/api/clients/calculate', data=json.dumps(payload), content_type='application/json')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["estimated_calories"] == "1540 kcal"
