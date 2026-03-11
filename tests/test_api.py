from fastapi.testclient import TestClient
from src.main import app
from src.modules.models import Item

client = TestClient(app)

def test_create_item():
    response = client.post('/items/', json={'name': 'Test Item', 'description': 'A test item', 'price': 10.0, 'tax': 1.0})
    assert response.status_code == 200
    assert response.json()['name'] == 'Test Item'


def test_read_item():
    response = client.post('/items/', json={'name': 'Test Item', 'description': 'A test item', 'price': 10.0, 'tax': 1.0})
    item_id = response.json()['id']
    response = client.get(f'/items/{item_id}')
    assert response.status_code == 200
    assert response.json()['id'] == item_id


def test_update_item():
    response = client.post('/items/', json={'name': 'Test Item', 'description': 'A test item', 'price': 10.0, 'tax': 1.0})
    item_id = response.json()['id']
    response = client.put(f'/items/{item_id}', json={'name': 'Updated Item', 'description': 'An updated test item', 'price': 15.0, 'tax': 2.0})
    assert response.status_code == 200
    assert response.json()['name'] == 'Updated Item'


def test_delete_item():
    response = client.post('/items/', json={'name': 'Test Item', 'description': 'A test item', 'price': 10.0, 'tax': 1.0})
    item_id = response.json()['id']
    response = client.delete(f'/items/{item_id}')
    assert response.status_code == 200
    assert response.json()['message'] == 'Item deleted successfully'