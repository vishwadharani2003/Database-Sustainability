import psutil

# Get the CPU usage (interval of 1 second)
cpu_usage = psutil.cpu_percent(1)
print(f"CPU Usage: {cpu_usage}%")