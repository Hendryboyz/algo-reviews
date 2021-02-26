def moveElementToEnd(array, toMove):
	left, right = 0, len(array) - 1
	while left < right:
		while left < right:
			if array[right] != toMove:
				break
			right -= 1
		if array[left] == toMove:
			swap(array, left, right)
		left += 1
	return array

def swap(array, left, right):
	array[left], array[right] = array[right], array[left]