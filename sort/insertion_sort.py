def insertion_sort(array):
  for i in range(1, len(array)):
    current = array[i]
    j = i - 1
    previous = array[j]
    while j >= 0 and previous > current:
      array[j + 1] = previous
      j -= 1
      if j < 0: # python allow negative index in array but other languages not
        break
      previous = array[j]
    array[j + 1] = current
  return array