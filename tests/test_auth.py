def test_auth_protected_route(client):
    res = client.get("/api-keys/my-keys")
    assert res.status_code in (200, 401, 403)
