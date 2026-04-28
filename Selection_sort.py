a = [76, 73, 69, 63, 67, 24, 42]

for i in range(0, len(a)-1):
    m = max(a[i:])
    idx = a.index(m, i)
    a[i], a[idx] = a[idx], a[i]
    print(a)