# think the idea of bubble up

def bubble_sort(array):
  for i in range(len(array) - 1):
    is_swap = False
    for j in range(len(array) - 1 - i):
      if array[j] > array[j+1]:
        is_swap = True
        tmp = array[j]
        array[j] = array[j+1]
        array[j+1] = tmp

    if is_swap == False:
      break
  return array