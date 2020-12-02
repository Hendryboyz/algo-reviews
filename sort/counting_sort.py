def counting_sort(array, key_upper_bound):
  counting = counting_element(array, key_upper_bound)
  
  output = [None] * len(array)
  for i in range(len(array)):
    element = array[-1-i]
    true_index = counting[element] - 1
    counting[element] -= 1
    output[true_index] = element

  return output

def counting_element(array, key_upper_bound):
  counting = [0] * (key_upper_bound + 1)
  for i in array:
    counting[i] += 1
  for i in range(1, len(counting)):
    counting[i] += counting[i-1]
  return counting
