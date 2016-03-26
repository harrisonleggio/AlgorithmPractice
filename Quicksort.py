def partition (aList, start, end):                        # pass the list, first element, and last element
    pivot = aList[start]                                  # set pivot as first element
    left = start + 1                                      # sets left to first element after pivot
    right = end                                           # sets right to last element
    done = False                                          # sets done to false
    while not done:
        while left <= right and aList[left] <= pivot:
            left += 1
        while aList[right] >= pivot and right >= left:
            right -= 1
        if right < left:
            done = True
        else:
            temp = aList[left]
            aList[left] = aList[right]
            aList[right] = temp
    temp = aList[start]
    aList[start] = aList[right]
    aList[right] = temp
    return right

def quicksort(aList, start, end):
    if start < end:
        pivot = partition(aList, start, end)
        quicksort(aList, start, pivot-1)
        quicksort(aList, pivot+1, end)
    return aList