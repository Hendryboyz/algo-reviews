OPENING = '('
def longestBalancedSubstring(string):
	longest_balanced_length = 0
	opening_count, closing_count = 0, 0
	for parathness in string:
		if parathness == OPENING:
			opening_count += 1
		else:
			closing_count += 1
		
		if opening_count == closing_count:
			longest_balanced_length = max(longest_balanced_length, opening_count + closing_count)
		elif opening_count < closing_count:
			opening_count, closing_count = 0, 0
			
	opening_count, closing_count = 0, 0
	for parathness in reversed(string):
		if parathness == OPENING:
			opening_count += 1
		else:
			closing_count += 1
			
		if opening_count == closing_count:
			longest_balanced_length = max(longest_balanced_length, opening_count + closing_count)
		elif opening_count > closing_count:
			opening_count, closing_count = 0, 0
	
	return longest_balanced_length
