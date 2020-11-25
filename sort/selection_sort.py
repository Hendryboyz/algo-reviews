def selection_sort(array):
  for i in range(len(array)):
    smallest = i
    for j in range(i, len(array)):
      if array[j] < array[smallest]:
        smallest = j
    tmp = array[i]
    array[i] = array[smallest]
    array[smallest] = tmp
  return array
