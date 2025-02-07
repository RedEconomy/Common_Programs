#Times the runtime of the function
import time


class FunctionTimer:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = time.time()
        self.end_time = None
        print("Timer started.")

    def stop(self):
        if self.start_time is None:
            raise ValueError("Timer has not been started. Use the 'start' method first.")
        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time
        print(f"Timer stopped. Elapsed time: {elapsed_time:.6f} seconds.")
        return elapsed_time

    def time_function(self, func, *args, **kwargs):
        print(f"Timing function '{func.__name__}'...")
        self.start()
        result = func(*args, **kwargs)
        elapsed_time = self.stop()
        return result, elapsed_time



if __name__ == "__main__":
    timer = FunctionTimer()

    # Time the function directly
    result, elapsed = timer.time_function('example_function', int)
    print(f"Function result: {result}")
    print(f"Elapsed time: {elapsed:.6f} seconds")
