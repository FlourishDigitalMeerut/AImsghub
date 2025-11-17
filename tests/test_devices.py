def test_get_devices(client):
    res = client.get("/devices")
    assert res.status_code in (200, 404)
    if res.status_code == 200:
        assert "devices" in res.json()