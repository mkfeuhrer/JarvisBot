import copy
import importlib
import random
from math import log10, floor

import re
from zulip_bots.bots.converter import utils

from typing import Any, Dict, List

'''
class calculator(object):

	def usage(self) -> str:
		return 'This plugin is a Calculator.'
	def handle_message(self, message: Dict[str, str], bot_handler: Any) -> None:
		bot_response = self.get_calculator_response(message, bot_handler)
		bot_handler.send_reply(message, bot_response)

handler_class = calculator
'''

def get_calculator_response(message: Dict[str, str], bot_handler: Any) -> str:
	content = message['content']
	words = content.lower().split()
	if words[3] == "+" :
		temp = float(words[2]) 
		temp1 = float(words[4])
		temp = temp + temp1 
		return str( temp ) 
	elif words[3] == "-" :
		temp = float(words[2]) 
		temp1 = float(words[4])
		temp = temp - temp1 
		return str( temp )
	elif words[3] == "*" :
		temp = float(words[2]) 
		temp1 = float(words[4])
		temp = temp * temp1 
		return str( temp )
	elif words[3] == "/" :
		if words[4] == "0":
			return "Division by zero."
		temp = float(words[2]) 
		temp1 = float(words[4])
		temp = temp / temp1 
		return str( temp )
	else :
		return "Under Construction"