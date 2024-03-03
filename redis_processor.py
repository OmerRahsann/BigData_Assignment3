from data_processor import DataProcessor
from db_config import get_redis_connection
import json

class RedisProcessor(DataProcessor):
    """A class to process data from an API and store it in RedisJSON."""

    def __init__(self, api_url):
        """
        Initializes the RedisProcessor with the API URL.

        :param api_url: URL of the API to fetch data from.
        """
        super().__init__(api_url)
        self.redis = get_redis_connection()

    def store_data(self, data, key='big_data'):
        """Stores data in RedisJSON."""
        self.redis.json().set(key, '.', json.dumps(data))
        print("Data stored in RedisJSON.")
