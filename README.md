# BigData_Assignment3
# Exchange Rate Data Processor and Visualizer

## Overview

This application is designed to fetch exchange rate data from the ExchangeRate-API, store it in Redis, and perform various operations such as aggregation, search, and chart generation. It demonstrates the use of object-oriented programming principles in Python to structure the application in a modular and reusable way. The application  includes a prompt section where users can enter the currency code they want to view.

## Features

- Fetches exchange rate data from the ExchangeRate-API.
- Stores the data in Redis for persistent storage.
- Aggregates the data to count the number of currencies available.
- Allows users to search for the exchange rate of a specific currency.
- Generates a bar chart to visualize the exchange rates of the top N currencies.

## Requirements

- Python 3.x
- Redis server
- `requests` library for making API requests.
- `matplotlib` library for generating charts.
- `redis-py` library for interacting with Redis.


## Usage

1. Update the `db_config.py` file with your Redis server configuration.
2. Run the `main.py` script to fetch the exchange rate data, store it in Redis, and perform the operations:
   ```bash
   python main.py
   ```
3. When prompted, enter the currency code you want to view (e.g., EUR, GBP, JPY).

## Files

- `data_processor.py`: Contains the `DataProcessor` class for fetching data from the API.
- `redis_processor.py`: Contains the `RedisProcessor` class for storing and retrieving data in Redis.
- `aggregator.py`: Contains the `Aggregator` class for performing aggregation operations on the data.
- `searcher.py`: Contains the `Searcher` class for searching specific data from the stored data.
- `chart_generator.py`: Contains the `ChartGenerator` class for generating charts based on the data.
- `main.py`: The main script that uses the above classes to fetch, store, and process the data.
- `db_config.py`: Configuration file for Redis connection settings.

## Notes

- Ensure that your Redis server is running before executing the script.
- You can modify the `main.py` script to change the query or perform different operations based on your requirements.

## License

This project is open-sourced under the MIT License.