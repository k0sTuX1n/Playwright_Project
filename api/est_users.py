from api.api_client import ApiClient


def test_get_users():
    client = ApiClient("https://jsonplaceholder.typicode.com")

    response = client.get("/users")

    assert response.status_code == 200

def test_create_user():
    client = ApiClient("https://jsonplaceholder.typicode.com")

    response = client.post(
        "/users",
        {
            "name": "Ivan",
            "email": "ivan@mail.com"
        }
    )

    assert response.status_code == 201
