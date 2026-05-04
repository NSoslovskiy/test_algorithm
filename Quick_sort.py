import sys

sys.setrecursionlimit(3000)

def quick_sort_desc(a):
    if len(a) <= 1:
        return a
    pivot = a[0]
    left = [x for x in a[1:] if x >= pivot]
    right = [x for x in a[1:] if x < pivot]
    return quick_sort_desc(left) + [pivot] + quick_sort_desc(right)

data = sys.stdin.read()
a = list(map(int, data.split()))

result = quick_sort_desc(a)

sys.stdout.write(str(result[:100]) + '\n')
sys.stdout.write("Total elements sorted: " + str(len(result)) + '\n')