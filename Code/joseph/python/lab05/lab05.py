import random

def generate_numbers():
    p = []
    p.append(random.sample(range(1, 99), 6))
    return p