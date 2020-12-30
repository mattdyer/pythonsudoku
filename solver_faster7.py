

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

# two solutions
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


#['1', '2', '3', '4', '9', '5', '8', '6', '7']
#['8', '5', '9', '6', '7', '1', '4', '2', '3']
#['9', '7', '4', '3', '8', '2', '1', '5', '1']
#['4', '9', '5', '1', '6', '3', '5', '7', '2']
#['3', '8', '2', '9', '4', '7', '5', '1', '6']
#['6', '3', '1', '5', '2', '8', '9', '7', '4']
#['3', '9', '6', '2', '1', '4', '7', '8', '5']
#['5', '4', '8', '7', '3', '9', '2', '6', '1']
#['2', '1', '7', '8', '5', '6', '3', '4', '9']

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


solutions = {}

paths_checked = {}


def convert_to_bits(puzzle):
	
	new_puzzle = []
	
	for row in range(0, 9):
		for col in range(0, 9):
			value = puzzle[row][col]
			
			new_puzzle.append(numbers[value])
	
	return new_puzzle

def validate_set(set):
	
	valid_set = True
	
	counts = {}
	
	for num in set['set']:
		try:
			
			# if num not in number_check:
			# 	set['valid'] = False
			# 	valid_set = False
			# 	break
			
			counts[num] = counts[num] + 1
			
			if counts[num] > 1 and num != 0 and num in number_check:
				set['valid'] = False
				valid_set = False
				break
			
		except Exception as e:
			counts[num] = 1
	
	
	# for num in range(1,10):
	# 	if set.count(num) > 1:
	# 		valid_set = False
	# 		if not valid_set:
	# 			break
			
	
	return valid_set



def get_row(puzzle, number):
	
	row = {}
	
	row['set'] = []
	row['valid'] = True
	
	counts = {}
	
	for num in range(0,9):
		index = num + ((number - 1) * 9)
		
		value = puzzle[index]
		
		add_value_to_set(row, counts, value)
		
	
	return row


def get_column(puzzle, number):
	
	col = {}
	
	col['set'] = []
	col['valid'] = True
	
	counts = {}
	
	for num in range(0,9):
		index = (num * 9) + (number - 1)
		value = puzzle[index]
		
		add_value_to_set(col, counts, value)
	
	return col


def get_block(puzzle, blockRow, blockCol):
	
	block = {}
	
	block['set'] = []
	block['valid'] = True
	
	counts = {}
	
	for row in range(0,3):
		for col in range(0,3):
			
			index = ((row + (3 * (blockRow - 1))) * 9) + (col + (3 * (blockCol - 1)))
			
			value = puzzle[index]
			
			add_value_to_set(block, counts, value)
	
	return block

def add_value_to_set(set, counts, value):
	set['set'].append(value)
	
	# try:
	# 	counts[value] = counts[value] + 1
		
	# 	if is_count_too_high(value, counts):
	# 		set['valid'] = False
		
	# except Exception as e:
	# 	counts[value] = 1
	

def is_count_too_high(value, counts):
	return  counts[value] > 1 and value != 0 and value in number_check
		

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

def print_puzzle(puzzle):
	for row in range(0, 9):
		
		rowList = []
		
		for col in range(0, 9):
			value = get_value(puzzle, row, col)
			if value in number_check:
				#rowList.append(number_check[value])
				rowList.append("{:<9}".format(number_check[value]))
			else:
				#rowList.append(0)
				formattedValue = "{0:b}".format(value)
				formattedValue = "{:<9}".format(formattedValue)
				rowList.append(formattedValue)
		
		print(rowList)

def get_index(row, col):
	return (row * 9) + col

def get_value(puzzle, row, col):
	return puzzle[get_index(row, col)]

def set_value(puzzle, row, col, value):
	puzzle[get_index(row, col)] = value

def validate_puzzle(puzzle):
	
	valid = True
	
	for num in range(1, 10):
		#print('column')
		valid = valid and validate_set(get_column(puzzle, num))
		if not valid:
			break
	
	if valid:
		for num in range(1, 10):
			#print('row')
			valid = valid and validate_set(get_row(puzzle, num))
			if not valid:
				break
	
	if valid:
		for row in range(1, 4):
			for col in range(1, 4):
				#print('block')
				valid = valid and validate_set(get_block(puzzle, row, col))
				if not valid:
					break
			if not valid:
				break
	
	return valid

def add_possible_values(puzzle):
	
	for row in range(0, 9):
		for col in range(0, 9):
			value = get_value(puzzle, row, col)
			if not (value in number_check) or value == 0:
				set_value(puzzle, row, col, get_possible_values(puzzle, row + 1, col + 1))


