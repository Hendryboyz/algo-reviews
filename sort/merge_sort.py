import math

def merge_sort(array):
  if len(array) <= 1:
    return array
  start = 0
  end = len(array) - 1
  mid = get_middle_idx(start, end)
  sort(array, start, mid, end)
  return array

def get_middle_idx(start, end):
  return int(math.ceil((end + start) / 2))

def sort(array, start, middle, end):
  if end <= start:
    return
  sort(
    array, 
    start,
    get_middle_idx(start, middle - 1),
    middle - 1)
  sort(
    array,
    middle,
    get_middle_idx(middle, end),
    end)
  merge(array, start, middle, end)
  
def merge(array, start, middle, end):
  left = array[start:middle]
  right = array[middle:end+1]
  left_idx = right_idx = 0
  idx = start

  while left_idx != len(left) and right_idx != len(right):
    if left[left_idx] <= right[right_idx]:
      array[idx] = left[left_idx]
      left_idx += 1
    else:
      array[idx] = right[right_idx]
      right_idx += 1
    idx += 1
  
  while right_idx != len(right):
    array[idx] = right[right_idx]
    right_idx += 1
    idx += 1

  while left_idx != len(left):
    array[idx] = left[left_idx]
    left_idx += 1
    idx += 1
