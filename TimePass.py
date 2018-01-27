from typing import Any, Dict
from imdbpie import Imdb
import lyricwikia
from weather import Weather
from zulip_bots.bots.TimePass import utils, sps, mindGame, hangman, scrabble, todo, calculator, news
import os


class TimePass(object):
    '''
    A docstring documenting this bot.
    '''

    def usage(self):
        return '''Build with python and Zulip chat api, Jarvis Bot is the most feature rich unofficial Zulip chat bot that is 100% free and open source.'''

    def handle_message(self, message: Dict[str, str], bot_handler: Any) -> None:
        results = []
        query = ""
        if message["content"] == "" or message["content"] == "@jarvis help":
            results.append(utils.HELP_MESSAGE)

        data = message["content"].split()
        if(len(data) >= 2 and data[0] == "@jarvis"):
            query = data[1]

        addData = ''
        if data.__len__() > 3:
            addData = data[3]

        if query == "movies":
            results.append(self.query_movie(data[2], addData))
        elif query == "weather":
            dataTemp = data[2::]
            dataTemp = " ".join(dataTemp)
            results.append(self.query_weather(dataTemp))
        elif query == "lyrics":
            dataTemp = data[3::]
            dataTemp = " ".join(dataTemp)
            results.append(self.query_lyrics(data[2],dataTemp))
        elif query == "man":
            results.append(self.query_man(data[2]))
        elif query == "ssh":
            dataTemp = data[5::]
            dataTemp = " ".join(dataTemp)
            results.append(self.query_ssh(data[2],data[3],data[4],dataTemp))
        elif query == "sps":
            results.append(sps.get_sps_response(message, bot_handler))
        elif query == "mind-game":
        	results.append(mindGame.get_mindGame_response(message,bot_handler))
        elif query == "hangman":
        	results.append(hangman.get_response(message,bot_handler))
        elif query == "scrabble":
        	results.append(scrabble.get_response(message,bot_handler))
        elif query == "todo":
        	results.append(todo.get_todo_response(message,bot_handler))
        elif query == "calculator":
            results.append(calculator.get_calculator_response(message,bot_handler))
        elif query == "news":
            results.append(news.get_news_response(message,bot_handler))
        else:
        	results.append(utils.QUICK_HELP) 

        new_content = ''
        for idx, result in enumerate(results, 1):
            new_content += ((str(idx)) if len(results) > 1 else '') + result + '\n'

        bot_handler.send_reply(message, new_content)

    def query_movie(self, query, data):

        imdb = Imdb()
        res = ""
        if query == "popularshows":
            ans = imdb.get_popular_shows()
            for i in range(10):
                res += ans['ranks'][i]['title'] + "\n"
        elif query == "popularmovies":
            ans = imdb.get_popular_movies()
            for i in range(10):
                res += ans['ranks'][i]['title'] + "\n"
        elif query == "search":
            ans = imdb.search_for_title(data)
            for i in range(5):
                res += ans[i]['title'] + "\n"
        return res

    def query_lyrics(self, artist, song):
        return lyricwikia.get_lyrics(artist, song)

    def query_weather(self,city):

        weather = Weather()

        location = weather.lookup_by_location(city)
        res = ""
        forecast = location.forecast()
        for forecasts in forecast:
            res += 'Date: ' + forecasts.date() + '\nCondition: ' + forecasts.text() + '\nHigh Temperature (F): ' + forecasts.high() + '\nLow Temperature (F): ' + forecasts.low() + '\n\n'
        return res

    def query_man(self, command):

        os.system("man " + command + " > man.txt")
        file = open("man.txt","r")
        return file.read()

    def query_ssh(self,user,server,password, command):

        command = "sshpass -p " + password + " ssh " + user + "@" + server + ' "' + command +  '" > output.txt 2>  error.txt'
        os.system(command)
        output = open("output.txt","r")
        error = open("error.txt","r")

        return output.read() + " " + error.read()

handler_class = TimePass