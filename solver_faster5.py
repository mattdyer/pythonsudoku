

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

#very difficult
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

#all zeros
puzzle5 = [
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0]
]


#hard puzzle example
puzzle6 = [
	[0,2,0,0,0,0,0,0,0],
	[0,0,0,6,0,0,0,0,3],
	[0,7,4,0,8,0,0,0,0],
	[0,0,0,0,0,3,0,0,2],
	[0,8,0,0,4,0,0,1,0],
	[6,0,0,5,0,0,0,0,0],
	[0,0,0,0,1,0,7,8,0],
	[5,0,0,0,0,9,0,0,0],
	[0,0,0,0,0,0,0,4,0]
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


call_counts = {
	'find_solutions': 0,
	'test_solution': 0,
	'validatePuzzle': 0,
	'validateSet': 0
}


def convert_to_bits(puzzle):
	
	new_puzzle = []
	
	for row in range(0, 9):
		for col in range(0, 9):
			value = puzzle[row][col]
			
			new_puzzle.append(numbers[value])
	
	return new_puzzle

def validateSet(set, call_counts):
	
	call_counts['validateSet'] = call_counts['validateSet'] + 1
	
	valid_set = True
	
	for num in range(1,10):
		if set.count(num) > 1:
			valid_set = False
			if not valid_set:
				break
	
	# validSet = True
	
	# check = {}
	
	# for num in range(1,10):
	# 	check[num] = 0
	
	# for number in set:
		
	# 	if number in number_check and number != 0:
			
	# 		if check[number_check[number]] > 0:
	# 			validSet = False
	# 			if not validSet:
	# 				break
			
	# 		check[number_check[number]] = check[number_check[number]] + 1
			
	
	return valid_set



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
				#rowList.append(number_check[value])
				rowList.append("{:<9}".format(number_check[value]))
			else:
				#rowList.append(0)
				formattedValue = "{0:b}".format(value)
				formattedValue = "{:<9}".format(formattedValue)
				rowList.append(formattedValue)
		
		print(rowList)

def getIndex(row, col):
	return ((row * 9) + col)

def getValue(puzzle, row, col):
	return puzzle[getIndex(row, col)]

def setValue(puzzle, row, col, value):
	puzzle[getIndex(row, col)] = value

def validatePuzzle(puzzle, call_counts):
	
	call_counts['validatePuzzle'] = call_counts['validatePuzzle'] + 1
	
	valid = True
	
	for num in range(1, 10):
		#print('column')
		valid = valid and validateSet(getColumn(puzzle, num), call_counts)
		if not valid:
			break
	
	if valid:
		for num in range(1, 10):
			#print('row')
			valid = valid and validateSet(getRow(puzzle, num), call_counts)
			if not valid:
				break
	
	if valid:
		for row in range(1, 4):
			for col in range(1, 4):
				#print('block')
				valid = valid and validateSet(getBlock(puzzle, row, col), call_counts)
				if not valid:
					break
			if not valid:
				break
	
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
			if possible_values == 0:
				break
	
	#print(getColumn(puzzle, col))
	
	if not possible_values == 0:
		if not (possible_values in number_check):
			for nums in getColumn(puzzle, col):
				if nums in number_check:
					possible_values = possible_values & ~nums
					if possible_values == 0:
						break
	
	if not possible_values == 0:
		if not (possible_values in number_check):
			blockCoordinates = get_block_coordinates(row, col)
			
			for nums in getBlock(puzzle, blockCoordinates[0], blockCoordinates[1]):
				if nums in number_check:
					possible_values = possible_values & ~nums
					if possible_values == 0:
						break
	
	if possible_values == 0:
		raise Exception('no possible values for ' + str(row) + ' ' + str(col))
	
	return possible_values

def find_solutions(puzzle, call_counts):
	
	if call_counts['find_solutions'] % 1000 == 0:
		print('find solutions called')
		printPuzzle(puzzle)
		print(call_counts)
	
	
	call_counts['find_solutions'] = call_counts['find_solutions'] + 1
	
	
	for row in range(0, 9):
		for col in range(0, 9):
			possible_values = getValue(puzzle, row, col)
			
			if not (possible_values in number_check):
				
				for num in number_check:
					if num & possible_values > 0:
						
						original_value = getValue(puzzle, row, col)
						
						#new_puzzle = puzzle.copy()
						
						setValue(puzzle, row, col, num)
						
						block_coords = get_block_coordinates(row, col)
						
						if validateSet(getRow(puzzle, row), call_counts) and validateSet(getColumn(puzzle, col), call_counts) and validateSet(getBlock(puzzle, block_coords[0], block_coords[1]), call_counts):
							
							new_puzzle = puzzle.copy()
							
							try:
								add_possible_values(new_puzzle)
								
								if(test_solution(new_puzzle, call_counts)):
									print('------------------------------------------------------')
									print('----------------- solution found ---------------------')
									print('------------------------------------------------------')
									printPuzzle(new_puzzle)
									print(call_counts)
								else:
									find_solutions(new_puzzle, call_counts)
							except Exception as e:
								e
								#print(e)
						
						setValue(puzzle, row, col, original_value)
				
						
						
						

def test_solution(puzzle, call_counts):
	
	call_counts['test_solution'] = call_counts['test_solution'] + 1
	
	
	finished = True
	
	for row in range(0, 9):
		for col in range(0, 9):
			
			value = getValue(puzzle, row, col)
			
			if not (value in number_check) or value == 0:
				finished = False
				break
		
		if not finished:
			break
	
	if finished:
		finished = finished and validatePuzzle(puzzle, call_counts)
	
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


puzzle = convert_to_bits(puzzle6)

printPuzzle(puzzle)

#testGetFunctions(puzzle)

if(validatePuzzle(puzzle, call_counts)):
	add_possible_values(puzzle)
	
	print('with values')
	printPuzzle(puzzle)
	
	find_solutions(puzzle, call_counts)
