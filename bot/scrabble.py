import sys, os
sys.path.insert(0,os.getcwd())

# dictionay to check valid words
import enchant
D = enchant.Dict("en_US")

# code for bot ai
import ai

# implementation class
'''
class ScrabbleBotHandler(object):
	
	def usage(scrabble):
		return 'bot for playing scrabble'

	def handle_message(scrabble, message, bot_handler):
		response = get_response(message, bot_handler)		
		bot_handler.send_reply(message, response)

handler_class = ScrabbleBotHandler
'''

def get_response(message):
	data = message['content'].split()
	if len(data) == 3:

		if(data[2] == "start"):

			bot_handler.storage.put("his_points", "0")
			bot_handler.storage.put("bot_points", "0")
			board = [['#' for i in range(9)] for j in range(9)]
			board_str = show_board(board)
			bot_handler.storage.put("board", board_str)
			bot_handler.storage.put("game_on", "true")
			return board_str + show_points(0, 0)

		else:

			return "Invalid Input."

	elif len(data) == 5:

		if bot_handler.storage.get("game_on") != "true":

			return "No Paused Game!"

		row = int(data[2])
		col = int(data[3])
		c = data[4][0].lower()
		his_points = int(bot_handler.storage.get("his_points"))
		bot_points = int(bot_handler.storage.get("bot_points"))
		board_str = bot_handler.storage.get("board")
		board = get_board(board_str)

		if valid_move(row, col, c):

			board[row][col] = c
			his_points += get_points(row, col, board)
			board_str = show_board(board)
			ret = game_result(board, his_points, bot_points)

			if ret != "":

				bot_handler.storage.put("game_on", "false")
				return ret

			x, y, z = ai.medium_bot(board)
			ret = ""

			if x != -1:

				board[x][y] = z
				# print ("board x,y=", board[x][y])
				bot_points += get_points(x, y, board)
				ret = "Bot Moves " + z + " At (" + str(x) + ", " + str(y) + ")\n"
				board_str = show_board(board)

			bot_handler.storage.put("board", board_str)
			bot_handler.storage.put("his_points", his_points)
			bot_handler.storage.put("bot_points", bot_points)
			ret += board_str+show_points(his_points, bot_points)
			return ret

		else:

			return "Invalid Input."
	else:

		return "Invalid Input."
		

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

# check if a (row, col, c) move is valid
def valid_move(row, col, c):
	if row < 0 or row >= 9:

		return False

	if col < 0 or col >= 9:

		return False

	if (c <= '0' or c >= 'z') and board[row][col] == '#':

		return False

	return True

# parse board from string
def get_board(board_str):
	board = []
	i = 0

	for row_str in board_str.split("\n"):

		if i > 0:
			board.append(row_str.split(" ")[1:])
		i += 1

	return board

# parse board to string
def show_board(board):
	ret = "0 "

	for i in range(9):

		ret += str(i) + " "

	ret += "\n"

	for i in range(9):

		ret += str(i) + " "
		for j in range(9):

			ret += board[i][j] + " "

		ret += "\n"

	return ret

# show points of user and bot
def show_points(his_points, bot_points):
	ret = ""
	ret += "Your Points: " + str(his_points)
	ret += "\tBot Points: " + str(bot_points)
	return ret

# check result of game
def game_result(board, his_points, bot_points):
	for i in range(9):
		for j in range(9):

			if board[i][j] == '#':

				return ""

	if his_points > bot_points:

		return "You Win :)"

	elif bot_points > his_points:

		return "Bot Wins :("

	else:

		return "It's a Draw :|"