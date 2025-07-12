from threading import Thread, Lock
counter = 0
counter_lock = Lock()

def increase_counter():
    global counter
    for _ in range(1000000):
        with counter_lock:
            counter += 1


def decrease_counter():
    global counter
    for _ in range(1000000):
        with counter_lock:
            counter -= 1

# Create two threads
thread1 = Thread(target=increase_counter)
thread2 = Thread(target=decrease_counter)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

# Print the final value of the counter
print("Final counter value: ", counter)