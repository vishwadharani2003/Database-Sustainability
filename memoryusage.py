import psutil

# Get memory details
memory_info = psutil.virtual_memory()

total_memory = memory_info.total / (1024 ** 3)  # Convert to GB
used_memory = memory_info.used / (1024 ** 3)    # Convert to GB
memory_percentage = memory_info.percent

print(f"Total Memory: {total_memory:.2f} GB")
print(f"Used Memory: {used_memory:.2f} GB")
print(f"Memory Usage: {memory_percentage}%")