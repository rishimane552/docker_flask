"""This test the about page"""


def test_request_about(client):
    """This makes the about page"""
    response = client.get("/about")
    assert response.status_code == 200
