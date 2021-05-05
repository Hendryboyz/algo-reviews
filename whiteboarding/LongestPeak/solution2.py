def longestPeak(array):
	index = 1
	longest_peak = 0
	last_index = len(array) - 1
	while index < last_index:
		is_tip = array[index - 1] < array[index] and array[index] > array[index + 1]
		if not is_tip:
			index += 1
			continue
		left, right = index - 1, index + 1
		while left > 0 and array[left - 1] < array[left]:
			left -= 1
		while right < last_index and array[right + 1] < array[right]:
			right += 1
		peak_length = right - left + 1
		longest_peak = max(longest_peak, peak_length)
		index = right + 1
	return longest_peak
  