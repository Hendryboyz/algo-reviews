OPENING = '('
def longestBalancedSubstring(string):
	match_parenthness = check_parenthness_matching(string)
	pair, max_pair = 0, 0
	for is_pair_parenthness in match_parenthness:
		if is_pair_parenthness:
			pair += 1
		else:
			max_pair = max(pair, max_pair)
			pair = 0
	return max(pair, max_pair)

def check_parenthness_matching(string):
	match_parenthness = [False for _ in range(len(string))]
	opening_stack = []
	for i, parenthness in enumerate(string):
		if parenthness == OPENING:
			opening_stack.append(i)
		elif len(opening_stack) > 0:
			match = opening_stack.pop()
			match_parenthness[i] = True
			match_parenthness[match] = True
	return match_parenthness
