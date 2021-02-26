def moveElementToEnd(array, toMove):
	left, right = 0, len(array) - 1
	while left < right:
		if array[right] == toMove:
			right -= 1
			continue
		while array[left] != toMove and left < right:
			left += 1
		if left < right:
			swap(array, left, right)
	return array

def swap(array, src, dest):
	array[src], array[dest] = array[dest], array[src]