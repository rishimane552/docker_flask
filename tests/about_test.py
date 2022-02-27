def test_request_example(client):
    """This makes the about page"""
    response = client.get("/")
    assert b"Nobis assumenda" in response.data
