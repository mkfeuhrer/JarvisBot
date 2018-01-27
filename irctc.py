from zulip_bots.bots.irctc import pnrapi
from zulip_bots.bots.converter import utils

from typing import Any, Dict, List

class irctc(object):

	def usage(self) -> str:
		return '''This plugin is for Fetching IRCTC Details'''

	def handle_message(self, message: Dict[str, str], bot_handler: Any) -> None:
		bot_response = self.get_irctc_response(message, bot_handler)
		bot_handler.send_reply(message, bot_response)

	def get_irctc_response(self, message: Dict[str, str], bot_handler: Any) -> str:
		content = message['content']
		words = content.lower().split()
		p = pnrapi.PNRAPI(words[1]) #10-digit PNR Number
		if p.request() == True:
			response = p.get_json()
		else:
			return "Service unavailable"
		res = response['ticket_type'] +"\n"	
		return res 
handler_class = irctc
