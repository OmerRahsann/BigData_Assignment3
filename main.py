from redis_processor import RedisProcessor
from aggregator import Aggregator
from searcher import Searcher
from chart_generator import ChartGenerator

def main():
    # Use the ExchangeRate-API endpoint for USD
    api_url = 'https://open.er-api.com/v6/latest/USD'
    key = 'exchange_rate_data'

    # Fetch and store exchange rate data
    processor = RedisProcessor(api_url)
    data = processor.fetch_data()
    processor.store_data(data, key)

    # Aggregation example: Count the number of currencies
    aggregator = Aggregator(key)
    count = aggregator.count_items()
    print(f"Total number of currencies: {count}")

    # Prompt the user to enter a currency code
    currency_code = input("Enter the currency code you want to view (e.g., EUR, GBP, JPY): ").upper()

    # Find the exchange rate for the specified currency
    searcher = Searcher(key)
    rate = searcher.find_item_by_attribute('rates', currency_code)
    if rate:
        print(f"Exchange rate for {currency_code}: {rate}")
    else:
        print(f"Exchange rate for {currency_code} not found.")

    # Plot the exchange rates for the top 10 currencies
    chart_generator = ChartGenerator(key)
    chart_generator.plot_top_currencies_by_rate(10)

if __name__ == '__main__':
    main()
