import user
import requests

class MockResponse:
    @staticmethod
    def json():
        return {'id': 1, 'name': 'Mock User'}
    
    @staticmethod
    def raise_for_status():
        pass

def mock_get(url):
    return MockResponse()

def test_fetch_user():
    # Save the real requests.get method
    real_get = requests.get

    try:
        # Replace the real requests.get method with our mock_get method
        requests.get = mock_get

        # Call the function to test
        result = user.fetch_user(1)

        # Assert that the result matches the mock response data
        assert result == {'id': 1, 'name': 'Mock User'}

    finally:
        requests.get = real_get

if __name__ == "__main__":
    test_fetch_user()
    print("Test passed!")
