def quicksort(a):
    less = []
    more = []
    pivotList = []
    if len(a) <= 1:
        return a
    else:
        pivot = a[0]
        for i in a:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quicksort(less)
        more = quicksort(more)
        return less + pivotList + more

