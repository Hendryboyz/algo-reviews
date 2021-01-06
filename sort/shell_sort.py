def shell_sort(array):
  for gap in [5, 3, 1]:
    insertion_sort_with_gap(array, gap)
  return array

def insertion_sort_with_gap(array, gap = 1):
  for i in range(len(array)):
    for j in range(i - gap, -1, -gap):
      if j + gap >= len(array):
        continue
      if array[j] < array[j + gap]: # previous < curren
        break
      swap(array, j, j + gap)
  return array

def swap(array, src, dest):
  if src == dest:
    return
  tmp = array[src]
  array[src] = array[dest]
  array[dest] = tmp
