import httpx

client = httpx.Client(base_url="http://localhost:8000")


def test_login_with_get_method_should_return_405():
    response = client.get(url="/auth/login")
    assert response.status_code == 405
    assert response.json() == {"detail": "Method Not Allowed"}, response.text


def test_login_without_session_cookie_should_return_401():
    response = client.post(url="/auth/login")
    assert response.status_code == 401
    assert response.json() == {"detail": "Unauthorized"}, response.text


def test_login_with_valid_session_cookie_should_return_200():
    client.cookies.set("__session", "jwt")
    response = client.post(url="/auth/login")
    assert response.status_code == 200
    assert response.json() == "ok", response.text
    client.cookies.clear()
