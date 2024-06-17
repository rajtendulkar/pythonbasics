import time
from functools import wraps


# Decorator to log the execution time of a function
def measure_execution_time(func):
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function executed in {execution_time:.3f} seconds")
        return result

    return with_logging


# Sample function to demonstrate the decorator
@measure_execution_time
def time_delay_function(time_delay):
    print("Starting function")
    time.sleep(time_delay)
    print("Function finished.")


if __name__ == "__main__":
    time_delay_function(1)
    time_delay_function(5)
    time_delay_function(10)
