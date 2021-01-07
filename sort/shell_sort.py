def shell_sort(array):
  for gap in compute_gap_sequences(len(array)):
    insertion_sort_with_gap(array, gap)
  return array

def compute_gap_sequences(length_of_array):
  # https://dl.acm.org/doi/10.1145/366552.366557
  k = 1
  sequences = []
  while True:
    current = pow(2, k) - 1
    if current < length_of_array:
      sequences.append(current)
      k += 1
    else:
      break
  return reversed(sequences)

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
