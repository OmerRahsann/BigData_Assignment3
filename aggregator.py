from db_config import get_redis_connection
import json

class Aggregator:
    """A class to perform aggregation operations on data stored in RedisJSON."""

    def __init__(self, key):
        """
        Initializes the Aggregator with the key of the RedisJSON data.

        :param key: The key of the RedisJSON data to aggregate.
        """
        self.redis = get_redis_connection()
        self.key = key

    def count_items(self):
        """Counts the number of items in the data."""
        data = json.loads(self.redis.json().get(self.key, '.'))
        count = len(data)
        print(f"Total items: {count}")
        return count
