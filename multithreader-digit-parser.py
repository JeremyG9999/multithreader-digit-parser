import sys
import time
import threading

sys.set_int_max_str_digits(1500000)

# Predefined list of digit values
digit_values = [100000, 500000]

def times():
    for digits in digit_values:
        start = time.time()
        int('1' * digits)
        print(f"{digits} digits parsed in: {time.time() - start:.5f} seconds")

# Create and start threads
threads = []
for _ in range(1):  # Number of threads
    thread = threading.Thread(target=times)
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()