import sys, os
sys.path.insert(0,os.getcwd())

import copy
import importlib
from math import log10, floor
from random_words import RandomWords
import re
from converter import utils

from typing import Any, Dict, List
'''
class hangman(object):
	def usage(self) -> str:
		return 'This plugin a hangman game. Guess the right name of movie to win.'

	def handle_message(self, message: Dict[str, str], bot_handler: Any) -> None:
		bot_response = self.get_response(message, bot_handler)
		bot_handler.send_reply(message, bot_response)
handler_class = hangman
'''

def get_response(message: Dict[str, str], bot_handler: Any) -> str:
	content = message['content']
	words = content.lower().split()
	if len(words) < 2:

		return "Invalid Input."

	elif words[2] == "start" :

		# chances = "6"
		# word = "avishek"
		chances = 5
		word = RandomWords().random_word()
		done = "".join(['#' for i in range(len(word))])
		# done = "*******"
		bot_handler.storage.put("word", word ) 
		bot_handler.storage.put("done" , done ) 
		bot_handler.storage.put("chances" , chances )
		return "Prediction String: " + done + "\nChances Left: " + str(chances)

	else :

		word = bot_handler.storage.get("word")
		done = bot_handler.storage.get("done") 
		chances = bot_handler.storage.get("chances")
		letter = words[2]
		i = 0 
		val = False 
		while i < len( word ) :
			if letter == word[i] and done[i] == "#" : 
				val = True
				done = done[:i] + word[i] + done[i+1:]
			i += 1
		if val == False :
			temp = int(chances)
			temp -= 1 
			chances = str(temp) 
		if chances == "0" :
			bot_handler.storage.put("word", word ) 
			bot_handler.storage.put("done" , done ) 
			bot_handler.storage.put("chances" , chances )
			return "You Lose :(\nString was: " + word 
		if done == word :
			bot_handler.storage.put("word", word ) 
			bot_handler.storage.put("done" , done ) 
			bot_handler.storage.put("chances" , chances )
			return "You Win :)"
		bot_handler.storage.put("word", word ) 
		bot_handler.storage.put("done" , done ) 
		bot_handler.storage.put("chances" , chances )
		return "Prediction String: " + done + "\nChances Left: " + str(chances)
