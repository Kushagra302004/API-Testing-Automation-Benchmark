def test_get_existing_user(api_client):
    r = api_client.get("/users/1")
    assert r.status_code == 200
    assert r.json()["id"] == 1
    assert isinstance(r.json()["age"], int)

def test_create_user(api_client):
    payload = {"name":"Test User","email":"test@example.com","age":25}
    r = api_client.post("/users", payload)
    assert r.status_code == 201
    assert r.json()["name"] == payload["name"]

def test_update_user_put(api_client):
    payload = {"name":"Updated","email":"updated@example.com","age":26}
    r = api_client.put("/users/1", payload)
    assert r.status_code == 200
    assert r.json()["name"] == "Updated"

def test_partial_update_patch(api_client):
    r = api_client.patch("/users/1", {"age":30})
    assert r.status_code == 200
    assert r.json()["age"] == 30

def test_delete_user(api_client):
    created = api_client.post("/users", {"name":"Delete Me","email":"delete@example.com","age":25})
    user_id = created.json()["id"]
    assert api_client.delete(f"/users/{user_id}").status_code == 204
    assert api_client.get(f"/users/{user_id}").status_code == 404
