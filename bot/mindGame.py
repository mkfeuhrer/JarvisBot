import sys, os
sys.path.insert(0,os.getcwd())

import copy
import importlib
from math import log10, floor

import re
from converter import utils

from typing import Any, Dict, List
'''
class mindGame(object):
	def usage(self) -> str:
		return 'This plugin is a Mind game. Try your luck.'

	def handle_message(self, message: Dict[str, str], bot_handler: Any) -> None:
		bot_response = self.get_mindGame_response(message, bot_handler)
		bot_handler.send_reply(message, bot_response)
handler_class = mindGame
'''

def get_mindGame_response(message: Dict[str, str]) -> str:
	content = message['content']
	words = content.lower().split()
	original1 = "abdc"
	original2 = "egfh"
	original3 = "hgfe"
	original4 = "dabc"
	if words[2] == "start" :
		dup1 = "****"
		dup2 = "****"
		dup3 = "****"
		dup4 = "****"
		bot_handler.storage.put("dup1", dup1 )
		bot_handler.storage.put("dup2", dup2 )
		bot_handler.storage.put("dup3", dup3 )
		bot_handler.storage.put("dup4", dup4 )
		bot_handler.storage.put("prevx", "5" ) 
		bot_handler.storage.put("prevy", "5" ) 
		bot_handler.storage.put("total" , "0") 
		return "Game Starts, choose an x,y coordinate to unflip :\n" + dup1 + "\n" + dup2 + "\n" + dup3 + "\n" + dup4 ;
	else :
		dup1 = bot_handler.storage.get("dup1") 
		dup2 = bot_handler.storage.get("dup2")
		dup3 = bot_handler.storage.get("dup3")
		dup4 = bot_handler.storage.get("dup4")
		x = int(words[2])
		y = int(words[3]) 
		prevx = bot_handler.storage.get("prevx") ;
		prevy = bot_handler.storage.get("prevy") ;
		total = bot_handler.storage.get("total") ;
		if prevx == "5" :
			if x == 1 :
				dup1 = dup1[:y] + original1[y] + dup1[y+1:] 
			elif x == 2 :
				dup2 = dup2[:y] + original2[y] + dup2[y+1:] 
			elif x == 3 :
				dup3 = dup3[:y] + original3[y] + dup3[y+1:]
			else :
				dup4 = dup4[:y] + original4[y] + dup4[y+1:] 
			bot_handler.storage.put("prevx" , x ) 
			bot_handler.storage.put("prevy" , y ) 
		else :
			temp = ""
			temp1 = "" 
			if x == 1 :
				temp = original1[y] 
			elif x == 2 :
				temp = original2[y] 
			elif x == 3 :
				temp = original3[y]
			else :
				temp = original4[y] 
			if prevx == 1 :
				temp1 = original1[prevy] 
			elif prevx == 2 :
				temp1 = original2[prevy] 
			elif prevx == 3 :
				temp1 = original3[prevy]
			else :
				temp1 = original4[prevy] 
			if temp == temp1 :
				bot_handler.storage.put("prevx" , "5") 
				bot_handler.storage.put("prevy" , "5")
				temp2 = int(total)
				temp2 += 1 
				if temp2 == 8 :
					return "You Win"
				total = str(temp2)
				if x == 1 :
					dup1 = dup1[:y] + original1[y] + dup1[y+1:] 
				elif x == 2 :
					dup2 = dup2[:y] + original2[y] + dup2[y+1:]
				elif x == 3 :
					dup3 = dup3[:y] + original3[y] + dup3[y+1:]
				else :
					dup4 = dup4[:y] + original4[y] + dup4[y+1:] 
			else :
				bot_handler.storage.put("prevx" , "5") 
				bot_handler.storage.put("prevy" , "5")
				if prevx == 1 :
					dup1 = dup1[:prevy] + "*" + dup1[prevy+1:] 
				elif prevx == 2 :
					dup2 = dup2[:prevy] + "*" + dup2[prevy+1:] 
				elif prevx == 3 :
					dup3 = dup3[:prevy] + "*" + dup3[prevy+1:]
				else :
					dup4 = dup4[:prevy] + "*" + dup4[prevy+1:]
		bot_handler.storage.put("dup1" , dup1 )
		bot_handler.storage.put("dup2" , dup2 )
		bot_handler.storage.put("dup3" , dup3 )
		bot_handler.storage.put("dup4" , dup4 )
		bot_handler.storage.put("total" , total )
		return "New Formation :\n" + dup1 + "\n" + dup2 + "\n" + dup3 + "\n" + dup4 ;