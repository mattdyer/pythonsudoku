
import copy


#multiple solutions
puzzle3 = [
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

# one solution
puzzle2 = [
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

# simple puzzle
puzzle1 = [
	[1,2,3,4,5,6,7,8,9],
	[4,5,6,7,8,9,1,2,3],
	[7,8,9,1,2,3,4,5,6],
	[3,9,1,2,4,5,6,7,8],
	[6,7,8,3,9,1,2,0,5],
	[2,4,5,6,7,8,3,9,1],
	[5,1,2,8,3,4,9,6,7],
	[9,3,7,5,6,2,8,1,4],
	[8,6,0,0,0,0,5,3,2]
]

puzzle4 = [
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


#original_puzzle = copy.deepcopy(puzzle)

def convert_to_list(puzzle):
	
	puzzle_list = []
	
	for row in range(0, 9):
		for col in range(0, 9):
			value = puzzle[row][col]
			if value == 0:
				puzzle_list.append('')
			else:
				puzzle_list.append(str(value))
				
	return puzzle_list


def validateSet(set):
	
	validSet = True
	check = {}
	
	for num in range(1,10):
		check[str(num)] = 0
	
	for numbers in set:
		
		number = numbers
		
		if len(number) > 0:
			
			if check[number] > 0:
				validSet = False
			
			check[number] = check[number] + 1
	
	return validSet


def getRow(puzzle, number):
	
	row = []
	
	for num in range(0,9):
		index = num + ((number - 1) * 9)
	
		row.append(puzzle[index])
	
	return row


def getColumn(puzzle, number):
	col = []
	
	for num in range(0,9):
		col.append(puzzle[(num * 9) + (number - 1)])
	
	return col


def getBlock(puzzle, blockRow, blockCol):
	
	block = []
	
	for row in range(0,3):
		for col in range(0,3):
			
			index = ((row + (3 * (blockRow - 1))) * 9) + (col + (3 * (blockCol - 1)))
			
			block.append(puzzle[index])
	
	return block


def getIndex(row, col):
	return ((row * 9) + col)


def getValue(puzzle, row, col):
	return puzzle[getIndex(row, col)]


def validatePuzzle(puzzle):
	
	valid = True
	
	for num in range(1, 10):
		#print('column')
		valid = valid and validateSet(getColumn(puzzle, num))
	
	for num in range(1, 10):
		#print('row')
		valid = valid and validateSet(getRow(puzzle, num))
	
	for row in range(1, 4):
		for col in range(1, 4):
			#print('block')
			valid = valid and validateSet(getBlock(puzzle, row, col))
	
	return valid


def setValue(puzzle, row, col, value):
	puzzle[getIndex(row, col)] = value


def add_possible_values(puzzle):
	
	for row in range(0, 9):
		for col in range(0, 9):
			value = getValue(puzzle, row, col)
			if len(str(value)) != 1:
				setValue(puzzle, row, col, ','.join(get_possible_values(puzzle, row + 1, col + 1)))
		

def get_possible_values(puzzle, row, col):
	
	possible_values = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
	
	if len(str(getValue(puzzle, row - 1, col - 1))) > 0:
		possible_values = getValue(puzzle, row - 1, col - 1).split(',')
	
	#print(getRow(puzzle, row))
	
	for nums in getRow(puzzle, row):
		if len(str(nums)) == 1:
			try:
				possible_values.remove(str(nums))
			except ValueError:
				pass
	
	#print(getColumn(puzzle, col))
	
	for nums in getColumn(puzzle, col):
		if len(str(nums)) == 1:
			try:
				possible_values.remove(str(nums))
			except ValueError:
				pass
	
	blockCoordinates = get_block_coordinates(row, col)
	
	for nums in getBlock(puzzle, blockCoordinates[0], blockCoordinates[1]):
		if len(str(nums)) == 1:
			try:
				possible_values.remove(str(nums))
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
		
		rowList = []
		
		for col in range(0, 9):
			rowList.append(getValue(puzzle, row, col))
		
		print(rowList)


def test_solution(puzzle):
	finished = True
	
	for row in range(0, 9):
		for col in range(0, 9):
			
			value = getValue(puzzle, row, col)
			
			if len(value) > 1:
				finished = False
			if len(value) == 0:
				finished = False
	
	#print(finished)
	if finished:
		finished = finished and validatePuzzle(puzzle)
	
	#print(finished)
	
	return finished


def find_solutions(puzzle):
	
	#print('find_solution called')
	
	#printPuzzle(puzzle)
	
	solution_found = True
	
	for row in range(0, 9):
		for col in range(0, 9):
			possible_values = getValue(puzzle, row, col).split(',')
			
			#print(possible_values)
			
			if len(possible_values) != 1:
				
				for num in possible_values:
					new_puzzle = puzzle.copy()
					
					setValue(new_puzzle, row, col, num)
					
					#printPuzzle(new_puzzle)
					
					if(test_solution(new_puzzle)):
						print('solution found')
						printPuzzle(new_puzzle)
					
					add_possible_values(new_puzzle)
					
					find_solutions(new_puzzle)
				
			
def testGetFunctions(puzzle):
	
	for blockRow in range(1,4):
		for blockCol in range(1,4):
			print('block')
			print([blockRow, blockCol])
			print(getBlock(puzzle, blockRow, blockCol))
	
	for row in range(1, 10):
		print('row')
		print(row)
		print(getRow(puzzle, row))
	
	for col in range(1, 10):
		print('column')
		print(col)
		print(getColumn(puzzle, col))
	
	for row in range(0, 9):
		for col in range(0, 9):
			print([row, col])
			print(getValue(puzzle, row, col))
	

#for nums in getRow(puzzle, 1):
#	print(nums)


puzzle = convert_to_list(puzzle3)

#testGetFunctions(puzzle)

#print(validatePuzzle(puzzle))

#print(getBlock(puzzle, 2, 2))

#print(get_possible_values(puzzle, 9, 9))

if(validatePuzzle(puzzle)):
	add_possible_values(puzzle)

	printPuzzle(puzzle)

	find_solutions(puzzle)

#printPuzzle(original_puzzle)