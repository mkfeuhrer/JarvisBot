import sys, os
sys.path.insert(0,os.getcwd())

import requests
import json
from typing import Any, Dict, List

'''
class currency(object):

	def usage(self) -> str:
		return "This plugin is a News App"

	def handle_message(self, message: Dict[str, str], bot_handler: Any) -> None:
		bot_response = self.get_currency_response(message, bot_handler)
		bot_handler.send_reply(message, bot_response)

handler_class = currency
'''

def get_currency_response(message: Dict[str, str]) -> str:
	content = message['content']
	words = content.split()
	res = requests.get('https://api.fixer.io/latest?base=' + words[2] + '&symbols=' + words[3] ).json()
	val = "1 " + words[2] + " = " + str(res['rates'][words[3]]) + " " + words[3] ;
	return val 