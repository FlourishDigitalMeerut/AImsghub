def test_generate_api_keys(client):
    res = client.post("/api-keys/generate")
    assert res.status_code == 200
    assert res.json()["success"] is True


def test_get_my_keys(client):
    res = client.get("/api-keys/my-keys")
    assert res.status_code == 200
    assert "keys" in res.json()


def test_rotate_keys(client):
    res = client.post("/api-keys/rotate")
    assert res.status_code == 200
    assert res.json()["success"] is True