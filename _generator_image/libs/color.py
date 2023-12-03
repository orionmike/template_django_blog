
import random


def get_random_color(rgb_start: int, rgb_finish: int) -> tuple:

    result = random.randint(rgb_start, rgb_finish), \
        random.randint(rgb_start, rgb_finish), \
        random.randint(rgb_start, rgb_finish)

    return result
