def quick_sort(array):
    if len(array) < 2:
        return array
    sort(array, 0, len(array) - 1)
    return array
    
def sort(array, start, end):
    if end <= start:
        return
    anchor = partition(array, start, end)
    sort(array, start, anchor - 1)
    sort(array, anchor + 1, end)

def partition(array, start, end):
    pivot = array[end]
    low = start - 1
    high = start
    while high < end:
        if array[high] < pivot:
            low += 1
            swap(array, low, high)
        high += 1
    swap(array, low + 1, end)
    return low + 1

def swap(array, idx1, idx2):
    tmp = array[idx1]
    array[idx1] = array[idx2]
    array[idx2] = tmp
