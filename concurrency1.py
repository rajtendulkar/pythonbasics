import threading
import time

# shared variable between threads
count = 0


def thread1():
    global count
    for i in range(1, 6):
        print("Incrementing counter")
        count = count + 1
        time.sleep(1)


def thread2():
    global count
    for i in range(1, 6):
        print(f"counter is now : {count}")
        time.sleep(1)


if __name__ == "__main__":
    # Creating threads
    thread1 = threading.Thread(target=thread1)
    thread2 = threading.Thread(target=thread2)

    # Starting threads
    thread1.start()
    thread2.start()

    # Waiting for both threads to complete
    thread1.join()
    thread2.join()

    print("Threads finished")
