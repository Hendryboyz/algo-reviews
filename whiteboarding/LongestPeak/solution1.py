def longestPeak(array):
	longest_peak = 0
	cur_peak_length = 1
	find_peak = False
	for i in range(1, len(array) - 1):
		num = array[i]
		if find_peak:
			if array[i - 1] > num and num > array[i + 1]:
				cur_peak_length += 1
			else:
				find_peak = False
				longest_peak = max(longest_peak, cur_peak_length + 1)
				cur_peak_length = 1
		else:
			is_peak = num > array[i - 1] and num > array[i + 1]
			if is_peak:
				find_peak = True
				cur_peak_length += 1
			elif array[i - 1] < num and num < array[i + 1]:
				cur_peak_length += 1
			else:
				cur_peak_length = 1
	if find_peak:
		longest_peak = max(cur_peak_length + 1, longest_peak)
	return longest_peak