
import copy

puzzle = [
	[1,0,0,0,0,0,0,0,0],
	[0,2,0,0,0,0,0,0,0],
	[0,0,3,0,0,0,0,0,0],
	[0,0,0,4,0,0,0,0,0],
	[0,0,0,0,5,0,0,0,0],
	[0,0,0,0,0,6,0,0,0],
	[0,0,0,0,0,0,7,0,0],
	[0,0,0,0,0,0,0,8,0],
	[0,0,0,0,0,0,0,0,9]
]


# one solution
puzzle = [
	[1,2,3,0,0,6,7,8,9],
	[4,5,6,7,8,0,1,2,3],
	[7,8,9,1,2,3,4,5,6],
	[3,9,1,0,4,5,6,7,8],
	[6,7,8,3,9,1,2,0,5],
	[2,4,0,0,0,0,0,9,1],
	[5,0,0,8,3,4,0,0,7],
	[9,3,0,0,6,0,8,1,4],
	[8,6,0,0,0,0,5,3,2]
]


#multiple solutions
puzzle = [
	[1,2,3,0,0,6,7,8,9],
	[4,5,6,7,8,0,1,2,3],
	[7,8,0,0,2,3,4,5,6],
	[0,9,1,0,4,5,6,7,8],
	[0,0,0,3,9,1,2,0,5],
	[0,4,0,0,0,0,0,9,1],
	[0,0,0,8,3,4,0,0,7],
	[9,3,0,0,6,0,8,1,4],
	[8,6,0,0,0,0,5,3,2]
]



original_puzzle = copy.deepcopy(puzzle)

def convert_to_lists(puzzle):
	for row in range(0, 9):
		for col in range(0, 9):
			value = puzzle[row][col]
			if value == 0:
				puzzle[row][col] = []
			else:
				puzzle[row][col] = [value]


def validateSet(set):
	
	validSet = True
	check = {}
	
	for num in range(1,10):
		check[num] = 0
	
	for numbers in set:
		
		if len(numbers) == 1:
			number = numbers[0]
		else:
			number = 0
		
		if number > 0:
			
			if check[number] > 0:
				validSet = False
			
			check[number] = check[number] + 1
	
	return validSet


def getRow(puzzle, number):
	return puzzle[number - 1]


def getColumn(puzzle, number):
	col = []
	
	for row in puzzle:
		col.append(row[number - 1])
	
	return col


def getBlock(puzzle, blockRow, blockCol):
	
	block = []
	
	for row in range(0,3):
		for col in range(0,3):
			block.append(puzzle[row + (3 * (blockRow - 1))][col + (3 * (blockCol - 1))])
	
	return block;


def validatePuzzle(puzzle):
	
	valid = True
	
	for num in range(1, 10):
		valid = valid and validateSet(getColumn(puzzle, num))
	
	for num in range(1, 10):
		valid = valid and validateSet(getRow(puzzle, num))
	
	for row in range(0, 3):
		for col in range(0, 3):
			valid = valid and validateSet(getBlock(puzzle, row, col))
	
	return valid

def add_possible_values(puzzle):
	
	for row in range(0, 9):
		for col in range(0, 9):
			value = puzzle[row][col]
			if len(value) != 1:
				puzzle[row][col] = get_possible_values(puzzle, row + 1, col + 1)
		

def get_possible_values(puzzle, row, col):
	
	possible_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	
	if len(puzzle[row - 1][col - 1]) > 0:
		possible_values = puzzle[row - 1][col - 1].copy()
	
	#print(getRow(puzzle, row))
	
	for nums in getRow(puzzle, row):
		if len(nums) == 1:
			try:
				possible_values.remove(nums[0])
			except ValueError:
				pass
	
	#print(getColumn(puzzle, col))
	
	for nums in getColumn(puzzle, col):
		if len(nums) == 1:
			try:
				possible_values.remove(nums[0])
			except ValueError:
				pass
	
	blockCoordinates = get_block_coordinates(row, col)
	
	for nums in getBlock(puzzle, blockCoordinates[0], blockCoordinates[1]):
		if len(nums) == 1:
			try:
				possible_values.remove(nums[0])
			except ValueError:
				pass
	
	return possible_values;

def get_block_coordinates(row, col):
	
	blockRow = convert_coordinate(row)
	blockCol = convert_coordinate(col)
	
	return [blockRow, blockCol]

def convert_coordinate(coor):
	
	blockCoor = 0
	
	if(coor == 1 or coor == 2 or coor == 3):
		blockCoor = 1
	
	if(coor == 4 or coor == 5 or coor == 6):
		blockCoor = 2
	
	if(coor == 7 or coor == 8 or coor == 9):
		blockCoor = 3
	
	return blockCoor

def printPuzzle(puzzle):
	for row in range(0, 9):
		print(puzzle[row])


def test_solution(puzzle):
	finished = True
	
	for row in range(0, 9):
		for col in range(0, 9):
			if len(puzzle[row][col]) > 1:
				finished = False
			if len(puzzle[row][col]) == 0:
				finished = False
	
	#print(finished)
	
	finished = finished and validatePuzzle(puzzle)
	
	#print(finished)
	
	return finished


def find_solutions(puzzle):
	
	#print('find_solution called')
	
	#printPuzzle(puzzle)
	
	solution_found = True
	
	for row in range(0, 9):
		for col in range(0, 9):
			possible_values = puzzle[row][col]
			
			#print(possible_values)
			
			if len(possible_values) != 1:
				
				for num in possible_values:
					new_puzzle = copy.deepcopy(puzzle)
					new_puzzle[row][col] = [num]
					
					#printPuzzle(new_puzzle)
					
					if(test_solution(new_puzzle)):
						print('solution found')
						printPuzzle(new_puzzle)
					
					add_possible_values(new_puzzle)
					
					find_solutions(new_puzzle)
				
			
	
	

#for nums in getRow(puzzle, 1):
#	print(nums)


convert_to_lists(puzzle)

#print(validatePuzzle(puzzle))

#print(getBlock(puzzle, 2, 2))

#print(get_possible_values(puzzle, 9, 9))

if(validatePuzzle(puzzle)):
	add_possible_values(puzzle)

	#printPuzzle(puzzle)

	
	find_solutions(puzzle)

printPuzzle(original_puzzle)