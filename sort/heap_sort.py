import math

# build min heap will cause sort descending, vice versa
def heap_sort(array):
  build_heap(array, len(array) - 1)
  for i in range(len(array) - 2, -1, -1):
    swap(array, 0, i + 1)
    build_heap(array, i)
  return array

def build_heap(array, last):
  last_idx_with_child = int(math.ceil(last / 2) - 1)
  for i in range(last_idx_with_child + 1, -1, -1):
    heapify(array, i, last, False)

def heapify(array, root_idx, last, min = True):
  if root_idx == last:
    return
  left = root_idx * 2 + 1
  right = root_idx * 2 + 2
  target = root_idx
  if is_out_of_array(left, last) == False and (array[left] < array[target]) == min:
    target = left
  if is_out_of_array(right, last) == False and (array[right] < array[target]) == min:
    target = right
  if target != root_idx:
    swap(array, target, root_idx)

def is_out_of_array(idx, last_idx):
  return idx > last_idx

def swap(array, idx1, idx2):
  tmp = array[idx1]
  array[idx1] = array[idx2]
  array[idx2] = tmp