def get_possible_values(puzzle, row, col):
	
	possible_values = int('111111111', 2)
	
	if not (get_value(puzzle, row - 1, col - 1) in number_check):
		possible_values = get_value(puzzle, row - 1, col - 1)
	
	if possible_values == 0:
		raise_no_values(row, col)
	
	#print(get_row(puzzle, row))
	
	for nums in get_row(puzzle, row)['set']:
		if nums in number_check:
			possible_values = possible_values & ~nums
			if possible_values == 0:
				raise_no_values(row, col)
	
	#print(get_column(puzzle, col))
	
	if not possible_values == 0:
		if not (possible_values in number_check):
			for nums in get_column(puzzle, col)['set']:
				if nums in number_check:
					possible_values = possible_values & ~nums
					if possible_values == 0:
						raise_no_values(row, col)
	
	if not possible_values == 0:
		if not (possible_values in number_check):
			blockCoordinates = get_block_coordinates(row, col)
			
			for nums in get_block(puzzle, blockCoordinates[0], blockCoordinates[1])['set']:
				if nums in number_check:
					possible_values = possible_values & ~nums
					if possible_values == 0:
						raise_no_values(row, col)
	
	if possible_values == 0:
		raise_no_values(row, col)
	
	return possible_values

def raise_no_values(row, col):
	raise Exception('no possible values for ' + str(row) + ' ' + str(col))

def find_solutions(puzzle, call_count, row, col):
	
	#print('-------------- top ----------------')
	#print_puzzle(puzzle)
	#print('-------------- bottom ----------------')
	
	puzzle_as_string = puzzle_to_string(puzzle)
	
	paths_checked[puzzle_as_string] = 1
	
	call_count = call_count + 1
	
	#if call_count % 30 == 0:
	#	print('find solutions called')
	#	print_puzzle(puzzle)
	#	print(call_count)
	
	
	new_row = row
	new_col = col + 1
	
	if(new_col > 8):
		new_row = row + 1
		new_col = 0
	
	possible_values = get_value(puzzle, row, col)
	
	if not (possible_values in number_check):
		
		for num in number_check:
			if num & possible_values > 0:
				
				original_value = get_value(puzzle, row, col)
				
				#new_puzzle = puzzle.copy()
				
				set_value(puzzle, row, col, num)
				
				block_coords = get_block_coordinates(row, col)
				
				if validate_set(get_row(puzzle, row)) and validate_set(get_column(puzzle, col)) and validate_set(get_block(puzzle, block_coords[0], block_coords[1])):
					
					new_puzzle = puzzle.copy()
					
					try:
						add_possible_values(new_puzzle)
						
						if(test_solution(new_puzzle)):
							solutions[puzzle_to_string(new_puzzle)] = 1
							
							print_solution(new_puzzle, call_count)
						else:
							if(not puzzle_to_string(new_puzzle) in paths_checked and new_row < 9 and new_col < 9):
								find_solutions(new_puzzle, call_count, new_row, new_col)
								
					except Exception as e:
						e
						#print_puzzle(new_puzzle)
						#print(e)
				
				set_value(puzzle, row, col, original_value)
		
	if(new_row < 9 and new_col < 9):
		find_solutions(puzzle, call_count, new_row, new_col)

		
def print_solution(puzzle, call_count):
	print('------------------------------------------------------')
	print('----------------- solution found ---------------------')
	print('------------------------------------------------------')
	print_puzzle(puzzle)
	print(call_count)
	print(solutions)

						
def puzzle_to_string(puzzle):
	
	solution_as_string = ""
	
	for row in range(0, 9):
		
		for col in range(0, 9):
			value = get_value(puzzle, row, col)
			
			solution_as_string = solution_as_string + str(value)
			
	return solution_as_string	
	
		
						
						

def test_solution(puzzle):
	
	finished = True
	
	for row in range(0, 9):
		for col in range(0, 9):
			
			value = get_value(puzzle, row, col)
			
			if not (value in number_check) or value == 0:
				finished = False
				break
		
		if not finished:
			break
	
	if finished:
		finished = finished and validate_puzzle(puzzle)
	
	return finished	

def test_get_functions(puzzle):
	
	for blockRow in range(1,4):
		for blockCol in range(1,4):
			print('block')
			print([blockRow, blockCol])
			print(get_block(puzzle, blockRow, blockCol))
	
	for row in range(1, 10):
		print('row')
		print(row)
		print(get_row(puzzle, row))
	
	for col in range(1, 10):
		print('column')
		print(col)
		print(get_column(puzzle, col))
	
	for row in range(0, 9):
		for col in range(0, 9):
			print([row, col])
			print(get_value(puzzle, row, col))


puzzle = convert_to_bits(puzzle4)

print_puzzle(puzzle)

#test_get_functions(puzzle)

if(validate_puzzle(puzzle)):
	add_possible_values(puzzle)
	
	print('with values')
	print_puzzle(puzzle)
	
	find_solutions(puzzle, 1, 0, 0)

