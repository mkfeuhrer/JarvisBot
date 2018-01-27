import random
import math
from string import ascii_lowercase
import enchant
D = enchant.Dict("en_US")

def medium_bot(board):
	max_points = 0
	max_mov = (-1, -1, '#')
	for i in range(9):
		for j in range(9):
			if board[i][j] == '#':
				for k in ascii_lowercase:
					board[i][j] = k
					cur_points = get_points(i, j, board)
					if cur_points > max_points:
						max_mov = (i, j, k)
						max_points = cur_points
					board[i][j] = '#'
	return max_mov

# how many points will you get for (row, col) move
def get_points(row, col, board):
	ret = 0

	for i in range(0, col+1):
		for j in range(col, 9):
			s = ""
			for k in range(i, j+1):
				s += board[row][k]
			if (D.check(s) or D.check(s[::-1])) and len(s) > 1:
				# print(s)
				ret += len(s)

	for i in range(0, row+1):
		for j in range(row, 9):
			s = ""
			for k in range(i, j+1):
				s += board[k][col]
			if (D.check(s) or D.check(s[::-1])) and len(s) > 1:
				# print(s)
				ret += len(s)
	return ret