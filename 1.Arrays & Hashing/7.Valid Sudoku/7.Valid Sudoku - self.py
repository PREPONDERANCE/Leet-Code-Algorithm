def isValidSudoku(board: list[list[str]]) -> bool:
	def isDigit(n):
		return n >= '0' and n <= '9'
	
	def containDuplicate(hashMap: dict):
		for num in hashMap.values():
			if num > 1: return True
		return False
	
	for i in range(9):
		rowMap, colMap = {}, {}
		for j in range(9):
			if isDigit(board[i][j]):
				rowMap[board[i][j]] = rowMap.get(board[i][j], 0) + 1
			if isDigit(board[j][i]):
				colMap[board[j][i]] = colMap.get(board[j][i], 0) + 1
		
		if containDuplicate(rowMap) or containDuplicate(colMap):
			return False
		
	for i in range(0, 9, 3):
		for j in range(0, 9, 3):
			submatrix = [row[j:j+3] for row in board[i:i+3]]
			hashMap = {}
			for p in range(3):
				for q in range(3):
					if isDigit(submatrix[p][q]):
						hashMap[submatrix[p][q]] = hashMap.get(submatrix[p][q], 0) + 1
			if containDuplicate(hashMap): return False
	
	return True

testBoard = [["8","3",".",".","7",".",".",".","."]
	,["6",".",".","1","9","5",".",".","."]
	,[".","9","8",".",".",".",".","6","."]
	,["8",".",".",".","6",".",".",".","3"]
	,["4",".",".","8",".","3",".",".","1"]
	,["7",".",".",".","2",".",".",".","6"]
	,[".","6",".",".",".",".","2","8","."]
	,[".",".",".","4","1","9",".",".","5"]
	,[".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(testBoard))