from heapq import merge

def mergesort(m):
    if len(m) <= 1:
        return m

    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]

    left = mergesort(left)
    right = mergesort(right)

    return list(merge(left, right))