def insertion_sort(array):
  for j in range(1, len(array)):
    current = array[j]
    i = j - 1
    previous = array[i]
    while i >= 0 and previous > current:
      array[i + 1] = previous
      i = i - 1
      previous = array[i]
    array[i + 1] = current