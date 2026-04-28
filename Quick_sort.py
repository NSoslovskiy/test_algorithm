def quick_sort_desc(a):
    if len(a) <= 1:
        return a
    pivot = a[0]
    left = [x for x in a[1:] if x >= pivot]
    right = [x for x in a[1:] if x < pivot]
    return quick_sort_desc(left) + [pivot] + quick_sort_desc(right)

a = [76, 73, 69, 63, 67, 24, 42]
print(quick_sort_desc(a))