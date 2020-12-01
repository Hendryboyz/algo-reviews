def heap_sort(array):
  build_min_heap(array, len(array) - 1)
  for i in range(len(array) - 2, -1, -1):
    swap(array, 0, i + 1)
    build_min_heap(array, i)
  return array

def build_min_heap(array, last):
  print(last)

def min_heapify(array, root_idx, last):
  if root_idx == last:
    return
  left = root_idx * 2 + 1
  right = root_idx * 2 + 2
  min_idx = root_idx
  if is_out_of_array(left, last) == False and array[left] < array[min_idx]:
    min_idx = left
  if is_out_of_array(right, last) == False and array[right] < array[min_idx]:
    min_idx = right
  if min_idx != root_idx:
    swap(array, min_idx, root_idx)
  print(array)

def is_out_of_array(idx, last_idx):
  return idx > last_idx

def swap(array, idx1, idx2):
  tmp = array[idx1]
  array[idx1] = array[idx2]
  array[idx2] = tmp
