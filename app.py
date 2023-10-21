import time
import psutil

def display_usage(cpu_usage, mem_usage, bars=50):
    cpu_percent = cpu_usage / 100
    cpu_bar = '▋' * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars))
    
    mem_percent = mem_usage / 100
    mem_bar = '▋' * int(mem_percent * bars) + '-' * (bars - int(mem_percent * bars))

    # Formatting the output to display CPU and Memory usage side by side
    print(f"CPU Usage:    |{cpu_bar}| {cpu_usage:.2f}%     ", end="")
    print(f"Memory Usage: |{mem_bar}| {mem_usage:.2f}%", end="\r\n")

while True:
    display_usage(psutil.cpu_percent(), psutil.virtual_memory().percent, 30)
    time.sleep(1)


import psutil

def get_usage(app_name):
    cpu_usage = 0
    memory_usage = 0
    
    for proc in psutil.process_iter(attrs=["pid", "name", "cpu_percent", "memory_info"]):
        if proc.info['name'] == app_name:
            cpu_usage += proc.info['cpu_percent']
            memory_usage += proc.info['memory_info'].rss

    return cpu_usage, memory_usage / (1024 ** 2)  # Convert bytes to MB

app_name = "notepad.exe"
cpu, mem = get_usage(app_name)
print(f"CPU Usage for {app_name}: {cpu}%")
print(f"Memory Usage for {app_name}: {mem:.2f} MB")