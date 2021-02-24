def riverSizes(matrix):
	height = len(matrix)
	width = len(matrix[0])
	is_visited = [False] * (height * width)
	result = []
	
	for row in range(height):
		for col in range(width):
			if unvisited_river_block(matrix, row, col, is_visited):
				river_size = measure_river(matrix, row, col, is_visited)
				result.append(river_size)
				
	return result

def unvisited_river_block(matrix, x, y, visited):
	width = len(matrix[0])
	return visited[x * width + y] == False and matrix[x][y] == 1

def measure_river(matrix, row, col, is_visited):
	tracker = [(row, col)]
	size = 0
	width = len(matrix[0])
	
	while len(tracker) > 0:
		x, y = tracker.pop()
		if out_of_matrix(matrix, x, y):
			continue
		if unvisited_river_block(matrix, x, y, is_visited) == False:
			continue
		size += 1
		is_visited[x * width + y] = True
		tracker.append((x + 1, y))
		tracker.append((x - 1, y))
		tracker.append((x, y + 1))
		tracker.append((x, y - 1))
		
	return size

def out_of_matrix(matrix, x, y):
	return x < 0 or len(matrix) <= x or y < 0 or len(matrix[0]) <= y
