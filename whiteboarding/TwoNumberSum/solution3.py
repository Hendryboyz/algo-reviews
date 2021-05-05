def twoNumberSum(array, targetSum):
	array.sort()
	left = 0
	right = len(array) - 1
	while left < right:
		sum = array[left] + array[right]
		if sum > targetSum:
			right -= 1
		elif sum < targetSum:
			left += 1
		else:
			return [array[left], array[right]]
	return []
