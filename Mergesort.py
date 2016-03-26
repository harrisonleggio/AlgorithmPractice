from heapq import merge             # import merge (python 2.6(?) or later)

# mergesort function
def mergesort(m):
    if len(m) <= 1:                 # returns given array if length is 1
        return m

    middle = len(m) // 2            # finds middle point of array
    left = m[:middle]               # left array takes all numbers from left to midpoint
    right = m[middle:]              # right array takes all numbers from midpoint to end

    left = mergesort(left)          # recursive call on left
    right = mergesort(right)        # recursive call on right

    return list(merge(left, right))     # merge both halves together (merge takes care of sorting)
