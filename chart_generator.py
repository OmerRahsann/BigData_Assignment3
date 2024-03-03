import matplotlib.pyplot as plt
from db_config import get_redis_connection
import json

class ChartGenerator:
    """A class to generate charts from data stored in RedisJSON."""

    def __init__(self, key):
        """
        Initializes the ChartGenerator with the key of the RedisJSON data.

        :param key: The key of the RedisJSON data to generate charts from.
        """
        self.redis = get_redis_connection()
        self.key = key

    def plot_top_currencies_by_rate(self, top_n):
        """Plots the exchange rates for the top N currencies."""
        # Get JSON data from Redis and decode
        json_data = self.redis.json().get(self.key)
        data = json.loads(json_data)

        rates = data.get('rates', {})

        # Sort the currencies by their exchange rates in descending order
        sorted_rates = sorted(rates.items(), key=lambda x: x[1], reverse=True)[:top_n]

        # Separate the currency codes and their rates
        currencies, exchange_rates = zip(*sorted_rates)

        # Plot the bar chart
        plt.bar(currencies, exchange_rates)
        plt.xlabel('Currency')
        plt.ylabel('Exchange Rate')
        plt.title(f'Top {top_n} Currencies by Exchange Rate')
        plt.show()
