import tkinter as tk
import requests
import json
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class DataApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Line Counter")
        self.geometry("200x100")

        self.label = tk.Label(self, text="Loading...", font=("Arial", 16))
        self.label.pack(pady=20)

        # File to save the data
        self.log_file = "line_data.txt"

        self.update_data()

    def get_total_size(self, json_data):
        # Load the JSON data if it's provided as a string
        if isinstance(json_data, str):
            data = json.loads(json_data)
        else:
            data = json_data

        # Extract and return the 'totalSize' value
        return data['totalSize']

    def fetch_data(self):
        url = "https://gosnappy.io/v1/la/status"
        headers = {
            "referer": "https://gosnappy.io/lineup/?storeId=7289",
            "storeId": "7289"
        }
        response = requests.get(url, headers=headers)
        return response.text

    def save_data(self, size):
        # Get the current timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Log the timestamp and size
        logging.info(f"Timestamp: {timestamp}, Size: {size}")
        # Save to file
        with open(self.log_file, "a") as file:
            file.write(f"{timestamp}, {size}\n")

    def update_data(self):
        try:
            json_data = self.fetch_data()
            size = self.get_total_size(json_data)
            self.label.config(text=f"{size}")
            self.save_data(size)
        except Exception as e:
            logging.error(f"Error fetching or processing data: {e}")
            self.label.config(text="Error loading data")

        self.after(60000, self.update_data)  # Schedule the update every minute


app = DataApp()
app.mainloop()
