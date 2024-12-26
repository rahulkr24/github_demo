import requests


def test_greet_default():
    """
    Test the default greeting when no name is provided.
    """
    response = requests.get("http://127.0.0.1:8000/greet").json()

    assert response["status"] == True


def test_greet_with_name():
    """
    Test the greeting with a custom name.
    """
    response = requests.get("http://127.0.0.1:8000/greet", params={"name": "Alice"}).json()
    assert response["status"] == True
