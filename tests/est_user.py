def test_user():
    user = {
        "name": "alex",
        "age": 25,
        "active": True
    }

    assert user["name"] == "alex"
    assert user["age"] >= 18
    assert user["active"] == True

