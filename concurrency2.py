import multiprocessing
import time


def producer_proc(queue):
    for i in range(1, 20):
        print(f"Producer putting: {i}")
        queue.put(i)


def consumer_proc(queue):
    time.sleep(1)
    while True:
        item = queue.get()  # Blocks until an item is available
        if item is None:
            break  # Exit the loop if None is received
        print(f"Consumer received: {item}")


if __name__ == "__main__":
    # Queue for inter-process communication
    my_queue = multiprocessing.Queue()

    # Create the processes
    producer_process = multiprocessing.Process(target=producer_proc, args=(my_queue,))
    consumer_process = multiprocessing.Process(target=consumer_proc, args=(my_queue,))

    # Start the processes
    producer_process.start()
    consumer_process.start()

    # Wait for the producer process to finish
    producer_process.join()

    # Signal the consumer process to exit
    my_queue.put(None)

    # Wait for the consumer process to finish
    consumer_process.join()

    print("Both processes have finished execution.")