def test_request_example(client):
    """This makes the about page"""
    response = client.get("/about")
    assert response.status_code == 200
