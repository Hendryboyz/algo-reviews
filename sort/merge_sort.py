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
  # sort(array, start, , middle - 1)
  # sort(array, middle, , end)
  # merge(array, start, middle, end)
  
def merge(array, start, middle, end):
  pass
