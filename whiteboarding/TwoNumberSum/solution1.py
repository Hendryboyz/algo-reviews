def twoNumberSum(array, targetSum):
	arr_size = len(array)
	for i in range(arr_size - 1):
		for j in range(i + 1, arr_size):
			if array[i] + array[j] == targetSum:
				return [array[i], array[j]]
	return []
  