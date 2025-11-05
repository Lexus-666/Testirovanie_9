import requests

def test_get_post_by_id():
    """GET"""
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "userId" in data
    assert "title" in data
    assert "body" in data

def test_create_post():
    """POST"""
    payload = {
    "userId": 1,
    "title": "created post title",
    "body": "created post body"
    }
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]

def test_update_post():
    """PUT"""
    payload = {
    "id": 2,
    "title": "new",
    "body": "new",
    "userId": 1
    }
    response = requests.put(f"https://jsonplaceholder.typicode.com/posts/2", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 2
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]