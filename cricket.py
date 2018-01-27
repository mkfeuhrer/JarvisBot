from zulip_bots.bots.irctc import pnrapi
from zulip_bots.bots.converter import utils
from pycricbuzz import Cricbuzz
from typing import Any, Dict, List

class cricket(object):

	def usage(self) -> str:
		return '''This plugin is for Fetching Cricket Scores'''

	def handle_message(self, message: Dict[str, str], bot_handler: Any) -> None:
		bot_response = self.get_cricket_response(message, bot_handler)
		bot_handler.send_reply(message, bot_response)

	def get_cricket_response(self, message: Dict[str, str], bot_handler: Any) -> str:
		content = message['content']
		words = content.lower().split()
		c = Cricbuzz( ) 
		matches = c.matches( )
		val = "\n" + match + "\n"
		for match in matches :
			if( match['mchstate'] != 'nextlive') :
				val = val + c.livescore( match['id'] ) + "\n"
				val = val + c.commentary( match['id'] ) + "\n" 
				val = val + c.scorecard( match['id'] ) + "\n"
		return val   
handler_class = cricket
