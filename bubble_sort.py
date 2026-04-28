a = [76, 73, 69, 63, 67, 24, 42]

for i in range(0, len(a) - 1):
    for j in range(0, len(a) - 1):

        if a[j] < a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)
