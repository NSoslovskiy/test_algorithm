import sys

data = sys.stdin.read()
a = list(map(int, data.split()))

for i in range(1, len(a)):
    key = a[i]
    j = i - 1
    while j >= 0 and a[j] < key:
        a[j+1] = a[j]
        j = j - 1
    a[j+1] = key

sys.stdout.write(str(a[:100]) + '\n')
sys.stdout.write("Total elements sorted: " + str(len(a)) + '\n')