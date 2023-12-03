import time


def get_execute_time(start_time: time) -> float:
    time_now = time.time()
    print(f'time execute: {round(time_now - start_time, 2)}')
