

# simple solution
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


numbers = {
	0:int('000000000', 2),
	1:int('100000000', 2),
	2:int('010000000', 2),
	3:int('001000000', 2),
	4:int('000100000', 2),
	5:int('000010000', 2),
	6:int('000001000', 2),
	7:int('000000100', 2),
	8:int('000000010', 2),
	9:int('000000001', 2)
}

number_check = {
	int('000000000', 2):0,
	int('100000000', 2):1,
	int('010000000', 2):2,
	int('001000000', 2):3,
	int('000100000', 2):4,
	int('000010000', 2):5,
	int('000001000', 2):6,
	int('000000100', 2):7,
	int('000000010', 2):8,
	int('000000001', 2):9
}

#print(number_check)

#bits = int('111100001', 2) 

#new_bits = bits & ~numbers[4]

#new_bits = new_bits & ~numbers[4]

#expected_bits = int('111000001', 2)

#print("{0:b}".format(bits))
#print("{0:b}".format(new_bits))
#print("{0:b}".format(expected_bits))

#print('bits')

def convert_to_bits(puzzle):
	
	new_puzzle = []
	
	for row in range(0, 9):
		for col in range(0, 9):
			value = puzzle[row][col]
			
			new_puzzle.append(numbers[value])
	
	return new_puzzle

def validateSet(set):
	
	validSet = True
	check = {}
	
	for num in range(1,10):
		check[num] = 0
	
	for number in set:
		
		if number in number_check and number != 0:
			if check[number_check[number]] > 0:
				validSet = False
			
			check[number_check[number]] = check[number_check[number]] + 1
	
	return validSet


# def has_one_bit_set(number):
	
# 	has_bit_set = false
	
# 	for num in range(1,10):
# 		has_set = has_set and number == numbers[num]
	
# 	return has_bit_set




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
			value = getValue(puzzle, row, col)
			if value in number_check:
				rowList.append(number_check[value])
			else:
				rowList.append("{0:b}".format(value))
		
		print(rowList)

def getIndex(row, col):
	return ((row * 9) + col)

def getValue(puzzle, row, col):
	return puzzle[getIndex(row, col)]

def setValue(puzzle, row, col, value):
	puzzle[getIndex(row, col)] = value

def validatePuzzle(puzzle):
	
	valid = True
	
	for num in range(1, 10):
		#print('column')
		valid = valid and validateSet(getColumn(puzzle, num))
	
	if valid:
		for num in range(1, 10):
			#print('row')
			valid = valid and validateSet(getRow(puzzle, num))
	
	if valid:
		for row in range(1, 4):
			for col in range(1, 4):
				#print('block')
				valid = valid and validateSet(getBlock(puzzle, row, col))
	
	return valid

def add_possible_values(puzzle):
	
	for row in range(0, 9):
		for col in range(0, 9):
			value = getValue(puzzle, row, col)
			if not (value in number_check) or value == 0:
				setValue(puzzle, row, col, get_possible_values(puzzle, row + 1, col + 1))


def get_possible_values(puzzle, row, col):
	
	possible_values = int('111111111', 2)
	
	if not (getValue(puzzle, row - 1, col - 1) in number_check):
		possible_values = getValue(puzzle, row - 1, col - 1)
	
	#print(getRow(puzzle, row))
	
	for nums in getRow(puzzle, row):
		if nums in number_check:
			possible_values = possible_values & ~nums
	
	#print(getColumn(puzzle, col))
	
	if not (possible_values in number_check):
		for nums in getColumn(puzzle, col):
			if nums in number_check:
				possible_values = possible_values & ~nums
	
	if not (possible_values in number_check):
		blockCoordinates = get_block_coordinates(row, col)
		
		for nums in getBlock(puzzle, blockCoordinates[0], blockCoordinates[1]):
			if nums in number_check:
				possible_values = possible_values & ~nums
	
	return possible_values

def find_solutions(puzzle):
	
	#print('find_solution called')
	
	#printPuzzle(puzzle)
	
	solution_found = True
	
	for row in range(0, 9):
		for col in range(0, 9):
			possible_values = getValue(puzzle, row, col)
			
			#print(possible_values)
			#print(possible_values in number_check)
			
			if not (possible_values in number_check):
				
				for num in number_check:
					if num & possible_values > 0:
						
						new_puzzle = puzzle.copy()
						
						setValue(new_puzzle, row, col, num)
						
						#printPuzzle(new_puzzle)
						
						if(test_solution(new_puzzle)):
							print('solution found')
							printPuzzle(new_puzzle)
						
						add_possible_values(new_puzzle)
						
						find_solutions(new_puzzle)


def test_solution(puzzle):
	finished = True
	
	for row in range(0, 9):
		for col in range(0, 9):
			
			value = getValue(puzzle, row, col)
			
			if not (value in number_check):
				finished = False
	
	if finished:
		finished = finished and validatePuzzle(puzzle)
	
	return finished	

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


puzzle = convert_to_bits(puzzle4)

#print("{0:b}".format(numbers[9]))

printPuzzle(puzzle)

#testGetFunctions(puzzle)

if(validatePuzzle(puzzle)):
	add_possible_values(puzzle)
	
	print('with values')
	printPuzzle(puzzle)
	
	find_solutions(puzzle)