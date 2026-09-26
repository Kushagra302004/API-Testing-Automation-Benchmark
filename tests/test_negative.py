import pytest

def test_missing_user(api_client):
    assert api_client.get("/users/999999").status_code == 404

def test_missing_required_field(api_client):
    r = api_client.post("/users", {"name":"No Email","age":25})
    assert r.status_code == 422

@pytest.mark.parametrize("age", [17, 61])
def test_age_outside_range(api_client, age):
    r = api_client.post("/users", {"name":"Boundary","email":"b@example.com","age":age})
    assert r.status_code == 422

def test_invalid_token(api_client):
    r = api_client.get("/protected", headers={"Authorization":"Bearer invalid-token"})
    assert r.status_code == 401
