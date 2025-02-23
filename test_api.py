import requests

# Define the API endpoint
API_URL = "https://jsonplaceholder.typicode.com/posts/1"

def test_status_code():
    """Test if the API returns a 200 status code."""
    response = requests.get(API_URL)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

def test_response_json():
    """Test if the response contains expected keys."""
    response = requests.get(API_URL)
    json_data = response.json()

    expected_keys = ["userId", "id", "title", "body"]
    for key in expected_keys:
        assert key in json_data, f"Missing key: {key}"

def test_title_is_string():
    """Test if the title is a string."""
    response = requests.get(API_URL)
    assert isinstance(response.json()["title"], str), "Title should be a string"

def test_body_is_not_empty():
    """Test if the body is not empty."""
    response = requests.get(API_URL)
    assert response.json()["body"], "Body should not be empty"


