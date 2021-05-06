OPENING = '('
def longestBalancedSubstring(string):
	index_stack = [-1]
	longest_balanced_length = 0
	for index, parathness in enumerate(string):
		if parathness == OPENING:
			index_stack.append(index)
		else:
			index_stack.pop()
			if len(index_stack) > 0:
				current_balanced_length = index - index_stack[-1]
				longest_balanced_length = max(longest_balanced_length, current_balanced_length)
			else:
				index_stack.append(index)
	return longest_balanced_length
