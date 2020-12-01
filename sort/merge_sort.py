import math

def merge_sort(array):
  if len(array) <= 1:
    return array
  start = 0
  end = len(array) - 1
  sort(array, start, end)
  return array

def sort(array, start, end):
  if end <= start:
    return
  middle = get_middle_idx(start, end)
  sort(
    array, 
    start,
    middle - 1)
  sort(
    array,
    middle,
    end)
  merge(array, start, middle, end)

def get_middle_idx(start, end):
  return int(math.ceil((end + start) / 2))
  
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
