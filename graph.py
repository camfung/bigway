import matplotlib.pyplot as plt
from datetime import datetime


def plot_waitlist_data(lines):
    # Prepare lists to hold the parsed dates and waitlist lengths
    times = []
    waitlist_lengths = []

    # Parse each line
    for line in lines:
        # Split the line by comma to separate the timestamp and waitlist length
        timestamp, length = line.split(', ')
        # Convert timestamp to datetime object
        dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
        # Append the datetime and waitlist length (converted to int) to the lists
        times.append(dt)
        waitlist_lengths.append(int(length))

    # Create a plot
    plt.figure(figsize=(10, 5))
    plt.plot(times, waitlist_lengths, marker='o', linestyle='-')
    plt.xlabel('Time')
    plt.ylabel('Waitlist Length')
    plt.title('Waitlist Length vs Time')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def bar_graph(lines):
    times = []
    waitlist_lengths = []

    # Parse each line
    for line in lines:
        # Split the line by comma to separate the timestamp and waitlist length
        timestamp, length = line.split(', ')
        # Convert timestamp to datetime object
        dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
        # Append the datetime and waitlist length (converted to int) to the lists
        times.append(dt)
        waitlist_lengths.append(int(length))

    # Create a bar graph
    plt.figure(figsize=(12, 6))
    plt.bar(times, waitlist_lengths, width=0.0007,
            align='center', color='blue')
    plt.xlabel('Time')
    plt.ylabel('Waitlist Length')
    plt.title('Waitlist Length vs Time (Bar Graph)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


data = ""
with open("line_data.txt") as file:
    data = file.readlines()


# plot_waitlist_data(data)

bar_graph(data)
