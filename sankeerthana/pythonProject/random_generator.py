import random

def generate_random_numbers(count, start, end):
    return [random.randint(start, end) for _ in range(count)]