# tests/test_app.py
import pytest
import json
from flask_app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    client = app.test_client()

    yield client

def test_create_user(client):
    user_data = {
        "username": "john_doe",
        "password": "securepassword",
        "profile": {
            "email": "john_doe@example.com",
            "name": "John Doe",
            "age": 30
        }
    }
    response = client.post('/user', data=json.dumps(user_data), content_type='application/json')
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['username'] == user_data['username']
    assert data['profile']['email'] == user_data['profile']['email']

def test_create_user_invalid_data(client):
    user_data = {
        "username": "john_doe"
        # Missing password and profile
    }
    response = client.post('/user', data=json.dumps(user_data), content_type='application/json')
    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'error' in data

def test_get_users(client):
    user_data = {
        "username": "john_doe",
        "password": "securepassword",
        "profile": {
            "email": "john_doe@example.com",
            "name": "John Doe",
            "age": 30
        }
    }
    # Create a user first
    client.post('/user', data=json.dumps(user_data), content_type='application/json')

    # Get users
    response = client.get('/users')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 1
    assert data[0]['username'] == user_data['username']
