puzzle = [x for x in range(0, 81)]

print(puzzle)

def get_block(puzzle, blockRow, blockCol):
	
	indexes = []
	
	for row in range(0,3):
		for col in range(0,3):
			
			indexes.append(((row + (3 * (blockRow - 1))) * 9) + (col + (3 * (blockCol - 1))))
			
			
	
	print(indexes)
	

for row in range(1,4):
	for col in range(1,4):
		
		print('----------')
		print(row)
		print(col)
		print('----------')
		
		get_block(puzzle, row, col)