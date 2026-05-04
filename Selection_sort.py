import sys

data = sys.stdin.read()
a = list(map(int, data.split()))

for i in range(0, len(a)-1):
    m = max(a[i:])
    idx = a.index(m, i)
    a[i], a[idx] = a[idx], a[i]

sys.stdout.write(str(a[:100]) + '\n')
sys.stdout.write("Total elements sorted: " + str(len(a)) + '\n')