def twoNumberSum(array, targetSum):
	remaining_table = {}
	for num in array:
		if num in remaining_table.keys():
			return [num, remaining_table[num]]
		else:
			remain = targetSum - num
			remaining_table[remain] = num
	return []
