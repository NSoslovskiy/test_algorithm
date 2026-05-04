import random

def generate(n):
    data = [random.randint(1, 1000) for _ in range(n)]
    data.sort()

    print(*data)

generate(500)
