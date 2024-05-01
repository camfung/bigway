import json
import requests
import logging
from datetime import datetime
import time


class BigWayLineUp:
    def __init__(self, update_interval):
        self.time_list = []
        self.update_interval = update_interval

        current_date = datetime.now()
        formatted_date = current_date.strftime('%m_%d_%Y')

        self.log_file = f"log-{formatted_date}.txt"
        self.save_file = f"data-{formatted_date}.txt"
        logging.basicConfig(filename=self.log_file, level=logging.INFO)

    def _get_total_size(self, json_data):
        if isinstance(json_data, str):
            data = json.loads(json_data)
        else:
            data = json_data
        return data['totalSize']

    def _fetch_data(self):
        url = "https://gosnappy.io/v1/la/status"
        headers = {
            "referer": "https://gosnappy.io/lineup/?storeId=7289",
            "storeId": "7289"
        }
        response = requests.get(url, headers=headers)
        return response.text

    def update_data(self):
        try:
            json_data = self._fetch_data()
            size = self._get_total_size(json_data)
            return size
        except Exception as e:
            logging.error(f"Error fetching or processing data: {e}")

    def format_data(self, size):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logging.info(f"Timestamp: {timestamp}, Size: {size}")

        return timestamp, size

    def run(self):
        while True:
            size = self.update_data()
            if size is not None:
                with open(self.save_file, "a") as file:
                    timestamp, formatted_size = self.format_data(size)
                    self.time_list.append((timestamp, formatted_size))
                    file.write(f"{timestamp}, {formatted_size}\n")

            time.sleep(self.update_interval)


bigWayLineUp = BigWayLineUp(60*5)
bigWayLineUp.run()
