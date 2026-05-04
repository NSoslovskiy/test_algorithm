import sys

data = sys.stdin.read()
a = list(map(int, data.split()))

for i in range(0, len(a) - 1):
    for j in range(0, len(a) - 1):
        if a[j] < a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

sys.stdout.write(str(a) + '\n')
