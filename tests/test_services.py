import requests


def test_backend():
    response = requests.get("http://localhost:8000/docs")
    assert response.status_code == requests.codes.ok


def test_frontend():
    response = requests.get("http://localhost:3000")
    assert response.status_code == requests.codes.ok
