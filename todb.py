from datetime import datetime
from db import execute_query_with_values_batch
import sys


def process_and_store_data(data):
    # Parse the array of strings and extract the timestamp and values
    parsed_data = []
    for entry in data:
        timestamp_str, value_str = entry.split(", ")
        timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
        value = int(value_str)
        parsed_data.append((timestamp, value))
        print(timestamp, value)

    # Construct the SQL INSERT query
    query = """
    INSERT INTO waitlist (date, waitlist_length) 
    VALUES (%s, %s)
    """

    # Use the provided function to execute the batch insert
    execute_query_with_values_batch(query, parsed_data)


def main(file_name):
    data = []
    with open(file_name) as file:
        lines = file.readlines()
        for line in lines:
            data.append(line.rstrip("\n"))
    process_and_store_data(data)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python todb.py <file_name>")
        sys.exit(1)

    file_name = sys.argv[1]
    main(file_name)
