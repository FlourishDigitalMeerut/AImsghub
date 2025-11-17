def test_get_whatsapp_campaigns(client):
    res = client.get("/whatsapp/campaigns")
    assert res.status_code in (200, 404)
    if res.status_code == 200:  
        assert "campaigns" in res.json()