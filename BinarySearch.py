# binary search
def binarysearch(l, value):             # takes a list and number to search for
    low = 0                             # low bound starts as first element
    high = len(l)-1                     # high bound starts as last element
    while low <= high:
        mid = (low+high) // 2           # finds middle element to start at
        if l[mid] > value:              # if mid element > value, sets high bound to mid-1
            high = mid - 1
        elif l[mid] < value:            # if mid element < value, sets low bound to mid+1
            low = mid + 1
        else:
            return mid                  # if mid element == value, returns mid element
    return -1                           # returns -1 if element is not found


