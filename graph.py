import matplotlib.pyplot as plt
import sys
from datetime import datetime, timedelta


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


def bar_graph(lines, diagram_file_name):
    times = []
    waitlist_lengths = []

    # Parse each line
    for line in lines:
        # Split the line by comma to separate the timestamp and waitlist length
        timestamp, length = line.split(', ')
        # Convert timestamp to datetime object
        dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
        # Append the datetime and waitlist length (converted to int) to the lists
        time = dt - timedelta(hours=6)
        times.append(time)
        waitlist_lengths.append(int(length))

    str_times = [time.strftime("%H:%M") for time in times]
    # Create a bar graph
    plt.figure(figsize=(12, 6))
    plt.bar(str_times, waitlist_lengths, width=0.03,
            align='center', color='blue')
    plt.xlabel('Time')
    plt.ylabel('Waitlist Length')
    plt.title('Waitlist Length vs Time (Bar Graph)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(diagram_file_name)


diagram_file_name = ""
data = ""
file_name = ""
if len(sys.argv) < 2:
    file_name = "line_data.txt"
if len(sys.argv) < 3:
    diagram_file_name = "diagram.png"

file_name = sys.argv[1]
diagram_file_name = sys.argv[2]
with open(file_name) as file:
    data = file.readlines()

# plot_waitlist_data(data)

bar_graph(data, diagram_file_name)
