import psutil
import time

THRESHOLD = 80  # CPU usage threshold percentage

print("Monitoring CPU usage...")

try:
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)

        if cpu_usage > THRESHOLD:
            print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")

except KeyboardInterrupt:
    print("\nMonitoring stopped by user.")
except Exception as e:
    print(f"An error occurred: {e}")
