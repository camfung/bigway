import matplotlib.pyplot as plt
from datetime import datetime, timedelta


def bar_graph(lines, diagram_file_name):
    times = []
    waitlist_lengths = []

    # Parse each line
    for line in lines:
        # Split the line by comma to separate the timestamp and waitlist length
        timestamp, length = line.split(', ')
        # Convert timestamp to datetime object
        dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
        # Adjust the time by subtracting 6 hours if necessary
        time = dt - timedelta(hours=6)
        times.append(time)
        waitlist_lengths.append(int(length))

    # Format times for the x-axis
    str_times = [time.strftime("%H:%M") for time in times]

    # Create a bar graph
    plt.figure(figsize=(12, 6))
    # Set a reasonable width for the bars to make them visible
    plt.bar(str_times, waitlist_lengths, width=0.3,
            align='center', color='blue')
    plt.xlabel('Time')
    plt.ylabel('Waitlist Length')
    plt.title('Bigway wait list times Tuesday')
    plt.xticks(ticks=[i for i in range(0, len(str_times), 5)], rotation=45)
    plt.tight_layout()
    plt.savefig(diagram_file_name)


data = ""
with open("condensed.txt", "r") as file:
    data = file.readlines()
    for line in data:
        line.strip()

bar_graph(data, 'waitlist_graph.png')
