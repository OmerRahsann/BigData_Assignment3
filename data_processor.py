import requests

class DataProcessor:
    """A class to process data from an API."""

    def __init__(self, api_url):
        """
        Initializes the DataProcessor with the API URL.

        :param api_url: URL of the API to fetch data from.
        """
        self.api_url = api_url

    def fetch_data(self):
        """Fetches exchange rate data from the API."""
        response = requests.get(self.api_url)
        data = response.json()
        print("Exchange rate data fetched from API.")
        return data
