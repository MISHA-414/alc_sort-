def bubble_sort(a):
    n = len(a)
    unordered = True
    while unordered:
        unordered = False
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                unordered = True
        n-=1
    return a
