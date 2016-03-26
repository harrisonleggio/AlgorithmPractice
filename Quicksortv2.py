# quicksort function
def quicksort(a):
    less = []               # array for #'s less than pivot
    more = []               # array for #'s greater than pivot
    pivotList = []          # array for #'s = pivot
    if len(a) <= 1:         # return original array if len = 1
        return a
    else:
        pivot = a[0]                    # start with first element as pivot
        for i in a:
            if i < pivot:               # if # < pivot add to less array
                less.append(i)
            elif i > pivot:             # if # > pivot add to more array
                more.append(i)
            else:                       # add pivot + duplicates to pivot array
                pivotList.append(i)
        less = quicksort(less)          # recursively sort less array
        more = quicksort(more)          # recursively sort more array
        return less + pivotList + more  # add 3 arrays together and return 1 array

