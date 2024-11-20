import requests
import pytest


@pytest.fixture
def pet_data():
    return {
        "id": 123,
        "name": "Kachna",
        "status": "available"
    }


url = "https://petstore.swagger.io/v2/pet"


def test_create_pet(pet_data):

    response = requests.post(url, json=pet_data)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["id"] == pet_data["id"]
    assert response_data["name"] == pet_data["name"]
    assert response_data["status"] == pet_data["status"]


def test_get_pet(pet_data):

    response = requests.get(f"{url}/{pet_data['id']}")
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["id"] == pet_data["id"]
    assert response_data["name"] == pet_data["name"]


def test_update_pet(pet_data):

    updated_pet_data = pet_data.copy()
    updated_pet_data['name'] = "Kure"
    response = requests.put(url, json=updated_pet_data)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["name"] == updated_pet_data["name"]
