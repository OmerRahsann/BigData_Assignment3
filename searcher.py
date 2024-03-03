from db_config import get_redis_connection
import json

class Searcher:
    """A class to perform search operations on data stored in RedisJSON."""

    def __init__(self, key):
        """
        Initializes the Searcher with the key of the RedisJSON data.

        :param key: The key of the RedisJSON data to search.
        """
        self.redis = get_redis_connection()
        self.key = key

    def find_item_by_attribute(self, attribute, key):
        """Finds the value for a given key in the specified attribute."""
        data = json.loads(self.redis.json().get(self.key, '.'))
        if attribute in data and key in data[attribute]:
            value = data[attribute][key]
            print(f"Value found: {value}")
            return value
        print("Value not found.")
        return None
